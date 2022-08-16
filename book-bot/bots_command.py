from telegram.ext import ConversationHandler

NAME = 1
SURNAME = 2
PHONE = 3
DESCRIPTION = 4


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Привет! Я помогу тебе работать со справочником\nДля вывода справочника нажми /export\nДля добавления нажми /import')


def c_export(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Для вывода в строчку нажми -> /v1\nДля вывода построчно нажми -> /v2')


def v1(update, context):
    with open('book_v1.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
    context.bot.send_message(update.effective_chat.id, f'{content}')
    context.bot.send_message(update.effective_chat.id,
                             'Готово!\nЕсли хочешь посмотреть справочник -> /export\nЕсли хочешь добавить -> /import')


def v2(update, context):
    with open('book_v2.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
    context.bot.send_message(update.effective_chat.id, f'{content}')
    context.bot.send_message(update.effective_chat.id,
                             'Готово!\nЕсли хочешь посмотреть справочник -> /export\nЕсли хочешь добавить -> /import')


def c_import(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Введи имя: ')
    return NAME


def name_input(update, context):
    name = update.message.text
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' \nИмя: {name};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Имя: {name};\n\n')
    context.bot.send_message(update.effective_chat.id,
                             'Введи фамилию: ')
    return SURNAME


def surname_input(update, context):
    surname = update.message.text
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Фамилия: {surname};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Фамилия: {surname};\n\n')
    context.bot.send_message(update.effective_chat.id,
                             'Введи номер телефона: ')
    return PHONE


def number_phone_input(update, context):
    num = update.message.text
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Номер телефона: {num};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Номер телефона: {num};\n\n')
    context.bot.send_message(update.effective_chat.id,
                             'Добавь описание: ')
    return DESCRIPTION


def description_input(update, context):
    des = update.message.text
    with open('book_v1.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Описание: {des};')
    with open('book_v2.txt', 'a', encoding='UTF-8') as file:
        file.write(f' Описание: {des};\n\n\n')
    context.bot.send_message(update.effective_chat.id,
                             'Готово!\nЕсли хочешь посмотреть справочник -> /export\nЕсли хочешь еще добавить -> /import')
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Рад был пообщаться! Всего доброго!')

    return ConversationHandler.END
