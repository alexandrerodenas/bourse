const API_URL = 'http://localhost:8000/history';

export function fetchData() {
  return fetch(API_URL)
  .then(response => response.json());
}