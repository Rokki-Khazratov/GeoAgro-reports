def _block(arr, key="name"):
    if not arr:
        return "—"
    lines = []
    for i, x in enumerate(arr[:3], 1):
        lines.append(f"{i}. {x.get(key)} — {x.get('count')}")
    return "\n".join(lines)

def format_daily(payload: dict, suffix: str = "18:00") -> str:
    return (
        f"📊 <b>GeoAgro Records — Kunlik hisobot ({suffix})</b>\n\n"
        f"🟢 Yangi qo'shilgan bog'lar: <b>{payload.get('total_added', 0)}</b>\n"
        f"✅ Tasdiqlangan: <b>{payload.get('total_approved', 0)}</b>\n"
        f"❌ Rad etilgan: <b>{payload.get('total_rejected', 0)}</b>\n\n"
        f"🏆 <b>Top 3 hududlar:</b>\n{_block(payload.get('top_regions'))}\n\n"
        f"📍 <b>Top 3 tumanlar:</b>\n{_block(payload.get('top_districts'))}\n\n"
        f"👤 <b>Top 3 foydalanuvchilar:</b>\n{_block(payload.get('top_users'), 'full_name')}"
    )

UZ_LOADING = "⏳ Hisobot tayyorlanmoqda…"
UZ_OK = "✅ Hisobot yuborildi."
UZ_ERR = "⚠️ Hisobot jo'natishda xatolik, keyinroq urinib ko'ring."
