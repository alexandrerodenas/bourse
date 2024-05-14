import { GREEN_COLOR, RED_COLOR } from './colors.js';

const TABLE_OPTIONS = [
  { data: 'name', title: 'Nom' },
  { data: 'number', title: 'Nombre' },
  { data: 'unit_cost', title: 'Prix achat (€)' },
  { data: 'current_price', title: 'Prix clotûre (€)' },
  { data: 'stock_value_investment', title: 'Investissement total (€)' },
  { data: 'stock_value_estimation', title: 'Valorisation (€)' },
  { data: 'difference_value_euros', title: 'Gain/Perte (€)' },
  { data: 'difference_value_percentage', title: 'Gain/Perte (%)' },
];
const LENGTH_MENU_OPTIONS = [
  [5, 10, 25, 50, -1],
  [5, 10, 25, 50, 'Tous'],
];
const DEFAULT_PAGE_LENGTH = 10;

export function createDataTable(portfolio) {
  const tabPane = createTabPane(portfolio.id);
  populateDataTable(tabPane.id, portfolio.stocks);
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
  table.classList.add('table', 'is-bordered', 'is-striped', 'is-narrow',
    'is-hoverable', 'is-fullwidth');
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

function formatDigit(cell) {
  const value = parseFloat(cell.innerHTML);
  cell.innerHTML = value.toFixed(2);
}

function getCell(row, columnName) {
  const index = TABLE_OPTIONS.findIndex(
    option => option.data === columnName
  );
  return row.getElementsByTagName('td')[index];
}

function createRow(row, data) {
  formatDigit(getCell(row, "current_price"));
  formatDigit(getCell(row, "stock_value_estimation"));

  const gainLossCell = getCell(row, "difference_value_euros");
  const gainLoss = parseFloat(gainLossCell.innerHTML);
  if (gainLoss < 0) {
    row.querySelectorAll('*').forEach(child => child.style.color = RED_COLOR);
  }

  const nomCell = getCell(row, "name");
  nomCell.innerHTML = capitalizeString(nomCell.innerHTML);

  getCell(row, "current_price").innerHTML += getCaretIcon(data.change);
}

function capitalizeString(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function getCaretIcon(change) {
  if (change === 'increased') {
    return ' <i style=\'color: ' + GREEN_COLOR + '\' class=\'fas fa-caret-up\'>';
  } else if (change === 'decreased') {
    return ' <i style=\'color: ' + RED_COLOR + '\' class=\'fas fa-caret-down\'>';
  } else {
    return "";
  }
}