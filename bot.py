from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

# Асинхронные функции — теперь обязательны
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я полезный бот. Напиши /help для списка команд.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - начать\n"
        "/help - помощь\n"
        "/add_note - добавить заметку\n"
        "/show_notes - показать заметки\n"
        "/weather - погода\n"
        "/calc - калькулятор"
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == '__main__':
    main()
