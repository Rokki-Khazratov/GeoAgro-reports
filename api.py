import httpx, asyncio
from typing import Optional
from config import (
    API_BASE_URL, API_REPORT_DAILY, API_HEALTH,
    API_BOT_TOKEN, HTTP_TIMEOUT, HTTP_RETRIES
)

async def _get(url: str, params: Optional[dict] = None) -> dict:
    last_exc = None
    for _ in range(HTTP_RETRIES + 1):
        try:
            headers = {"X-Bot-Token": API_BOT_TOKEN} if API_BOT_TOKEN else {}
            async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as c:
                r = await c.get(url, headers=headers, params=params)
                r.raise_for_status()
                return r.json()
        except Exception as e:
            last_exc = e
            await asyncio.sleep(1.0)
    raise last_exc

async def health() -> dict:
    """Health check без аутентификации"""
    async with httpx.AsyncClient(timeout=HTTP_TIMEOUT) as c:
        r = await c.get(f"{API_BASE_URL}{API_HEALTH}")
        r.raise_for_status()
        return r.json()

async def get_daily_report(date_iso: str | None = None) -> dict:
    """Получить ежедневный отчет"""
    try:
        # Пробуем использовать reports endpoint
        params = {"date": date_iso} if date_iso else None
        return await _get(f"{API_BASE_URL}{API_REPORT_DAILY}", params=params)
    except Exception as e:
        # Если reports endpoint недоступен, выбрасываем ошибку
        raise Exception(f"Ошибка подключения к API: {str(e)}")
