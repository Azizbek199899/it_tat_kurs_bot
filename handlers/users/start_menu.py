from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp,bot
from keyboards.inline.start_menu import menu, menu_courses, ha_yoq
from states.state_group import Register


#bu yerda tugmani bossa xabar alohida boradi pasida

# @dp.callback_query_handler(text='about')
# async def about_message(call:types.CallbackQuery):
#     text="IT TAT O'quv Markazi Zamonaviy IT Yo'nalishlarida Ta'lim Beradi\n"
#     text+="Maqsadimiz-yoshlarni zamonaviy bilimlar bilan ta;minlash\n\n"
#     await call.message.answer(text,parse_mode="Markdown")

#bu yerda esa xabar almashadi

@dp.callback_query_handler(text='about')
async def about_message(call:types.CallbackQuery):
    text="IT TAT O'quv Markazi Zamonaviy IT Yo'nalishlarida Ta'lim Beradi\n"
    text+="Maqsadimiz-yoshlarni zamonaviy bilimlar bilan ta'minlash\n\n"
    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()



@dp.callback_query_handler(text='feedback')
async def feedback_message(call: types.CallbackQuery):
    text = "SAVOLLARIZNI BIZNI TGRAM AKKAUNTIMIZGA YUBORISHINGIZ MUMKIN\n"
    text += "T.me/Uquv_bulimi_it_tat\n\n"
    await call.message.edit_text(text, reply_markup=menu)
    await call.answer()



@dp.callback_query_handler(text='contact')
async def contact_message(call:types.CallbackQuery):
    text="Savollariz bolsa bizga qo'ng'iroq qilishingiz mumkin\n"
    text+="+998(88)6110440\n\n"
    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()

@dp.callback_query_handler(text='news')
async def news_message(call:types.CallbackQuery):
    text="*E'tibor bering! 📅 Yangilangan dars jadvali e'lon qilindi.\n" \
         "O‘quv markazimiz veb-saytida yangi dars vaqtlarini ko‘rishingiz mumkin.\n" \
         "Har qanday savollar bo‘lsa, biz bilan bog‘laning!\n" \
         "Yangiliklar bo‘limida yangiliklarni doimiy ravishda kuzatib boring!*"

    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()


@dp.callback_query_handler(text='location')
async def location_message(call: types.CallbackQuery):
    # O'quv markazining manzilini ko'rsatish
    text = "📍 O'quv markazimiz manzili: Samarqand shahar, Beruniy ko'chasi 32a-Uy\n\n" \
           "📍 Siz bizning joylashuvimizni quyidagi xaritada ko'rishingiz mumkin."

    # Manzilni foydalanuvchiga ko'rsatish
    await call.message.edit_text(text, reply_markup=menu, parse_mode="Markdown")

    # Joylashuvni yuborish
    await call.message.answer_location(latitude=39.677567, longitude=66.926539)  # Bu yerda haqiqiy koordinatalarni qo'shing

    # Call ni tasdiqlash
    await call.answer()




@dp.callback_query_handler(text='contact')
async def contact_message(call:types.CallbackQuery):
    text="📞 Telefon Raqam +998(88)6110440\n"
    text+="📝 Telegram Orqali @Uquv_bulimi_it_tat"
    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()


@dp.callback_query_handler(text='courses')
async def courses_message(call:types.CallbackQuery):
    text="Bizda mavjud kurslar\n\n"
    await call.message.edit_text(text,reply_markup=menu_courses,parse_mode="Markdown")
    await call.answer()


@dp.callback_query_handler(text='back')
async def back_message(call:types.CallbackQuery):
    text="Siz bosh menudasiz !\n\n"
    await call.message.edit_text(text,reply_markup=menu,parse_mode="Markdown")
    await call.answer()

