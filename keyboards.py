from telegram import InlineKeyboardButton, InlineKeyboardMarkup

welcome = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🤚 Manual signal", callback_data="manual"),
            InlineKeyboardButton("💻 Automatic signal", callback_data="automatic"),
        ],
    ]
)

signal_type = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔴 Short", callback_data="short"),
            InlineKeyboardButton("🟢 Long", callback_data="long"),
        ],
    ]
)

confirm = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("☑️ Confirm", callback_data="confirm"),
        ],
    ]
)

exchange = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("ByBit", callback_data="bybit"),
            InlineKeyboardButton("Binance", callback_data="binance"),
        ],
        [
            InlineKeyboardButton("BitGet", callback_data="bitget"),
            InlineKeyboardButton("MEXC", callback_data="mexc"),
        ],
        [
            InlineKeyboardButton("BingX", callback_data="bingx"),
            # InlineKeyboardButton("OKX", callback_data="okx"),
        ],
        [
            InlineKeyboardButton("LBANK", callback_data="lbank"),
        ],
    ]
)

image_binance = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Binance 1", callback_data="binance_1"),
            InlineKeyboardButton("Binance 2", callback_data="binance_2"),
        ],
        [
            InlineKeyboardButton("Binance 3", callback_data="binance_3"),
            InlineKeyboardButton("Binance 4", callback_data="binance_4"),
        ],
        [
            InlineKeyboardButton("Binance 5", callback_data="binance_5"),
            InlineKeyboardButton("Binance 6", callback_data="binance_6"),
        ],
        [
            InlineKeyboardButton("Binance 7", callback_data="binance_7"),
            InlineKeyboardButton("Binance 8", callback_data="binance_8"),
        ],
    ]
)

image_bybit = InlineKeyboardMarkup(
    [
        # [
        #     InlineKeyboardButton("ByBit 1", callback_data="bybit_1"),
        #     InlineKeyboardButton("ByBit 2", callback_data="bybit_2"),
        #     InlineKeyboardButton("ByBit 3", callback_data="bybit_3"),
        # ],
        [
            InlineKeyboardButton("ByBit 4", callback_data="bybit_4"),
            InlineKeyboardButton("ByBit 5", callback_data="bybit_5"),
        ]
    ]
)

image_bitget = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Bitget 1", callback_data="bitget_1"),
            InlineKeyboardButton("Bitget 2", callback_data="bitget_2"),
        ],
    ]
)

image_mexc = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("MEXC 2", callback_data="mexc_4"),
            InlineKeyboardButton("MEXC 3", callback_data="mexc_5"),
            InlineKeyboardButton("MEXC 4", callback_data="mexc_6"),
        ],
    ]
)

image_bingx = InlineKeyboardMarkup(
    [
        [
            # InlineKeyboardButton("BingX 1", callback_data="bingx_3"),
            # InlineKeyboardButton("BingX 1 - CAN", callback_data="bingx_1"),
        ],
        [
            # InlineKeyboardButton("BingX 1 - Ashan", callback_data="bingx_2"),
        ],
        [
            InlineKeyboardButton("BingX 2", callback_data="bingx_5"),
            InlineKeyboardButton("BingX 2 - CAN", callback_data="bingx_4"),
        ],
        [
            InlineKeyboardButton("BingX 2 - Ashan", callback_data="bingx_6"),
        ],
        [
            InlineKeyboardButton("BingX 3", callback_data="bingx_9"),
            InlineKeyboardButton("BingX 3 - CAN", callback_data="bingx_7"),
        ],
        [
            InlineKeyboardButton("BingX 3 - Board", callback_data="bingx_8"),
        ],
    ]
)

image_okx = InlineKeyboardMarkup(
    [[InlineKeyboardButton("OKX 1", callback_data="okx_1")]]
)

image_lbank = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("LBANK 1", callback_data="lbank_1"),
            InlineKeyboardButton("LBANK 2", callback_data="lbank_2"),
        ]
    ]
)

qr_binance = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="binance_1"),
            InlineKeyboardButton("QR 2", callback_data="binance_2"),
            InlineKeyboardButton("QR 3", callback_data="binance_3"),
        ],
        [
            InlineKeyboardButton("QR 4", callback_data="binance_4"),
            InlineKeyboardButton("QR 5", callback_data="binance_5"),
            InlineKeyboardButton("QR 5", callback_data="binance_6"),
        ],
    ]
)

