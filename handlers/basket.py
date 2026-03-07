from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()
class Add_to_basket(StatesGroup):
    product = State()
    quantity = State()
    current_car = State()
baskets = {}
@router.callback_query(F.data == 'Add_to_basket')
async def Add_start(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    car_id = data.get('current_car')
    if car_id is None:
        await callback.answer("Ошибка! Выберите машину заново")
        return
    await state.update_data(product=car_id)
    await state.set_state(Add_to_basket.quantity)
    await callback.message.answer('Сколько штук добавить?')
    await callback.answer()

@router.message(Add_to_basket.quantity)
async def add_quantity(message: Message, state : FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите число!")
        return
    from new_cars_data import cars
    quantity = int(message.text)
    user_id = message.from_user.id

    data = await state.get_data()
    car_id = data['product']
    car = cars[car_id]
    if user_id not in baskets:
        baskets[user_id] = {}
    if car_id in baskets[user_id]:
        baskets[user_id][car_id] += quantity
    else:
        baskets[user_id][car_id] = quantity
    await state.clear()
    await message.answer(f'✅{car['name']} добавлена в корзину!\nКолчисетво: {quantity}')

@router.message(F.text == '🛒 Корзина')
async def show_basket(message: Message):
    user_id = message.from_user.id
    if user_id not in baskets or not baskets[user_id]:
        await message.answer("🛒 Корзина пуста")
        return
    from new_cars_data import cars
    text = "🛒 **Твоя корзина:**\n\n"
    total = 0
    for car_id, quantity in baskets[user_id].items():
        car = cars[car_id]
        price = car['price'] * quantity
        total += price
        text += f"• {car['name']} в колчестве {quantity} = {price}₽\n"
    text += f'\n**Итого: {total}₽**'
    await message.answer(text)