from aiogram import Router, types
from aiogram.filters import Command
from datetime import datetime
from texts import format_daily, UZ_LOADING, UZ_OK, UZ_ERR
from api import get_daily_report, health
from config import ADMIN_IDS

router = Router()

@router.message(Command("start"))
async def start(m: types.Message):
    welcome_text = (
        "Assalomu aleykum!\n\n"
        "Men GeoAgro Reports botman. "
        "Kunlik va haftalik hisobotlarni yuboraman.\n\n"
        "Yordam uchun: @rokki_khazratov"
    )
    await m.answer(welcome_text)

@router.message(Command("ping"))
async def ping(m: types.Message):
    # Только для админов
    if m.from_user.id not in ADMIN_IDS:
        await m.answer("❌ Bu buyruq faqat adminlar uchun")
        return
    data = await health()
    await m.answer(f"pong: {data.get('status','?')} {data.get('tz','')}", disable_web_page_preview=True)

@router.message(Command("report"))
async def manual_report(m: types.Message):
    # Только для админов
    if m.from_user.id not in ADMIN_IDS:
        await m.answer("❌ Bu buyruq faqat adminlar uchun")
        return
    # /report [YYYY-MM-DD]
    parts = m.text.split()
    d = None
    if len(parts) > 1:
        try:
            datetime.strptime(parts[1], "%Y-%m-%d")
            d = parts[1]
        except ValueError:
            await m.answer("Format: /report YYYY-MM-DD")
            return
    try:
        payload = await get_daily_report(d)
        msg = format_daily(payload, suffix=(d or "manual"))
        await m.answer(msg, parse_mode="HTML")
    except Exception as e:
        await m.answer(f"{UZ_ERR}\n{e!s}")
