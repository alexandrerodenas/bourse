import { formatDate } from './date-utils.js';

export function drawGainLossChart(series){
  formatDate(series)
  Highcharts.chart('gain-loss', {
    title: {
      text: 'Gain/Perte',
    },
    xAxis: {
      type: 'datetime',
      title: {
        text: 'Date',
      },
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
    series: series,
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
