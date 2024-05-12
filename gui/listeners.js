

export function attachTabClickListeners() {
  const tabLinks = document.querySelectorAll('#apiTabs ul li a');
  tabLinks.forEach(function(tabLink) {
    tabLink.addEventListener('click', function(event) {
      desactiveAll();
      setActive(tabLink);
    });
  });
}

function setActive(tabLink){
  const portfolioId = tabLink.getAttribute('href').substring(1);
  const targetPane = document.getElementById(portfolioId);
  const tab = document.getElementById(`tab-${portfolioId}`)
  tab.classList.add('is-active')
  targetPane.classList.add('is-active');
  targetPane.style.display = 'block'
}

function desactiveAll() {
  document.querySelectorAll('.tab-pane').forEach(function (tabPane) {
    tabPane.classList.remove('is-active');
    tabPane.style.display = 'none';
  });
  document.querySelectorAll('#apiTabs ul li').forEach(function (tab) {
    tab.classList.remove('is-active');
  });
}