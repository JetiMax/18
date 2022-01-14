import telebot
from telebot import TeleBot

TOKEN = "5055858253:AAEaDZmZ8s0cSjA46OB0cvqOveUS3H0v2EQ"
bot: TeleBot = telebot.TeleBot(TOKEN)

# keys = {
#     'биткоин': 'BTC',
#     'эфириум': 'ETH',
#     'доллар': 'USD',
# }
keys = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    }
