import json
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# --- Загружаем данные ---
with open("output.json", "r", encoding="utf-8") as f:
    data = [json.loads(line) for line in f]

df = pd.json_normalize(data)

# --- Агрегированные метрики ---
summary = df.groupby("metric")["data.value"].agg(
    ["count", "mean", "min", "max"]
).reset_index()

summary.rename(
    columns={
        "metric": "Метрика",
        "count": "Кол-во точек",
        "mean": "Среднее",
        "min": "Мин",
        "max": "Макс",
    },
    inplace=True,
)

# --- Функция для сохранения графика в base64 ---
def plot_to_base64(plt_fig):
    buf = BytesIO()
    plt_fig.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

# --- График: распределение времени ответа ---
plt.figure(figsize=(8, 4))
http_times = df[df["metric"] == "http_req_duration"]["data.value"]
http_times.plot(kind="hist", bins=30, title="Распределение времени отклика (ms)")
plt.xlabel("Время ответа (ms)")
plt.ylabel("Частота")
plt.grid(True, alpha=0.3)
plt.tight_layout()
img_base64 = plot_to_base64(plt.gcf())
plt.close()

# --- Формируем HTML ---
html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>K6 Отчёт</title>
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="p-4">
    <h1 class="mb-4">📊 Отчёт по нагрузочному тестированию (k6)</h1>

    <h2>Сырые данные</h2>
    {df.head(20).to_html(index=False, border=0, classes="table table-striped")}

    <h2>Агрегированные метрики</h2>
    {summary.to_html(index=False, border=0, classes="table table-bordered")}

    <h2>График распределения времени отклика</h2>
    <img src="data:image/png;base64,{img_base64}" class="img-fluid"/>
</body>
</html>
"""

with open("report.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Отчёт создан: report.html")