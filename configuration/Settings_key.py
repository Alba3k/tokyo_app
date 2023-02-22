import ccxt

HUOBI_EXCHANGE = ccxt.huobi({
    'apiKey': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'options': {
        'defaultType': 'spot',
    },
})

TELEGRAM_TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
USER_ID_TELEGRAM = 'xxxxxxxxxxxxxxxx'