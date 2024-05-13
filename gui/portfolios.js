export function addChangeIndicator(portfolios) {
  return portfolios.reduce((acc, portfolio, index) => {
    const previousPortfolio = acc[index - 1] || { stocks: [] };
    const changes = portfolio.stocks.map(stock => {
      const previousPrice = previousPortfolio.stocks.find(prevVal => prevVal.name === stock.name);
      const change = previousPrice ? (
        stock.current_price > previousPrice.current_price ? 'increased' : (stock.current_price < previousPrice.current_price ? 'decreased' : 'unchanged')
      ) : 'unchanged';
      return { ...stock, change };
    });
    return [...acc, { ...portfolio, stocks: changes }];
  }, []);
}