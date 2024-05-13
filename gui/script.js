import { fetchPortfolios } from './api.js';
import {
    createDataTable,
} from './datatables.js';
import { createTab } from './tabs.js';
import { attachTabClickListeners, activePortfolio } from './listeners.js';
import { populateAdditionalInfo } from './additionalInfo.js';
import { drawPortfoliosEvolution } from './charts/investment-versus-market.chart.js';
import { drawGainLossChart } from './charts/gain-loss.chart.js';



document.addEventListener('DOMContentLoaded', function () {
    fetchPortfolios()
        .then(portfolios => {
            portfolios.forEach(portfolio => {
                createTab(portfolio)
                createDataTable(portfolio)
                populateAdditionalInfo(portfolio);
            });
            activePortfolio(portfolios[0].id);
            attachTabClickListeners();
            drawPortfoliosEvolution(portfolios);
            drawGainLossChart(portfolios);
        })
        .catch(error => console.error('Error fetching data:', error));
});



