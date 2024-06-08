from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Функция обработчика команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Путь к изображению
    photo_path = 'photo.png'

    # Создаем кнопки
    keyboard = [
        [InlineKeyboardButton("Join Us", url='https://t.me/empirecoin_crypto')],
        [InlineKeyboardButton("Play now", url='https://t.me/Empirecoin_bot/Empirecoin')]
    ]

    # Создаем разметку для кнопок
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем фотографию и сообщение с кнопками
    await update.message.reply_photo(photo=open(photo_path, 'rb'), caption='Coming soon!', reply_markup=reply_markup)


def main() -> None:
    # Вставьте свой токен, который вы получили от BotFather
    token = '6993453906:AAGbPh6HanSyMxo7wv_VJRKt63FyGfdnEb0'

    # Создаем объект Application и передаем ему токен бота
    application = Application.builder().token(token).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()


if __name__ == '__main__':
    main()
