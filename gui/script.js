import { fetchData } from './api.js';
import {
    activateFirstTab,
    attachTabClickListeners,
    createTabAndDataTable,
} from './datatables.js';



document.addEventListener('DOMContentLoaded', function () {
    fetchData()
        .then(data => {
            data.forEach(createTabAndDataTable);
            activateFirstTab();
            attachTabClickListeners();
        })
        .catch(error => console.error('Error fetching data:', error));
});



