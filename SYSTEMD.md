# Настройка systemd сервиса

## Создание сервиса

Создайте файл `/etc/systemd/system/geoagro-bot.service`:

```ini
[Unit]
Description=GeoAgro Reports Bot
After=network.target

[Service]
Type=simple
User=bot
Group=bot
WorkingDirectory=/opt/GeoAgro-reports
Environment="PYTHONUNBUFFERED=1"
ExecStart=/opt/GeoAgro-reports/.venv/bin/python /opt/GeoAgro-reports/app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Установка

1. Создайте пользователя для бота:
```bash
sudo useradd -r -s /bin/false bot
```

2. Скопируйте файлы в `/opt/GeoAgro-reports`:
```bash
sudo cp -r /path/to/GeoAgro-reports /opt/
sudo chown -R bot:bot /opt/GeoAgro-reports
```

3. Установите зависимости:
```bash
cd /opt/GeoAgro-reports
sudo -u bot python3 -m venv .venv
sudo -u bot .venv/bin/pip install -r requirements.txt
```

4. Настройте переменные окружения:
```bash
sudo -u bot cp env.example .env
sudo -u bot nano .env  # Заполните переменные
```

5. Активируйте сервис:
```bash
sudo systemctl daemon-reload
sudo systemctl enable geoagro-bot
sudo systemctl start geoagro-bot
```

## Управление сервисом

```bash
# Статус
sudo systemctl status geoagro-bot

# Запуск
sudo systemctl start geoagro-bot

# Остановка
sudo systemctl stop geoagro-bot

# Перезапуск
sudo systemctl restart geoagro-bot

# Логи
sudo journalctl -u geoagro-bot -f
```

## Логирование

Логи сохраняются в systemd journal:
```bash
# Последние логи
sudo journalctl -u geoagro-bot -n 50

# Логи в реальном времени
sudo journalctl -u geoagro-bot -f

# Логи за сегодня
sudo journalctl -u geoagro-bot --since today
```
