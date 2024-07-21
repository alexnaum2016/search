from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello!')

def main() -> None:
    # Создание экземпляра Updater с использованием токена
    updater = Updater(token="7150994983:AAHDblfvLA8xUfXHxGOCZKATAhtIyFtcs54", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    # Запуск Polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
