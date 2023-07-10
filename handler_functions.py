from telegram.ext import ConversationHandler

import keyboards
import utilities


async def welcome(update, context):
    await utilities.send_message(context, update, "🙏 Welcome. Choose an option below:", keyboard=keyboards.welcome)


async def cancel(update, context):
    await utilities.send_message(context, update, "❌ Operation canceled. Use /start to start over.")
    return ConversationHandler.END


class NormalReportConv:
    SYMBOL, TRADE_TYPE, ENTRY_PRICE, EXIT_PRICE = range(4)

    @staticmethod
    async def start(update, context):
        await update.callback_query.answer()
        await utilities.send_message(context, update, "❓ Please enter the symbol:", is_callback_query=True)

        return NormalReportConv.SYMBOL

    @staticmethod
    async def symbol(update, context):
        context.user_data["symbol"] = update.message.text

        await utilities.send_message(context, update, "❓ Now enter the type of the trade (Short/Long):",
                                     keyboards.signal_type)

        return NormalReportConv.TRADE_TYPE

    @staticmethod
    async def trade_type(update, context):
        query = update.callback_query
        await query.answer()
        context.user_data["trade_type"] = query.data

        await utilities.send_message(context, update, "❓ Now enter the entry price:", is_callback_query=True)

        return NormalReportConv.ENTRY_PRICE

    @staticmethod
    async def entry_price(update, context):
        context.user_data["entry_price"] = update.message.text

        await utilities.send_message(context, update, "❓ Now enter your exit price:")
        return NormalReportConv.EXIT_PRICE

    @staticmethod
    async def exit_price(update, context):
        context.user_data["exit_price"] = update.message.text

        await utilities.send_message(context, update, "🎉 Done. Generating image...")
        await utilities.send_message(context, update, f"{context.user_data['trade_type']}")

        return ConversationHandler.END


class AutomaticSignalConv:
    SIGNAL, SELECT_TARGET, CONFIRM = range(3)

    @staticmethod
    async def start(update, context):
        await update.callback_query.answer()
        await utilities.send_message(context, update, "❓ Please forward or copy a signal:", is_callback_query=True)

        return AutomaticSignalConv.SIGNAL

    @staticmethod
    async def signal(update, context):
        signal_text = update.message.text.lower()

        symbol = utilities.RegexPatterns.symbol(signal_text)
        signal_type = utilities.RegexPatterns.signal_type(signal_text)
        leverage = utilities.RegexPatterns.leverage(signal_text)
        entry = utilities.RegexPatterns.entry(signal_text)[0]
        targets = utilities.RegexPatterns.targets(signal_text)
        stop = utilities.RegexPatterns.stop(signal_text)[0]

        if not symbol:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find symbol. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        if not signal_type:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find signal type. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        if not leverage:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find leverage. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        if not entry:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find entry target. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        if not targets:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find targets. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        if not stop:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find stop targets. Check if signal was copied/forwarded correctly.")
            return ConversationHandler.END

        context.user_data["symbol"] = symbol
        context.user_data["signal_type"] = signal_type
        context.user_data["leverage"] = leverage
        context.user_data["entry"] = entry
        context.user_data["targets"] = targets
        context.user_data["stop"] = stop

        confirmation_message = f'''
💰 Symbol: {symbol}
💰 Type: {signal_type}
⬆️ Leverage: {leverage}
⏎ Entry: {entry}
☑️ Targets: {targets}
🚪 Stop: {stop}
        
If this information is correct, press "☑️ Confirm" below to start generating the image. 
Otherwise, use /cancel to end the process.
        '''

        await utilities.send_message(context, update, confirmation_message, keyboard=keyboards.confirm)

        return AutomaticSignalConv.CONFIRM

    # @staticmethod
    # async def select_target(update, context):
    #     target_hit = update.message.text
    #
    #     if not target_hit.isnumeric():
    #         message = "❌ The entered number is not valid. Try another input."
    #         await utilities.send_message(context, update, message)
    #         return AutomaticSignalConv.SELECT_TARGET
    #
    #     elif int(target_hit) > len(context.user_data["targets"]):
    #         message = "❌ The entered number doesn't correspond to a valid target. Try another input."
    #         await utilities.send_message(context, update, message)
    #         return AutomaticSignalConv.SELECT_TARGET
    #
    #     context.user_data["selected_target"] = context.user_data['targets'][int(target_hit) - 1]
    #     message = f"🆗 Target #{target_hit} was selected. It has a value of {context.user_data['selected_target']}\n"
    #     message += 'Press "☑️ Confirm" below to start generating the image.'
    #
    #     await utilities.send_message(context, update, message, keyboard=keyboards.confirm)
    #
    #     return AutomaticSignalConv.CONFIRM

    @staticmethod
    async def confirm_signal(update, context):
        await update.callback_query.answer()
        await utilities.send_message(context, update, "🎉 Done! Generating image...", is_callback_query=True)

        return ConversationHandler.END
