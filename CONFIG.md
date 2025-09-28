# Конфигурация

## Переменные окружения

| Переменная       | Описание               | Обязательная        |
| ---------------- | ---------------------- | ------------------- |
| `BOT_TOKEN`      | Токен Telegram бота    | Да                  |
| `REPORT_CHAT_ID` | ID группы для отчетов  | Да                  |
| `TECH_CHAT_ID`   | ID тех-чата для ошибок | Нет                 |
| `API_BASE_URL`   | URL API сервера        | Да                  |
| `API_USERNAME`   | Логин для API          | Да                  |
| `API_PASSWORD`   | Пароль для API         | Да                  |
| `TZ`             | Часовой пояс           | Нет (Asia/Tashkent) |
| `HTTP_TIMEOUT`   | Таймаут запросов       | Нет (20)            |
| `HTTP_RETRIES`   | Количество повторов    | Нет (2)             |

## Пример .env файла

```bash
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
REPORT_CHAT_ID=-1001234567890
TECH_CHAT_ID=-1001234567891
API_BASE_URL=https://api.example.com
API_USERNAME=bot_user
API_PASSWORD=secure_password
TZ=Asia/Tashkent
HTTP_TIMEOUT=30
HTTP_RETRIES=3
```

## Получение BOT_TOKEN

1. Создайте бота через @BotFather
2. Получите токен вида `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
3. Добавьте в .env файл

## Получение CHAT_ID

1. Добавьте бота в группу
2. Отправьте команду `/ping`
3. В логах будет показан ID группы
4. Добавьте в .env файл с минусом: `-1001234567890`
