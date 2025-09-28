# 🚀 Запуск бота

## Быстрый старт

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения
```bash
cp env.example .env
# Отредактируйте .env файл
```

### 3. Запуск бота
```bash
python app.py
```

## Настройка .env файла

```bash
# Telegram Bot Token (получить у @BotFather)
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# ID группы для отчетов (добавить бота в группу и получить ID)
REPORT_CHAT_ID=-1001234567890

# ID тех-чата (опционально, можно = REPORT_CHAT_ID)
TECH_CHAT_ID=-1001234567891

# API настройки
API_BASE_URL=https://luxa.uz
API_BOT_TOKEN=bot_your_bot_token_here

# Часовой пояс
TZ=Asia/Tashkent
```

## Команды бота

- `/start` - приветствие на узбекском языке
- `/ping` - проверка состояния API
- `/report [дата]` - ручной отчет

## Автоматические отчеты

- **Ежедневно** в 18:00 (Asia/Tashkent)
- **Еженедельно** по пятницам в 17:30 (Asia/Tashkent)

## Получение BOT_TOKEN

1. Напишите @BotFather в Telegram
2. Отправьте `/newbot`
3. Введите имя бота
4. Введите username бота
5. Скопируйте полученный токен

## Получение CHAT_ID

1. Добавьте бота в группу
2. Отправьте команду `/ping`
3. В логах будет показан ID группы
4. Добавьте ID в .env с минусом: `-1001234567890`

## Логи

Бот выводит логи в консоль:
```
INFO:aiogram:Bot started
INFO:aiogram:Bot is running
```

## Остановка

Нажмите `Ctrl+C` для остановки бота.
