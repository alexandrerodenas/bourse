import { formatDate } from './date-utils.js';

export function drawPortfoliosEvolution(series) {
  formatDate(series)

  Highcharts.chart('investment-market', {
    title: {
      text: 'Investissement/Estimation',
    },
    xAxis: {
      type: 'datetime',
      title: {
        text: 'Date',
      }
    },
    yAxis: {
      title: {
        text: 'Montant',
      },
    },
    legend: {
      layout: 'horizontal',
      align: 'center',
      verticalAlign: 'top',
    },
    series: series.map(item => ({
      name: translate(item.name),
      data: item.data,
    })),
    responsive: {
      rules: [{
        condition: {
          maxWidth: 500
        },
        chartOptions: {
          legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom'
          }
        }
      }]
    }
  });
}

function translate(title){
  if(title === "total_market_value"){
    return "Estimation"
  } else {
    return "Investissement"
  }
}