qr_bybit = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="bybit_1"),
        ],
    ]
)

qr_bitget = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="bitget_1"),
        ]
    ]
)

qr_bitget = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="bitget_1"),
            InlineKeyboardButton("QR 2", callback_data="bitget_2"),
            InlineKeyboardButton("QR 3", callback_data="bitget_3"),
        ],
        [
            InlineKeyboardButton("QR 4", callback_data="bitget_4"),
            InlineKeyboardButton("QR 5", callback_data="bitget_5"),
        ],
    ]
)

qr_mexc = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="mexc_1"),
            InlineKeyboardButton("QR 2", callback_data="mexc_2"),
            InlineKeyboardButton("QR 3", callback_data="mexc_3"),
        ],
        [
            InlineKeyboardButton("QR 4", callback_data="mexc_4"),
            InlineKeyboardButton("QR 5", callback_data="mexc_5"),
        ],
    ]
)

qr_okx = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="okx_1"),
        ]
    ]
)

qr_okx = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("QR 1", callback_data="lbank_1"),
        ]
    ]
)

binance_setups = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Board Main", callback_data="Board Main"),
            InlineKeyboardButton("Board Free", callback_data="Board Free"),
        ],
        [
            InlineKeyboardButton("CAN Main", callback_data="CAN Main"),
            InlineKeyboardButton("CAN Free", callback_data="CAN Free"),
        ],
        [
            InlineKeyboardButton("Turk Free", callback_data="Turk Free"),
            InlineKeyboardButton("Turk Main", callback_data="Turk Main"),
        ],
        [
            InlineKeyboardButton("Extra 1", callback_data="Extra 1"),
            InlineKeyboardButton("Extra 2", callback_data="Extra 2"),
        ],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

bybit_setups = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("CAN Main", callback_data="CAN Main"),
            InlineKeyboardButton("CAN Free", callback_data="CAN Free"),
        ],
        [
            InlineKeyboardButton("Turk Main", callback_data="Turk Main"),
            InlineKeyboardButton("Turk Free", callback_data="Turk Free"),
        ],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

bitget_setups = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("CAN Main", callback_data="CAN Main"),
            InlineKeyboardButton("CAN Free", callback_data="CAN Free"),
        ],
        [
            InlineKeyboardButton("Turk Main", callback_data="Turk Main"),
            InlineKeyboardButton("Turk Free", callback_data="Turk Free"),
        ],
        [
            InlineKeyboardButton("Board Main", callback_data="Board Main"),
            InlineKeyboardButton("Board Free", callback_data="Board Free"),
        ],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

mexc_setups = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Board Main", callback_data="Board Main"),
            InlineKeyboardButton("Board Free", callback_data="Board Free"),
        ],
        [
            InlineKeyboardButton("CAN Main", callback_data="CAN Main"),
            InlineKeyboardButton("CAN Free", callback_data="CAN Free"),
        ],
        [
            InlineKeyboardButton("Turk Main", callback_data="Turk Main"),
            InlineKeyboardButton("Turk Free", callback_data="Turk Free"),
        ],
        [
            InlineKeyboardButton("Extra 1", callback_data="Extra 1"),
        ],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

bingx_setups = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("CAN Main", callback_data="CAN Main")],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

okx_setups = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("CAN Main", callback_data="CAN Main")],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)

lbank_setups = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("CAN Main", callback_data="CAN Main"),
            InlineKeyboardButton("CAN Free", callback_data="CAN Free"),
        ],
        [
            InlineKeyboardButton("Turk Main", callback_data="Turk Main"),
            InlineKeyboardButton("Turk Free", callback_data="Turk Free"),
        ],
        [
            InlineKeyboardButton("Board Main", callback_data="Board Main"),
            InlineKeyboardButton("Board Free", callback_data="Board Free"),
        ],
        [
            InlineKeyboardButton("Custom...", callback_data="custom"),
            InlineKeyboardButton("Random...", callback_data="random"),
        ],
    ]
)
