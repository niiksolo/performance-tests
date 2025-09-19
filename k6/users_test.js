import http from 'k6/http';
import { sleep, check } from 'k6';
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';

export let options = {
  vus: 10,           // количество виртуальных пользователей
  duration: '30s',   // время нагрузки
  thresholds: {
    'http_req_duration': ['p(95)<500'], // 95% запросов < 500ms
  },
};

export default function () {
  let res = http.get('https://reqres.in/api/users?page=2');

  // Функциональные проверки
  check(res, {
    'status is 200': (r) => r.status === 200,
    'page = 2': (r) => r.json().page === 2,
    'data array exists': (r) => Array.isArray(r.json().data),
    'first user has id': (r) => r.json().data[0].id !== undefined,
  });

  sleep(1); // имитация паузы между итерациями
}

// Генерация HTML отчета
export function handleSummary(data) {
  return {
    'site/k6/index.html': htmlReport(data),
  };
}