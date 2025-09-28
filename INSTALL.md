# Установка и запуск

## Требования
- Python 3.8+
- pip

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Rokki-Khazratov/GeoAgro-reports.git
cd GeoAgro-reports
```

2. Создайте виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
# или
.venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
cp env.example .env
# Отредактируйте .env файл
```

5. Запустите бота:
```bash
python app.py
```

## Переменные окружения

Скопируйте `env.example` в `.env` и заполните:

- `BOT_TOKEN` - токен Telegram бота
- `REPORT_CHAT_ID` - ID группы для отчетов
- `TECH_CHAT_ID` - ID тех-чата (опционально)
- `API_BASE_URL` - URL API сервера
- `API_USERNAME` - логин для API
- `API_PASSWORD` - пароль для API
