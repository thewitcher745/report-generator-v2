from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import utilities

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

binance_setups = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("Cryptolovers", callback_data="Cryptolovers"),
        InlineKeyboardButton("CAN 1", callback_data="CAN 1")],
    [
        InlineKeyboardButton("CAN 2", callback_data="CAN 2"),
        InlineKeyboardButton("Mentally", callback_data="Mentally"),
    ],
    [
        InlineKeyboardButton("Bbland", callback_data="Bbland"),
        InlineKeyboardButton("Paid", callback_data="Paid"),
    ],
    [
        InlineKeyboardButton("Turk", callback_data="Turk"),
    ],
    [
        InlineKeyboardButton("Custom...", callback_data="custom"),
    ],
])

bybit_setups = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ByBit QR1", callback_data="ByBit QR1"),
        InlineKeyboardButton("ByBit QR2", callback_data="ByBit QR2")],
    [
        InlineKeyboardButton("ByBit QR3", callback_data="ByBit QR3"),
        InlineKeyboardButton("ByBit QR4", callback_data="ByBit QR4"),
    ],
    [
        InlineKeyboardButton("Custom...", callback_data="custom"),
    ],
])
