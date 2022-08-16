from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import bots_command

bot = Bot(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
updater = Updater(token='5492812666:AAFttoWzPNS3eO-0p60bpcKsYidJzcc5j1I')
dispatcher = updater.dispatcher

NAME = 1
SURNAME = 2
PHONE = 3
DESCRIPTION = 4


start_handler = CommandHandler('start', bots_command.start)
export_handler = CommandHandler('export', bots_command.c_export)
import_handler = CommandHandler('import', bots_command.c_import)
cancel_handler = CommandHandler('cancel', bots_command.cancel)
export_v1_handler = CommandHandler('v1', bots_command.v1)
export_v2_handler = CommandHandler('v2', bots_command.v2)
input_name_handler = MessageHandler(Filters.text, bots_command.name_input)
input_surname_handler = MessageHandler(
    Filters.text, bots_command.surname_input)
input_phone_handler = MessageHandler(
    Filters.text, bots_command.number_phone_input)
input_description_handler = MessageHandler(
    Filters.text, bots_command.description_input)
conv_handler = ConversationHandler(entry_points=[import_handler],
                                   states={NAME: [input_name_handler],
                                           SURNAME: [input_surname_handler],
                                           PHONE: [input_phone_handler],
                                           DESCRIPTION: [input_description_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(export_handler)
dispatcher.add_handler(export_v1_handler)
dispatcher.add_handler(export_v2_handler)
dispatcher.add_handler(import_handler)

print('Server start')
updater.start_polling()
updater.idle()
