from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = '8312758635:AAEZwqaa_3ubc9AK7XqMTtcQgnZxEoxlbn0'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привет! Я полезный бот. Напиши /help для списка команд.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(
        "/start - начать\n"
        "/help - помощь\n"
        "/add_note - добавить заметку\n"
        "/show_notes - показать заметки\n"
        "/weather - погода\n"
        "/calc - калькулятор"
    )

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
