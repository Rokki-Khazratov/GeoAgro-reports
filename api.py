import httpx, asyncio
from typing import Optional
from config import (
    API_BASE_URL, API_REPORT_DAILY, API_HEALTH,
    API_USERNAME, API_PASSWORD, HTTP_TIMEOUT, HTTP_RETRIES
)

# Кэш для JWT токена
_jwt_token = None

async def _get_jwt_token() -> str:
    """Получить JWT токен для аутентификации"""
    global _jwt_token
    if _jwt_token:
        return _jwt_token
    
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as c:
        login_data = {"username": API_USERNAME, "password": API_PASSWORD}
        r = await c.post(f"{API_BASE_URL}/api/login/", json=login_data)
        r.raise_for_status()
        data = r.json()
        _jwt_token = data["access"]
        return _jwt_token

async def _get(url: str, params: Optional[dict] = None) -> dict:
    last_exc = None
    for _ in range(HTTP_RETRIES + 1):
        try:
            token = await _get_jwt_token()
            headers = {"Authorization": f"Bearer {token}"}
            async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as c:
                r = await c.get(url, headers=headers, params=params)
                r.raise_for_status()
                return r.json()
        except Exception as e:
            last_exc = e
            await asyncio.sleep(1.0)
    raise last_exc

async def health() -> dict:
    return await _get(f"{API_BASE_URL}{API_HEALTH}")

async def get_daily_report(date_iso: str | None = None) -> dict:
    """Получить ежедневный отчет, используя admin dashboard данные"""
    try:
        # Сначала попробуем использовать reports endpoint
        params = {"date": date_iso} if date_iso else None
        return await _get(f"{API_BASE_URL}{API_REPORT_DAILY}", params=params)
    except Exception:
        # Если reports endpoint недоступен, используем admin dashboard
        dashboard_data = await _get(f"{API_BASE_URL}/api/admin/dashboard/")
        
        # Преобразуем данные dashboard в формат отчета
        plantations = dashboard_data.get("plantations", {})
        
        return {
            "date": date_iso or "today",
            "total_added": plantations.get("created_today", 0),
            "total_approved": plantations.get("approved_today", 0),
            "total_rejected": plantations.get("rejected_today", 0),
            "top_regions": [
                {"name": region["name"], "count": region["plantations_count"]}
                for region in dashboard_data.get("regions", [])[:3]
                if region["plantations_count"] > 0
            ],
            "top_districts": [],  # Нет данных о районах в dashboard
            "top_users": []  # Нет данных о пользователях в dashboard
        }
