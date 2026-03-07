
from aiogram.filters import CommandStart
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
router = Router()

@router.message(CommandStart())
async def comstart(message: Message):
    from keyboards import reply
    await message.answer(
        f'🚗 Привет, {message.from_user.first_name}!\n \n'
        'Я бот магазин крутых тачек. Здесь ты можешь:\n'
        '• Посмотреть каталог автомобилей\n'
        '• Добавить машину в корзину\n'
        '• Оформить заказ\n\n'
        'Используй кнопки внизу 👇', reply_markup=reply.command_start
    )
@router.message(F.text == '🚗 Каталог')
async def Catalog(message: Message):
    from keyboards import inline
    await message.answer(text='🚗 Наши автомобили:', reply_markup=inline.catalog)

@router.callback_query(F.data.in_(['car_0', 'car_1', 'car_2', 'car_3']))
async def show_car(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    id = int(callback.data.split('_')[1])
    await state.update_data(current_car=id)
    from new_cars_data import cars
    car = cars[id]
    name = car['name']
    price = car['price']
    photo = car['photo']
    description = car['desc']
    await callback.message.delete()
    from keyboards import inline
    await callback.message.answer_photo(
        photo=photo,
        caption=f'🚗 {name}\n💰 Цена: {price}₽\n 📝 {description}',
        reply_markup=inline.caption_car
    )
@router.callback_query(F.data == 'return_to_catalog')

async def return_to_catalog(callback: CallbackQuery):
    from keyboards import inline
    await callback.message.delete()
    await callback.message.answer(text='🚗 Наши автомобили:', reply_markup=inline.catalog)
@router.message(F.text == '📞 Контакты')
async def contacts(message: Message):
    text = """
    📞 **Наши контакты:**

    Email: danilashakirov33@gmail.com
    Адрес: Россия

    📱 Telegram: @Ashkelon1337
    
    Режим работы: Круглосуточно
        """
    await message.answer(text)