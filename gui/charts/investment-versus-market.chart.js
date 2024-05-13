export function drawPortfoliosEvolution(history) {
  history.forEach(history => {
    history.portfolio_date = new Date(history.portfolio_date);
  });

  const margin = { top: 20, right: 30, bottom: 60, left: 60 };
  const width = 1000 - margin.left - margin.right;
  const height = 400 - margin.top - margin.bottom;

  const svg = d3.select('#investment-market').
    attr('width', width + margin.left + margin.right).
    attr('height', height + margin.top + margin.bottom).
    append('g').
    attr('transform', `translate(${margin.left},${margin.top})`);

  const colors = d3.scaleOrdinal().
    domain(['total_market_value', 'total_investment_amount']).
    range(d3.schemeSet2);

  const dataReady = ['total_market_value', 'total_investment_amount'].map(
    function (grpName) { // .map allows to do something for each element of the list
      return {
        name: grpName,
        title: toTitleCase(grpName),
        values: history.map(p =>
          ({
            time: new Date(p.date),
            value: +p[grpName],
            gain_deficit: p.total_gain_deficit,
          }),
        ),
      };
    });

  const uniqueDates = Array.from(
    new Set(history.map(p => p.date)));

  const xScale = d3.scaleUtc().
    domain(d3.extent(uniqueDates, d => new Date(d))).
    range([0, width]);

  const yScale = d3.scaleLinear().domain([
    0,
    d3.max(history,
      d => Math.max(d.total_investment_amount, d.total_market_value)),
  ]).nice().range([height, 0]);

  const line = d3.line().
    x(function (d) { return xScale(+d.time); }).
    y(function (d) { return yScale(+d.value); });
  svg.selectAll('myLines').
    data(dataReady).
    enter().
    append('path').
    attr('class', function (d) { return d.name; }).
    attr('d', function (d) { return line(d.values); }).
    attr('stroke', function (d) { return colors(d.name); }).
    style('stroke-width', 4).
    style('fill', 'none');

  svg.selectAll('myDots').
    data(dataReady).
    enter().
    append('g').
    style('fill', function (d) { return colors(d.name); }).
    attr('class', function (d) { return d.name; }).selectAll('myPoints').
    data(function (d) { return d.values; }).
    enter().
    append('circle').
    attr('cx', function (d) { return xScale(d.time); }).
    attr('cy', function (d) { return yScale(d.value); }).
    attr('r', 5).
    attr('stroke', 'white');

  svg.selectAll('.legend').
    data(dataReady).
    enter().
    append('g').
    append('text').
    attr('x', function (d, i) { return 30 + i * 200;}).
    attr('y', 30).
    text(function (d) { return d.title; }).
    style('fill', function (d) { return colors(d.name); }).
    style('font-size', 15).
    on('click', function (d) {
      const currentOpacity = d3.selectAll('.' + d.name).style('opacity');
      d3.selectAll('.' + d.name).
        transition().
        style('opacity', currentOpacity == 1 ? 0 : 1);

    });

  svg.append('g').
    attr('transform', `translate(0,${height})`).
    call(d3.axisBottom(xScale).ticks(uniqueDates.length));

  svg.append('g').call(d3.axisLeft(yScale));

  svg.append('text').
    attr('transform', `translate(${width / 2},${height + margin.top + 10})`).
    style('text-anchor', 'middle').
    text('Date');

  svg.append('text').
    attr('transform', 'rotate(-90)').
    attr('y', 0 - margin.left).
    attr('x', 0 - (height / 2)).
    attr('dy', '1em').
    style('text-anchor', 'middle').
    text('Montant');
}

function toTitleCase(str) {
  return str.replace(
    /\b\w+/g,
    function (txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    },
  ).replace(/_/g, ' ');
}