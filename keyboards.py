from telegram import InlineKeyboardButton, InlineKeyboardMarkup

welcome = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🤚 Manual signal", callback_data="manual"),
        InlineKeyboardButton("💻 Automatic signal", callback_data="automatic"),
    ],
])

signal_type = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🔴 Short", callback_data="short"),
        InlineKeyboardButton("🟢 Long", callback_data="long"),
    ],
])

confirm = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("☑️ Confirm", callback_data="confirm"),
    ],
])

exchange = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ByBit", callback_data="bybit"),
        InlineKeyboardButton("Binance", callback_data="binance"),
    ],
])

image_bybit = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ByBit 1", callback_data="bybit_1"),
        InlineKeyboardButton("ByBit 2", callback_data="bybit_2"),
        InlineKeyboardButton("ByBit 3", callback_data="bybit_3"),
    ],
])

image_binance = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Binance 1", callback_data="binance_1"),
        InlineKeyboardButton("Binance 2", callback_data="binance_2"),
    ],
    [
        InlineKeyboardButton("Binance 3", callback_data="binance_3"),
    ]
])

qr_bybit = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("QR 1", callback_data="bybit_1"),
        InlineKeyboardButton("QR 2", callback_data="bybit_2"),
        InlineKeyboardButton("QR 3", callback_data="bybit_3")],
    [
        InlineKeyboardButton("QR 4", callback_data="bybit_4"),
        InlineKeyboardButton("QR 5", callback_data="bybit_5"),
    ],
])

qr_binance = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("QR 1", callback_data="binance_1"),
        InlineKeyboardButton("QR 2", callback_data="binance_2"),
        InlineKeyboardButton("QR 3", callback_data="binance_3")],
    [
        InlineKeyboardButton("QR 4", callback_data="binance_4"),
        InlineKeyboardButton("QR 5", callback_data="binance_5"),
        InlineKeyboardButton("QR 5", callback_data="binance_6"),
    ],
])
