import http from 'k6/http';
import { sleep, check } from 'k6';
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';

export let options = {
  vus: 50,          // количество виртуальных пользователей
  duration: '30s',  // время нагрузки
};

export default function () {
  let res = http.get('https://reqres.in/api/users?page=2');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
  });

  sleep(1);
}

// Генерация HTML отчета
export function handleSummary(data) {
  return {
    'site/k6/index.html': htmlReport(data),
  };
}