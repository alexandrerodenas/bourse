export function drawGainLossChart(history){
  const margin = { top: 20, right: 30, bottom: 60, left: 60 };
  const width = 1000 - margin.left - margin.right;
  const height = 400 - margin.top - margin.bottom;

  const svg = d3.select(`#gain-loss`)
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', `translate(${margin.left},${margin.top})`);

  const data = ['gain_loss'].map(function (grpName) {
    return {
      name: grpName,
      values: history.map(p =>
        ({ time: new Date(p.date), value: p.value })
      ),
    };
  });

  const uniqueDates = Array.from(new Set(history.map(p => p.date)));

  const xScale = d3.scaleUtc()
  .domain(d3.extent(uniqueDates, d => new Date(d)))
  .range([0, width]);

  const yScale = d3.scaleLinear()
  .domain(d3.extent(history, d => d.value))
  .nice()
  .range([height, 0]);

  const line = d3.line()
  .x(function (d) { return xScale(+d.time); })
  .y(function (d) { return yScale(+d.value); });

  // Append the line
  svg.append('line')
  .attr('x1', 0)
  .attr('y1', yScale(0))
  .attr('x2', width)
  .attr('y2', yScale(0))
  .attr('stroke', 'black')
  .attr('stroke-dasharray', '5,5'); // Dotted line style

  svg.selectAll('myDots').
    data(data).
    enter().
    append('g').
    style('fill', 'blue').
    attr('class', function (d) { return d.name; }).selectAll('myPoints').
    data(function (d) { return d.values; }).
    enter().
    append('circle').
    attr('cx', function (d) { return xScale(d.time); }).
    attr('cy', function (d) { return yScale(d.value); }).
    attr('r', 5).
    attr('stroke', 'white');

  svg.selectAll('myLines')
  .data(data)
  .enter()
  .append('path')
  .attr('class', function (d) { return d.name; })
  .attr('d', function (d) { return line(d.values); })
  .attr('stroke', 'blue')
  .style('stroke-width', 4)
  .style('fill', 'none');

  svg.append('g')
  .attr('transform', `translate(0,${height})`)
  .call(d3.axisBottom(xScale).ticks(uniqueDates.length));

  svg.append('g').call(d3.axisLeft(yScale));

  svg.append('text')
  .attr('transform', `translate(${width / 2},${height + margin.top + 10})`)
  .style('text-anchor', 'middle')
  .text('Date');

  svg.append('text')
  .attr('transform', 'rotate(-90)')
  .attr('y', 0 - margin.left)
  .attr('x', 0 - (height / 2))
  .attr('dy', '1em')
  .style('text-anchor', 'middle')
  .text('Gain/Perte');
}
