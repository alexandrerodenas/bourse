const API_URL = 'http://localhost:8000/history';

export function fetchPortfolios() {
  return fetch(API_URL)
  .then(response => response.json());
}

export function fetchGainLossHistory() {
  return fetch(`${API_URL}/gain-loss`)
    .then(response => response.json());
}


export function fetchInvestmentHistory() {
  return fetch(`${API_URL}/investment`)
  .then(response => response.json());
}