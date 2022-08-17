from ast import Global
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import bots_command

bot = Bot(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
updater = Updater(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
dispatcher = updater.dispatcher

STATE1 = 0


def start(update, context):

    context.bot.send_message(update.effective_chat.id,
                             'Привет, давай сыграем в игру с конфетами.\nДля начала нажми -> /run\nДля показа правил нажми -> /info')


def info_game(update, context):

    context.bot.send_message(update.effective_chat.id,
                             'Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.'
                             '\nЗа один ход можно забрать не более чем 28 конфет.'
                             '\nВсе конфеты оппонента достаются сделавшему последний ход.'
                             '\nДля начала нажми -> /run')


def start_game(update, context):

    global num_of_players
    num_of_players = 2
    global ostatok
    ostatok = 2021
    global num_of_try
    num_of_try = 28
    global list_of_players
    list_of_players = [i for i in range(1, num_of_players+1)]
    global i
    i = 0
    global candy_take

    context.bot.send_message(update.effective_chat.id,
                             f"\nОсталось {ostatok} конфет.  \nИгрок {list_of_players[i]} может взять не более {num_of_try} конфет: ")
    return STATE1


def candy_takes(update, context):
    ostatok = 2021
    if num_of_try > ostatok:
        num_of_try = ostatok
    candy_take = update.message.text
    ostatok -= candy_take
    if ostatok == 0:
        context.bot.send_message(update.effective_chat.id,
                                 f"Игрок {list_of_players[i]} забрал последние конфеты. Он победил!!")
        return ConversationHandler.END
    else:
        if i == num_of_players-1:
            i = 0
            context.bot.send_message(update.effective_chat.id,
                                     f"\nОсталось {ostatok} конфет.  \nИгрок {list_of_players[i]} может взять не более {num_of_try} конфет: ")
            return STATE1
        else:
            i += 1
            context.bot.send_message(update.effective_chat.id,
                                     f"\nОсталось {ostatok} конфет.  \nИгрок {list_of_players[i]} может взять не более {num_of_try} конфет: ")
            return STATE1


def cancel(update, context):

    context.bot.send_message(update.effective_chat.id,
                             'Рад был пообщаться! Всего доброго!')

    return ConversationHandler.END


start_handler = CommandHandler('start', start)
start_game_handler = CommandHandler('run', start_game)
info_game_handler = CommandHandler('info', info_game)
candy_take_handler = MessageHandler(Filters.text, candy_takes)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_game_handler],
                                   states={STATE1: [candy_take_handler]},
                                   fallbacks=[cancel_handler])
dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_game_handler)
dispatcher.add_handler(info_game_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(cancel_handler)
print('Server start')
updater.start_polling()
updater.idle()
