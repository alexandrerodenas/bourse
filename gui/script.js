const API_URL = 'http://localhost:5000/history';
const DATE_FORMAT_OPTIONS = {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric'
};
const TABLE_OPTIONS = [
    { data: 'name', title: 'Nom' },
    { data: 'number', title: 'Nombre' },
    { data: 'cost', title: 'Prix achat' },
    { data: 'current_price', title: 'Prix clotûre' },
    { data: 'difference_value_euros', title: 'Gain/Perte (€)' },
    { data: 'difference_value_percentage', title: 'Gain/Perte (%)'}
];
const LENGTH_MENU_OPTIONS = [
    [5, 10, 25, 50, -1],
    [5, 10, 25, 50, "Tous"]
];
const DEFAULT_PAGE_LENGTH = 10;
const RED_COLOR = '#DC143C';

document.addEventListener('DOMContentLoaded', function () {
    fetchData(API_URL)
        .then(data => {
            data.forEach(createTabAndDataTable);
            activateFirstTab();
            attachTabClickListeners();
        })
        .catch(error => console.error('Error fetching data:', error));
});

function fetchData(url) {
    return fetch(url)
        .then(response => response.json());
}

function createTabAndDataTable(entry, index) {
    var formattedDate = formatDate(entry.portfolio_date);
    var tab = createTab(formattedDate);
    var tabPane = createTabPane(formattedDate);
    populateDataTable(tabPane.id, entry.stocks);
    createInfoSeparator(tabPane.id);
    populateAdditionalInfo(entry, tabPane.id);
}

function formatDate(dateString) {
    return new Date(dateString).toLocaleDateString('fr-FR', DATE_FORMAT_OPTIONS)
        .replace(/\//g, '-');
}

function createTab(formattedDate) {
    var tab = document.createElement('li');
    tab.innerHTML = `<a href="#tab${formattedDate}">${formattedDate}</a>`;
    document.querySelector('#apiTabs ul').appendChild(tab);
    return tab;
}

function createTabPane(formattedDate) {
    var tabContent = document.getElementById('tabContent');
    var tabPane = document.createElement('div');
    tabPane.classList.add('tab-pane');
    tabPane.style.display = 'none';
    tabPane.id = `tab${formattedDate}`;
    tabContent.appendChild(tabPane);
    return tabPane;
}

function populateDataTable(tabPaneId, stocks) {
    var tableContainer = document.createElement('div');
    tableContainer.classList.add('table-container');
    document.getElementById(tabPaneId).appendChild(tableContainer);

    var table = document.createElement('table');
    table.classList.add('table', 'is-bordered', 'is-striped', 'is-narrow', 'is-hoverable', 'is-fullwidth');
    table.id = `table${tabPaneId.substr(3)}`;
    tableContainer.appendChild(table);

    var dataTable = new DataTable(table, {
        data: stocks,
        columns: TABLE_OPTIONS,
        lengthMenu: LENGTH_MENU_OPTIONS,
        pageLength: DEFAULT_PAGE_LENGTH,
        createdRow: createRow,
        columnDefs: [
            { targets: [0, 1], className: 'has-text-centered' }
        ],
        autoWidth: false,
    });

    tableContainer.style.overflowY = 'auto';
    tableContainer.style.overflowX = 'hidden';
}

function createRow(row, data) {
    var currentPriceCell = row.getElementsByTagName('td')[3];
    var currentPrice = parseFloat(currentPriceCell.innerHTML);
    currentPriceCell.innerHTML = currentPrice.toFixed(2);

    var gainLossCell = row.getElementsByTagName('td')[4];
    var gainLoss = parseFloat(gainLossCell.innerHTML);
    if (gainLoss < 0) {
        row.style.backgroundColor = RED_COLOR;
    }
}

function activateFirstTab() {
    var firstTab = document.querySelector('#apiTabs ul li:first-child a');
    firstTab.classList.add('is-active');
    var firstTabPaneId = firstTab.getAttribute('href').substring(1);
    document.getElementById(firstTabPaneId).classList.add('is-active');
}

function attachTabClickListeners() {
    var tabLinks = document.querySelectorAll('#apiTabs ul li a');
    tabLinks.forEach(function(tabLink) {
        tabLink.addEventListener('click', function(event) {
            var targetId = this.getAttribute('href').substring(1);
            var targetPane = document.getElementById(targetId);
            document.querySelectorAll('.tab-pane').forEach(function(tabPane) {
                tabPane.classList.remove('is-active');
                tabPane.style.display = 'none';
            });
            document.querySelectorAll('#apiTabs ul li a').forEach(function(tab) {
                tab.classList.remove('is-active');
            });
            this.classList.add('is-active');
            targetPane.classList.add('is-active');
            targetPane.style.display = 'block'
        });
    });
}

function createInfoSeparator(tabPaneId) {
    var separator = document.createElement('hr');
    separator.classList.add('info-separator');
    document.getElementById(tabPaneId).appendChild(separator);
}

function populateAdditionalInfo(entry, tabPaneId) {
    var infoContainer = document.createElement('div');
    infoContainer.classList.add('info-container');
    var totalGainDeficit = parseFloat(entry.total_gain_deficit).toFixed(2);
    var totalInvestmentAmount = parseFloat(entry.total_investment_amount).toFixed(2);
    var totalMarketValue = parseFloat(entry.total_market_value).toFixed(2);
    infoContainer.innerHTML = `
        <h3><i class="fas fa-info-circle"></i> Portfolio information</h3>
        <p><i class="fas fa-money-bill"></i> Montant investit: ${totalInvestmentAmount}€</p>
        <p><i class="fas fa-chart-pie"></i> Montant sur le marché: ${totalMarketValue}€</p>
        <p><i class="fas fa-chart-line"></i> Total Gain/Perte: ${totalGainDeficit}</p>
    `;
    document.getElementById(tabPaneId).appendChild(infoContainer);
}
