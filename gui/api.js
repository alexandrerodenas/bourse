const API_URL = 'http://localhost:8000/history';

export function fetchPortfolios() {
  return fetch(API_URL)
  .then(response => response.json());
}