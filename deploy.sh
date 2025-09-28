#!/bin/bash

# 🚀 Безопасное обновление бота в продакшене

set -e  # Остановить при ошибке

echo "🔄 Начинаем обновление бота..."

# 1. Создаем бэкап
echo "📦 Создаем бэкап..."
cp -r /opt/GeoAgro-reports /opt/GeoAgro-reports.backup.$(date +%Y%m%d_%H%M%S)

# 2. Останавливаем бота
echo "⏹️ Останавливаем бота..."
sudo systemctl stop geoagro-bot || true

# 3. Переходим в директорию
cd /opt/GeoAgro-reports

# 4. Сохраняем .env файл
echo "💾 Сохраняем .env файл..."
cp .env .env.backup

# 5. Получаем обновления
echo "📥 Получаем обновления..."
git fetch origin
git reset --hard origin/main

# 6. Восстанавливаем .env
echo "🔄 Восстанавливаем .env файл..."
cp .env.backup .env

# 7. Обновляем зависимости
echo "📦 Обновляем зависимости..."
sudo -u bot .venv/bin/pip install -r requirements.txt

# 8. Проверяем конфигурацию
echo "🔍 Проверяем конфигурацию..."
sudo -u bot python3 -c "
import os
from config import BOT_TOKEN, REPORT_CHAT_ID, ADMIN_IDS
print(f'✅ BOT_TOKEN: {BOT_TOKEN[:10]}...')
print(f'✅ REPORT_CHAT_ID: {REPORT_CHAT_ID}')
print(f'✅ ADMIN_IDS: {ADMIN_IDS}')
"

# 9. Запускаем бота
echo "🚀 Запускаем бота..."
sudo systemctl start geoagro-bot

# 10. Проверяем статус
echo "📊 Проверяем статус..."
sleep 5
sudo systemctl status geoagro-bot --no-pager

echo "✅ Обновление завершено успешно!"
echo "📝 Логи: sudo journalctl -u geoagro-bot -f"
