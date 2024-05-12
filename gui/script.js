import { fetchPortfolios } from './api.js';
import {
    activateFirstTab,
    createDataTable,
} from './datatables.js';
import { createTab } from './tabs.js';
import { attachTabClickListeners } from './listeners.js';
import { populateAdditionalInfo } from './additionalInfo.js';



document.addEventListener('DOMContentLoaded', function () {
    fetchPortfolios()
        .then(portfolios => {
            portfolios.forEach(portfolio => {
                createTab(portfolio)
                createDataTable(portfolio)
                populateAdditionalInfo(portfolio);
            });
            activateFirstTab();
            attachTabClickListeners();
        })
        .catch(error => console.error('Error fetching data:', error));
});



