const DATE_FORMAT_OPTIONS = {
  day: '2-digit',
  month: '2-digit',
  year: 'numeric'
};

export function createTab(portfolio) {
  const formattedDate = formatDate(portfolio.portfolio_date);
  const tab = document.createElement('li');
  tab.id = `tab-${portfolio.id}`
  tab.innerHTML = `<a href="#${portfolio.id}">${formattedDate}</a>`;
  document.querySelector('#apiTabs ul').appendChild(tab);
  return tab;
}

function formatDate(dateString) {
  return new Date(dateString).toLocaleDateString('fr-FR', DATE_FORMAT_OPTIONS)
  .replace(/\//g, '-');
}