# 🚗 Car Shop Bot

A Telegram bot for automotive sales, featuring an interactive product catalog and a fully functional shopping cart system.

---

## 📌 Features

* **Visual Vehicle Catalog:** Browsable list of cars complete with high-quality images and detailed descriptions.
* **Granular Product Specifications:** View deep-dive details for every vehicle entry.
* **Smart Cart Integration:** Add items to the shopping cart with dynamic quantity selection.
* **Streamlined Ordering Process:** Utilizes FSM (Finite State Machine) to guide users smoothly through order placement.

---

## 🎮 Bot Commands & Controls

* `/start` — Initializes the bot and opens the main menu.
* `🚗 Catalog` (Reply Button) — Displays the list of available vehicles.
* `🛒 Cart` (Reply Button) — Reviews items currently inside the shopping cart.

---

## 🚀 Installation & Setup

1. **Clone the repository and navigate to the project root:**
    ```bash
    git clone [https://github.com/Ashkelon1337/cars_store_bot.git](https://github.com/Ashkelon1337/cars_store_bot.git)
    cd cars_store_bot
    ```
2. **Install the required packages:**
    ```bash pip install -r requirements.txt```
3. **Create a .env file in the root directory and add your secret token:**
    ```bash BOT_TOKEN=your_bot_token_here```
4. **Start the Telegram bot:**
    ```bash python run.py```
