# GeoAgro Reports Bot

Telegram-бот (aiogram 3) для авто-отчётов из GeoAgro API.

## Функции
- Ежедневный отчёт: каждый день **18:00 Asia/Tashkent**
- Еженедельный отчёт: **пятница 17:30 Asia/Tashkent**
- `/report [YYYY-MM-DD]` — ручной отчёт
- `/ping` — health API

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp env.example .env  # заполни переменные
python app.py
```

## Переменные окружения

Смотри env.example (обязательны: BOT_TOKEN, REPORT_CHAT_ID, API_BASE_URL, API_BOT_TOKEN).

## Systemd (опционально)

```ini
[Unit]
Description=GeoAgro Reports Bot
After=network.target

[Service]
WorkingDirectory=/opt/GeoAgro-reports
Environment="PYTHONUNBUFFERED=1"
ExecStart=/usr/bin/python3 /opt/GeoAgro-reports/app.py
Restart=always
User=bot
Group=bot

[Install]
WantedBy=multi-user.target
```

## Примечания

Бэкенд принимает X-Bot-Token (см. docs).

Таймзона: Asia/Tashkent.
