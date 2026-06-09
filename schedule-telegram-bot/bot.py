'''
import pandas as pd
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Твій токен
TOKEN = ""
# TOKEN = "ВСТАВ_СЮДИ_ТОКЕН_З_BOTFATHER"

# 🔗 Лінк на CSV
CSV_URL = ""
# CSV_URL = "https://docs.google.com/spreadsheets/d/ID/export?format=csv"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я бот із розкладом. Напиши /schedule щоб побачити його.")

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    df = pd.read_csv(CSV_URL)
    text = df.to_string(index=False)  # перетворюємо в текст
    await update.message.reply_text(f"Ось твій розклад:\n\n{text}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("schedule", schedule))
    app.run_polling()

if __name__ == "__main__":
    main()
'''

import logging
import pandas as pd
import datetime
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === Налаштування ===
TOKEN = "7658069538:AAGg3ln8fyPhindqzJWQhli_7vitEBOhZWw"
# TOKEN = "ВСТАВ_СЮДИ_ТОКЕН_З_BOTFATHER"
CSV_URL = "https://docs.google.com/spreadsheets/d/1WABeYlt2gBW0ADi2iutxQztu1DAHUY3w0Ap83XQnfHo/export?format=csv"
# CSV_URL = "https://docs.google.com/spreadsheets/d/ID/export?format=csv"

# === Логи для відладки ===
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# === Функція завантаження таблиці ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я бот із розкладом.Є" + \
    "Напиши /today щоб побачити його на сьогодні." + \
    "Напиши /tomorrow щоб побачити його на сьогодні." + \
    'Напиши /date щоб побачити його на конкретну дату.')


def load_schedule():
    try:
        df = pd.read_csv(CSV_URL)
        return df
    except:
        return None

# === Команди ===
async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    df = load_schedule()
    if df is None:
        await update.message.reply_text("Не можу завантажити розклад 😢")
        return

    today = datetime.date.today().strftime("%Y-%m-%d")
    schedule = df[df["Date"] == today]

    if schedule.empty:
        text = f"📅 На {today} занять немає."
    else:
        text = f"📅 Розклад на {today}:\n"
        for _, row in schedule.iterrows():
            text += f"— {row['Start_time']} {row['End_time']} ({row['Subject']})\n"

    await update.message.reply_text(text)

async def tomorrow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    df = load_schedule()
    if df is None:
        await update.message.reply_text("Не можу завантажити розклад 😢")
        return

    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    schedule = df[df["Date"] == tomorrow]

    if schedule.empty:
        text = f"📅 На {tomorrow} занять немає."
    else:
        text = f"📅 Розклад на {tomorrow}:\n"
        for _, row in schedule.iterrows():
            text += f"— {row['Start_time']} {row['End_time']} ({row['Subject']})\n"

    await update.message.reply_text(text)

async def by_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Використання: /date YYYY-MM-DD")
        return

    date = context.args[0]
    df = load_schedule()
    if df is None:
        await update.message.reply_text("Не можу завантажити розклад 😢")
        return

    schedule = df[df["Date"] == date]
    if schedule.empty:
        text = f"📅 На {date} занять немає."
    else:
        text = f"📅 Розклад на {date}:\n"
        for _, row in schedule.iterrows():
            text += f"— {row['Start_time']} {row['End_time']} ({row['Subject']})\n"

    await update.message.reply_text(text)

# === Запуск бота ===
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("tomorrow", tomorrow))
    app.add_handler(CommandHandler("date", by_date))



    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
