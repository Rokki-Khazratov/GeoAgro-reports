from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot
from texts import format_daily
from api import get_daily_report
from config import TZ, REPORT_CHAT_ID, TECH_CHAT_ID

async def send_daily(bot: Bot):
    try:
        data = await get_daily_report(None)
        await bot.send_message(REPORT_CHAT_ID, format_daily(data, suffix="18:00"), parse_mode="HTML")
    except Exception as e:
        await bot.send_message(TECH_CHAT_ID, f"⚠️ Daily report error: {e!s}")

async def send_weekly(bot: Bot):
    """Еженедельный (пятница 17:30). Можно расширить (на период / limit) позже."""
    try:
        data = await get_daily_report(None)  # MVP: пока суточный с пометкой
        await bot.send_message(REPORT_CHAT_ID, format_daily(data, suffix="Weekly Fri 17:30"), parse_mode="HTML")
    except Exception as e:
        await bot.send_message(TECH_CHAT_ID, f"⚠️ Weekly report error: {e!s}")

def setup_scheduler(bot: Bot):
    sched = AsyncIOScheduler(timezone=TZ)
    # каждый день 18:00
    sched.add_job(lambda: send_daily(bot), CronTrigger(hour=18, minute=0, timezone=TZ))
    # каждую пятницу 17:30
    sched.add_job(lambda: send_weekly(bot), CronTrigger(day_of_week="fri", hour=17, minute=30, timezone=TZ))
    sched.start()
    return sched
