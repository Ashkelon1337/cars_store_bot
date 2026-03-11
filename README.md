# 🚗 Car Shop Bot

Telegram бот для продажи автомобилей с каталогом и корзиной.

## Возможности
- Каталог машин с фото и описанием
- Просмотр детальной информации
- Добавление в корзину с выбором количества
- FSM для оформления заказа

## Команды
- "/start" - Начало работы
- Кнопка "🚗 Каталог" - список машин
- Кнопка "🛒 Корзина" - просмотр корзины

## Установка
### 1.
    git clone https://github.com/Ashkelon1337/cars_store_bot.git
    cd cars_store_bot
### 2.
    python -m venv .venv 
    source .venv/bin/activate # для Linux/Mac
    
    .venv\Scripts\activate # для Windows
### 3.
    Установи зависимости: `pip install -r requirements.txt`
    Создай файл `.env` с токеном: BOT_TOKEN=твой_токен_сюда
    Запусти: `python run.py`
