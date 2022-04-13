from telebot import types
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

main_buttons = ReplyKeyboardMarkup([
    ['Bugun'], ['Ertaga', "To'liq taqvim"], ["Mintaqa"], ["Duo"]
], resize_keyboard=True)


def start(update:Update, context:CallbackContext):
    user = update.message.chat.first_name

    # buttons = [
    #     [
    #         keyboard = types.ReplyKeyboardMarkup(row_width=1)
    #
    #     keyboard.add(
    #         types.KeyboardButton('⬅️Назад'),
    #         types.KeyboardButton('📩Оставить Заявку', request_contact=True)
    #     )
    #     return keyboard
    #     ]
    # ]

    buttons = [
        [
            InlineKeyboardButton('Buxoro', callback_data='buxoro'),
            InlineKeyboardButton('Andijon', callback_data='andijon'),
            InlineKeyboardButton("Farg'ona", callback_data="farg'ona"),
        ],
        [
            InlineKeyboardButton('Jizzax', callback_data='jizzax'),
            InlineKeyboardButton('Xorazm', callback_data='xorazm'),
            InlineKeyboardButton('Namangan', callback_data='namangan'),
        ],
        [
            InlineKeyboardButton('Navoiy', callback_data='navoiy'),
            InlineKeyboardButton('Qashqadaryo', callback_data='qashqadaryo'),
            InlineKeyboardButton('Nukus', callback_data='nukus'),
        ],
        [
            InlineKeyboardButton('Samarqand', callback_data='samarqand'),
            InlineKeyboardButton('Sirdaryo', callback_data='sirdaryo'),
            InlineKeyboardButton('Surxondaryo', callback_data='surxondaryo'),
        ],
        [
            InlineKeyboardButton('Tashkent', callback_data='tashkent')
        ]
    ]

    update.message.reply_text(f"Assalomu alaykum <u><b>{user}</b></u>. \t<b>Ro'zai-ramazon oyi hayrli va barokatli bo'lsin</b> 🕌 !!️ \n\n Sizga qaysi mintaqa bo'yicha ma'lumot kerak 🌐 !?",
                              parse_mode='HTML', reply_markup=InlineKeyboardMarkup(buttons))


def inline_callback(update:Update, context:CallbackContext):
    try:
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(text="<b>Ramazon taqvimi</b> 2️⃣0️⃣2️⃣1️⃣ \n \n Quyidagilardan birini tanlang 👇", reply_markup=main_buttons)
    except Exception as e:
        print('error', str(e))


def main():
    updater = Updater('5094107588:AAF_Wp5iTzPn911UiWjsjq9Qvv2JYZ4gtos', use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    main()
