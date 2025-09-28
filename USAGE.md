# Использование бота

## Команды

### `/ping`
Проверяет состояние API сервера.

**Пример:**
```
/ping
```

**Ответ:**
```
pong: ok Asia/Tashkent
```

### `/report [дата]`
Получает отчет за указанную дату или за сегодня.

**Примеры:**
```
/report                    # Отчет за сегодня
/report 2025-09-28        # Отчет за 28 сентября 2025
```

**Ответ:**
```
📊 GeoAgro Records — Kunlik hisobot (18:00)

🟢 Yangi qo'shilgan bog'lar: 15
✅ Tasdiqlangan: 12
❌ Rad etilgan: 3

🏆 Top 3 hududlar:
1. Tashkent — 8
2. Samarkand — 4
3. Fergana — 3

📍 Top 3 tumanlar:
1. Chilonzor — 5
2. Urgut — 3
3. Qo'qon — 2

👤 Top 3 foydalanuvchilar:
1. Aliyev A. — 6
2. Karimov K. — 4
3. Olimova O. — 3
```

## Автоматические отчеты

Бот автоматически отправляет отчеты:

- **Ежедневно** в 18:00 (Asia/Tashkent)
- **Еженедельно** по пятницам в 17:30 (Asia/Tashkent)

## Настройка

Отчеты отправляются в группу, указанную в переменной `REPORT_CHAT_ID`.

Для получения ID группы:
1. Добавьте бота в группу
2. Отправьте любое сообщение
3. Используйте команду `/ping` - в логах будет показан ID группы