# @dp.callback_query_handler(text='backend')
# async def backend_message(call: types.CallbackQuery):
#     image_url = "https://play-lh.googleusercontent.com/mHEywwrourM3N9Z94du0IqO7tVu0cm78E0NeYdUFUwDAvfPLtFt0jXMGbh8mIcapDio"
#
#     # Matn
#     text = (
#         "📖Ta'lim maqsadi: Server tomonidagi dasturlashni o'rganish."
#         " Python, Node.js yoki Java kabi tillar yordamida ma'lumotlar bazalari bilan ishlashni o'z ichiga oladi\n"
#         "📒Asosiy texnologiyalar: RESTful API, SQL, NoSQL"
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()
#
# @dp.callback_query_handler(text='frontend')
# async def frontend_message(call: types.CallbackQuery):
#     image_url = "https://bilgi.uz/upload/resize_cache/iblock/c94/cbr99q2o55k2fnmbbc0j032w7jpjsnqy/354_225_2/Front-End%20Developer%20(5).jpg"
#     text = (
#         "📖 Ta'lim maqsadi: Veb-saytlar va veb-ilovalar uchun foydalanuvchi interfeyslarini yaratish.\n"
#         "HTML, CSS va JavaScript tillaridan foydalaniladi.\n"
#         "📒 Asosiy texnologiyalar: React, Angular, Vue.js"
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()
#
# @dp.callback_query_handler(text='smm')
# async def smm_message(call: types.CallbackQuery):
#     image_url = "https://bilgi.uz/upload/resize_cache/iblock/e6f/qewr6knvc1r81eioy4lk4ako3n1ctle1/354_225_2/SMM%20professional%20(5).jpg"
#     text = (
#         "📖 Ta'lim maqsadi: Ijtimoiy tarmoqlarda brendlarni rivojlantirish va marketing strategiyalarini o'rganish.\n"
#         "📒 Asosiy ko'nikmalar: Kontent yaratish, maqsadli auditoriya, reklama kampaniyalari."
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()
#
# @dp.callback_query_handler(text='cs')
# async def cs_message(call: types.CallbackQuery):
#     image_url = "https://bilgi.uz/upload/resize_cache/iblock/88e/7hl9eh6c3ahnehripfz1ka4pvifdk0zy/354_225_2/KOMPYUTER%20SAVODXONLIGI%20(5).jpg"
#     text = (
#         "📖 Ta'lim maqsadi: Kompyuter va Internetdan samarali foydalanishni o'rganish.\n"
#         "Dasturlarni ishlatish, xujjatlar tayyorlash, va Internetdan ma'lumot qidirish ko'nikmalarini o'z ichiga oladi.\n"
#         "📒 Asosiy texnologiyalar: Office dasturlari, elektron pochta, Internet."
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()
#
# @dp.callback_query_handler(text='grafik_dizayner')
# async def graphic_designer_message(call: types.CallbackQuery):
#     image_url = "https://algoritm-ziyo-nur.uz/web/upload/files/grafika/kurslar%D0%BD4.jpg"
#     text = (
#         "📖 Ta'lim maqsadi: Grafik dizayn asoslarini o'rganish, logo, banner va boshqa grafik elementlarni yaratish.\n"
#         "📒 Asosiy texnologiyalar: Grafik dizayn asoslarini o'rganish, logo, banner va boshqa grafik elementlarni yaratish."
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()
#
# @dp.callback_query_handler(text='robot')
# async def robot_message(call: types.CallbackQuery):
#     image_url = "https://р66.навигатор.дети/images/events/cover/bb7d4f1fcd0534415c48913a6bf4faf5_big.jpg"
#     text = (
#         "📖 Ta'lim maqsadi: Robotlarni loyihalash, dasturlash va boshqarish.\n"
#         "Fizik va dasturlash bilimlarini birlashtirish.\n\n"
#         "📒 Asosiy texnologiyalar: Arduino, Raspberry Pi, sensorlar."
#     )
#
#     # Xabarni rasm bilan yangilash
#     await call.message.edit_media(media=types.InputMediaPhoto(media=image_url, caption=text), reply_markup=menu_courses)
#     await call.answer()

@dp.callback_query_handler(text="register")
async def register_course(call: types.CallbackQuery, state: FSMContext):
    await state.finish()  # Oldingi holatlarni tugatish
    await call.message.answer("Ism va familiyangizni kiriting:")
    await Register.fullname.set()  # Holatni o'rnatish

@dp.message_handler(state=Register.fullname)
async def fullname_state(message: types.Message, state: FSMContext):
    fullname = message.text
    await state.update_data({"full_name": fullname})
    await message.answer("Qaysi kursda o'qimoqchisiz?")
    await Register.course.set()

@dp.message_handler(state=Register.course)
async def course_state(message: types.Message, state: FSMContext):
    course = message.text
    await state.update_data({"course": course})
    await message.answer("Telefon raqamingizni kiriting:")
    await Register.phone.set()

@dp.message_handler(state=Register.phone)
async def phone_state(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data({"phone": phone})

    # Foydalanuvchidan kelgan ma'lumotlar va tasdiqlash tugmalari ko'rsatiladi
    data = await state.get_data()
    fullname = data.get('full_name')
    course = data.get('course')

    text = "Quyidagi ma'lumotlar olindi:\n\n"
    text += f"Ism Familiyasi: {fullname}\n"
    text += f"Kurs: {course}\n"
    text += f"Telefon raqami: {phone}\n"
    text += "Ma'lumotlarni tasdiqlaysizmi?"

    await message.answer(text, reply_markup=ha_yoq)
    await Register.confirm.set()

@dp.callback_query_handler(state=Register.confirm)
async def confirm_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    admin_chat_id = 973358587  # Admin chat ID o'rnating

    if call.data == "yes":
        await bot.send_message(
            admin_chat_id,
            f"Yangi ariza:\n\n"
            f"Xodim: {data['full_name']}\n"
            f"Kurs: {data['course']}\n"
            f"Aloqa raqami: {data['phone']}"
        )
        await call.message.answer("✅ Arizangiz muvaffaqiyatli yuborildi!")
    else:
        await call.message.answer("❌ Ariza bekor qilindi. Yana bir bor boshlash uchun /start yozing.")

    await state.finish()
