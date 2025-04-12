from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚 Mavjud kurslar", callback_data='courses'),
            InlineKeyboardButton(text="📖 Biz haqimizda", callback_data='about'),
        ],
        [
            InlineKeyboardButton(text="📞 Aloqa", callback_data='contact'),
            InlineKeyboardButton(text="📍 Manzil", callback_data="location"),
        ],
        [
            InlineKeyboardButton(text="📃 Ro'yxatdan O'tish", callback_data="register"),
            InlineKeyboardButton(text="📣 Yangiliklar", callback_data="news"),
        ],
        [
            InlineKeyboardButton(text="📝 Takliflar", callback_data="feedback"),
        ],
    ],
)

menu_courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚 Backend", callback_data='backend'),
            InlineKeyboardButton(text="📖 Frontend", callback_data='frontend'),
        ],
        [
            InlineKeyboardButton(text="🎥 SMM", callback_data="smm"),
            InlineKeyboardButton(text="💻 Kompyuter Savodxonligi", callback_data="cs"),
        ],
        [
            InlineKeyboardButton(text="🌐 Grafik Dizayner", callback_data="grafik_dizayner"),
            InlineKeyboardButton(text="🤖 Robototexnika", callback_data="robot"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back"),
        ],
    ],
)

ha_yoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="HA", callback_data='yes'),
            InlineKeyboardButton(text="YO'Q", callback_data='not'),
        ],
    ],
)