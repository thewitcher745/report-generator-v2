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

