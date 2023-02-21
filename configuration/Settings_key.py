import ccxt

HUOBI_EXCHANGE = ccxt.huobi({
    'apiKey': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'secret': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'options': {
        'defaultType': 'spot',
    },
})