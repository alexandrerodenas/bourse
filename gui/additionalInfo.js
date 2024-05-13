
export function populateAdditionalInfo(portfolio) {
  const infoContainer = document.createElement('div');
  infoContainer.classList.add('info-container');
  const totalGainDeficit = parseFloat(portfolio.total_gain_deficit).toFixed(2);
  const totalInvestmentAmount = parseFloat(portfolio.total_investment_amount).
    toFixed(2);
  const totalMarketValue = parseFloat(portfolio.total_market_value).toFixed(2);
  infoContainer.innerHTML = `
        <h3><i class="fas fa-info-circle"></i> Portfolio information</h3>
        <p><i class="fas fa-money-bill"></i> Montant investit: ${totalInvestmentAmount}€</p>
        <p><i class="fas fa-chart-pie"></i> Montant sur le marché: ${totalMarketValue}€</p>
        <p><i class="fas fa-chart-line"></i> Total Gain/Perte: ${totalGainDeficit}</p>
    `;
  document.getElementById(portfolio.id).appendChild(infoContainer);
}