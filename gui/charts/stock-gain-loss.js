import { formatDate } from './date-utils.js';

export function drawStockGainLossChart(stockSeries) {
  formatDate(series)

  Highcharts.chart('stock-gain-loss', {
    title: {
      text: 'Historique des gains/pertes'
    },
    xAxis: {
      type: 'datetime',
      title: {
        text: 'Date'
      }
    },
    yAxis: {
      title: {
        text: "Gain/Perte (€)"
      }
    },
    legend: {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'middle'
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