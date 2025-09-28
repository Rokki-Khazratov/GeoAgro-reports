# 🚀 Безопасное обновление в продакшене

## 🔒 Ограничения команд

Теперь команды `/ping` и `/report` доступны только админам:

### Настройка админов в .env:
```bash
ADMIN_IDS=123456789,987654321  # Ваши Telegram ID через запятую
```

### Получение своего Telegram ID:
1. Напишите @userinfobot в Telegram
2. Скопируйте ваш ID
3. Добавьте в ADMIN_IDS

## 📦 Безопасное обновление

### Автоматическое обновление:
```bash
# На сервере
cd /opt/GeoAgro-reports
sudo ./deploy.sh
```

### Ручное обновление:
```bash
# 1. Создать бэкап
sudo cp -r /opt/GeoAgro-reports /opt/GeoAgro-reports.backup.$(date +%Y%m%d_%H%M%S)

# 2. Остановить бота
sudo systemctl stop geoagro-bot

# 3. Сохранить .env
cd /opt/GeoAgro-reports
cp .env .env.backup

# 4. Получить обновления
git fetch origin
git reset --hard origin/main

# 5. Восстановить .env
cp .env.backup .env

# 6. Обновить зависимости
sudo -u bot .venv/bin/pip install -r requirements.txt

# 7. Запустить бота
sudo systemctl start geoagro-bot

# 8. Проверить статус
sudo systemctl status geoagro-bot
```

## 🔍 Проверка после обновления

```bash
# Статус сервиса
sudo systemctl status geoagro-bot

# Логи
sudo journalctl -u geoagro-bot -f

# Тест команд (только для админов)
# /start - работает для всех
# /ping - только для админов
# /report - только для админов
```

## 🚨 Откат при проблемах

```bash
# Остановить бота
sudo systemctl stop geoagro-bot

# Восстановить из бэкапа
sudo rm -rf /opt/GeoAgro-reports
sudo mv /opt/GeoAgro-reports.backup.* /opt/GeoAgro-reports

# Запустить
sudo systemctl start geoagro-bot
```

## 📋 Чек-лист обновления

- [ ] Создан бэкап
- [ ] Бот остановлен
- [ ] .env файл сохранен
- [ ] Код обновлен
- [ ] .env восстановлен
- [ ] Зависимости обновлены
- [ ] Бот запущен
- [ ] Статус проверен
- [ ] Команды протестированы
