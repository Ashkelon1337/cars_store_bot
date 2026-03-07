from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


catalog = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text='•🚗 Tesla Model 3 — 4.5M ₽', callback_data='car_0')],
    [InlineKeyboardButton(text='•🚙 BMW X5 — 5.5M ₽', callback_data='car_1')],
    [InlineKeyboardButton(text='•🏎️ Audi RS6 — 8M ₽', callback_data='car_2')],
    [InlineKeyboardButton(text='•🚘 Mercedes S-Class — 12M ₽', callback_data='car_3')],
])
caption_car = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⬅️ Назад к каталогу', callback_data='return_to_catalog'),
     InlineKeyboardButton(text='➕ Добавить в корзину', callback_data='Add_to_basket')]
])