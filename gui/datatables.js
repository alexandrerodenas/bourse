
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

export function createDataTable(portfolio) {
  const tabPane = createTabPane(portfolio.id);
  populateDataTable(tabPane.id, portfolio.stocks);
  createInfoSeparator(tabPane.id);
  populateAdditionalInfo(portfolio, tabPane.id);
}

function createTabPane(portfolioId) {
  const tabContent = document.getElementById('tabContent');
  const tabPane = document.createElement('div');
  tabPane.classList.add('tab-pane');
  tabPane.style.display = 'none';
  tabPane.id = portfolioId;
  tabContent.appendChild(tabPane);
  return tabPane;
}

function populateDataTable(tabPaneId, stocks) {
  const tableContainer = document.createElement('div');
  tableContainer.classList.add('table-container');
  document.getElementById(tabPaneId).appendChild(tableContainer);

  const table = document.createElement('table');
  table.classList.add('table', 'is-bordered', 'is-striped', 'is-narrow', 'is-hoverable', 'is-fullwidth');
  table.id = `table-${tabPaneId.substr(3)}`;
  tableContainer.appendChild(table);
  new DataTable(table, {
    data: stocks,
    columns: TABLE_OPTIONS,
    lengthMenu: LENGTH_MENU_OPTIONS,
    pageLength: DEFAULT_PAGE_LENGTH,
    createdRow: createRow,
    columnDefs: [
      { targets: [0, 1], className: 'has-text-centered' },
    ],
    autoWidth: false,
  });
  tableContainer.style.overflowY = 'auto';
  tableContainer.style.overflowX = 'hidden';
}

function createRow(row, data) {
  const currentPriceCell = row.getElementsByTagName('td')[3];
  const currentPrice = parseFloat(currentPriceCell.innerHTML);
  currentPriceCell.innerHTML = currentPrice.toFixed(2);

  const gainLossCell = row.getElementsByTagName('td')[4];
  const gainLoss = parseFloat(gainLossCell.innerHTML);
  if (gainLoss < 0) {
    row.style.backgroundColor = RED_COLOR;
  }

  const nomCell = row.getElementsByTagName('td')[0];
  nomCell.innerHTML = capitalizeString(nomCell.innerHTML)
}

function capitalizeString(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

export function activateFirstTab() {
  const firstTabLink = document.querySelector('#apiTabs ul li:first-child a');
  firstTabLink.click()
}


function createInfoSeparator(tabPaneId) {
  const separator = document.createElement('hr');
  separator.classList.add('info-separator');
  document.getElementById(tabPaneId).appendChild(separator);
}

function populateAdditionalInfo(entry, tabPaneId) {
  const infoContainer = document.createElement('div');
  infoContainer.classList.add('info-container');
  const totalGainDeficit = parseFloat(entry.total_gain_deficit).toFixed(2);
  const totalInvestmentAmount = parseFloat(entry.total_investment_amount).
    toFixed(2);
  const totalMarketValue = parseFloat(entry.total_market_value).toFixed(2);
  infoContainer.innerHTML = `
        <h3><i class="fas fa-info-circle"></i> Portfolio information</h3>
        <p><i class="fas fa-money-bill"></i> Montant investit: ${totalInvestmentAmount}€</p>
        <p><i class="fas fa-chart-pie"></i> Montant sur le marché: ${totalMarketValue}€</p>
        <p><i class="fas fa-chart-line"></i> Total Gain/Perte: ${totalGainDeficit}</p>
    `;
  document.getElementById(tabPaneId).appendChild(infoContainer);
}
