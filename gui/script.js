import {
    fetchGainLossHistory,
    fetchInvestmentHistory,
    fetchPortfolios, fetchStockValuesHistory,
} from './api.js';
import {
    createDataTable,
} from './datatables.js';
import { createTab } from './tabs.js';
import { attachTabClickListeners, activePortfolio } from './listeners.js';
import { populateAdditionalInfo } from './additionalInfo.js';
import { drawPortfoliosEvolution } from './charts/investment-versus-market.chart.js';
import { drawGainLossChart } from './charts/gain-loss.chart.js';
import { drawStockValuesChart } from './charts/stock-values-history.chart.js';



document.addEventListener('DOMContentLoaded', function () {
    fetchPortfolios()
        .then(portfolios => {
            portfolios.forEach(portfolio => {
                createTab(portfolio)
                createDataTable(portfolio)
                populateAdditionalInfo(portfolio);
            });
            activePortfolio(portfolios[portfolios.length - 1].id);
            attachTabClickListeners();
        })
        .catch(error => console.error('Error fetching data:', error));

    fetchGainLossHistory()
    .then(history => {
        drawGainLossChart(history);
    })
    .catch(error => console.error('Error fetching data:', error));

    fetchInvestmentHistory()
    .then(history => {
        drawPortfoliosEvolution(history);
    })
    .catch(error => console.error('Error fetching data:', error));

    fetchStockValuesHistory()
    .then(history => {
        drawStockValuesChart(history);
    })
    .catch(error => console.error('Error fetching data:', error));
});



