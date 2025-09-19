# 🚀 Performance Tests

Проект демонстрирует нагрузочное тестирование API с помощью **JMeter** и **k6**,  
а результаты автоматически публикуются в **GitHub Pages**.

---

## 🛠 Технологии

- ⚡ Apache JMeter  
- 📈 k6  
- 🤖 GitHub Actions (CI/CD)  
- 🌐 GitHub Pages (отчёты)

---

## 📊 Что проверяют тесты

### Функциональность
- Проверка HTTP-статуса (200 OK)  
- Проверка структуры JSON (page, data и id)  

### Производительность и нагрузка
- **k6** собирает метрики: среднее время ответа, медиану, p90/p95, максимальное/минимальное время  
- **JMeter** собирает Summary/Aggregate Report  

⚠️ На публичном API **reqres.in** нагрузка ограничена rate limit, поэтому CI иногда показывает частичные ошибки.  
Это связано с внешними ограничениями, а не с тестами.

---

## 📊 Отчёты
- [JMeter Report](https://niiksolo.github.io/performance-tests/jmeter/)  
- [k6 Report](https://niiksolo.github.io/performance-tests/k6/)