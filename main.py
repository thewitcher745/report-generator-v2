from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters, CallbackQueryHandler
from dotenv import dotenv_values

import handler_functions as handlers

bot_token = dotenv_values(".env.secret")["BOT_TOKEN"]

application = Application.builder().token(bot_token).build()

welcome_handler = CommandHandler('start', handlers.welcome)

manual_report_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(handlers.NormalReportConv.start, "manual"),
                  CommandHandler("manual", handlers.NormalReportConv.start)],
    states={
        handlers.NormalReportConv.SYMBOL: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.NormalReportConv.symbol)],
        handlers.NormalReportConv.TRADE_TYPE: [CallbackQueryHandler(handlers.NormalReportConv.trade_type)],
        handlers.NormalReportConv.ENTRY_PRICE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.NormalReportConv.entry_price)],
        handlers.NormalReportConv.EXIT_PRICE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.NormalReportConv.exit_price)],
    },
    fallbacks=[CommandHandler('cancel', handlers.cancel)]
)

automatic_report_handler = ConversationHandler(
    entry_points=[CallbackQueryHandler(handlers.AutomaticSignalConv.start, "automatic"),
                  MessageHandler(filters.FORWARDED & ~filters.COMMAND, handlers.AutomaticSignalConv.start_full_auto)],
    states={
        handlers.AutomaticSignalConv.EXCHANGE: [
            CallbackQueryHandler(handlers.AutomaticSignalConv.exchange)],
        handlers.AutomaticSignalConv.IMAGE: [
            CallbackQueryHandler(handlers.AutomaticSignalConv.image)
        ],
        handlers.AutomaticSignalConv.SIGNAL: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.AutomaticSignalConv.signal)
        ],
        handlers.AutomaticSignalConv.SAVED_SETUP: [
            CallbackQueryHandler(handlers.AutomaticSignalConv.saved_setup)
        ],
        handlers.AutomaticSignalConv.USERNAME: [
            MessageHandler(filters.TEXT, handlers.AutomaticSignalConv.username)
        ],
        handlers.AutomaticSignalConv.QR: [
            CallbackQueryHandler(handlers.AutomaticSignalConv.qr)
        ],
        handlers.AutomaticSignalConv.REF: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.AutomaticSignalConv.ref)
        ],
        handlers.AutomaticSignalConv.MARGIN: [
            MessageHandler(filters.TEXT, handlers.AutomaticSignalConv.margin)
        ],
        # handlers.AutomaticSignalConv.SELECT_TARGET: [
        #     MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.AutomaticSignalConv.select_target),
        #     CommandHandler('cancel', handlers.cancel)
        # ],
    },
    fallbacks=[CommandHandler('cancel', handlers.cancel)]
)

handler_objects = [welcome_handler, manual_report_handler, automatic_report_handler]

for handler in handler_objects:
    application.add_handler(handler)

application.run_polling(allowed_updates=Update.ALL_TYPES)
