import telebot

with open('secret.txt') as file:
    TOKEN = file.readline()

bot = telebot.TeleBot(TOKEN)


keys = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'биткоин': 'BTC',
    'эфириум': 'ETH',
}
