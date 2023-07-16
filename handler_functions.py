from telegram import InputMediaPhoto
from telegram.ext import ConversationHandler
from binance.client import Client

import image_generator
import keyboards
import utilities
import os

client = Client("", "")


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
    EXCHANGE, IMAGE, SIGNAL, TARGET, QR, REF = range(7)

    @staticmethod
    async def start(update, context):
        await update.callback_query.answer()
        context.user_data["full_auto_signal"] = False

        await utilities.send_message(context, update, "❓ Please select an exchange:", keyboard=keyboards.exchange,
                                     is_callback_query=True)

        return AutomaticSignalConv.EXCHANGE

    @staticmethod
    # This handler takes the forwarded/copied signal and processes it using RegEx using functions provided in utilities
    async def start_full_auto(update, context):
        signal_text = update.message.text.lower()
        context.user_data["full_auto_signal"] = True

        symbol = utilities.RegexPatterns.symbol(signal_text)
        signal_type = utilities.RegexPatterns.signal_type(signal_text)
        leverage = utilities.RegexPatterns.leverage(signal_text)
        entry = utilities.RegexPatterns.entry(signal_text)[0]
        targets = utilities.RegexPatterns.targets(signal_text)
        stop = utilities.RegexPatterns.stop(signal_text)[0]

        if not symbol:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find symbol. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not signal_type:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find signal type. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not leverage:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find leverage. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not entry:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find entry target. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not targets:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find targets. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not stop:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find stop target. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

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

    If the information is incorrect, use /cancel to end the process.
            '''
        await utilities.send_message(context, update, confirmation_message)
        await utilities.send_message(context, update, "❓ Please select an exchange:", keyboard=keyboards.exchange)

        return AutomaticSignalConv.EXCHANGE

    @staticmethod
    async def exchange(update, context):
        await update.callback_query.answer()
        context.user_data["exchange"] = update.callback_query.data

        exchange = context.user_data["exchange"]
        media_group = [InputMediaPhoto(open(f"./background_images/{exchange}_images.png", 'rb'))]
        await context.bot.send_media_group(chat_id=update.callback_query.message.chat.id, media=media_group)
        if exchange == "bybit":
            await utilities.send_message(context, update, "❓ Please select an image:",
                                         keyboard=keyboards.image_bybit, is_callback_query=True)
        elif exchange == "binance":
            await utilities.send_message(context, update, "❓ Please select an image:",
                                         keyboard=keyboards.image_binance, is_callback_query=True)

        return AutomaticSignalConv.IMAGE

    @staticmethod
    async def image(update, context):
        await update.callback_query.answer()
        context.user_data["image_id"] = update.callback_query.data

        if context.user_data["full_auto_signal"]:
            keyboard = keyboards.qr_bybit
            if context.user_data["exchange"] == "binance":
                keyboard = keyboards.qr_binance
            qr_message = "❓ Select a QR code from below: "
            await utilities.send_message(context, update, qr_message, keyboard=keyboard, is_callback_query=True)

            return AutomaticSignalConv.QR
        else:
            await utilities.send_message(context, update, "❓ Please forward or copy a signal:", is_callback_query=True)
            return AutomaticSignalConv.SIGNAL

    @staticmethod
    # This handler takes the forwarded/copied signal and processes it using RegEx using functions provided in utilities
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
                                         "❌ Couldn't find symbol. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not signal_type:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find signal type. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not leverage:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find leverage. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not entry:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find entry target. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not targets:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find targets. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

        if not stop:
            await utilities.send_message(context, update,
                                         "❌ Couldn't find stop target. Check if signal was copied/forwarded " +
                                         "correctly and send it again or use /cancel to cancel the operation.")
            return AutomaticSignalConv.SIGNAL

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
        
If the information is incorrect, use /cancel to end the process.
        '''
        await utilities.send_message(context, update, confirmation_message)

        keyboard = keyboards.qr_bybit
        if context.user_data["exchange"] == "binance":
            keyboard = keyboards.qr_binance

        qr_message = "❓ Select a QR code from below: "
        await utilities.send_message(context, update, qr_message, keyboard=keyboard)

        return AutomaticSignalConv.QR

    @staticmethod
    async def qr(update, context):
        await update.callback_query.answer()
        context.user_data["qr"] = update.callback_query.data
        await utilities.send_message(context, update, "❓ Please type a referral code:", is_callback_query=True)

        return AutomaticSignalConv.REF

    @staticmethod
    async def ref(update, context):
        context.user_data["ref"] = update.message.text
        await utilities.send_message(context, update, "🎉 Confirmed! Generating image...")

        # Clear the /images subdirectory
        for filename in os.listdir("./images"):
            os.remove("./images/" + filename)

        image_id = context.user_data["image_id"]
        symbol = context.user_data["symbol"]
        signal_type = context.user_data["signal_type"].capitalize()
        leverage = context.user_data["leverage"].upper()
        if context.user_data["exchange"] == "binance":
            context.user_data["leverage"].lower()

        stripped_symbol = symbol.replace(" ", "").replace("Perpetual", "").replace("/", "")
        try:
            symbol_precision = utilities.get_pair_precision(stripped_symbol, context.user_data["exchange"])
            if symbol_precision == 0:
                error_message = "❌ The selected exchange doesn't support the given symbol. Please try another exchange."
                await utilities.send_message(context, update, error_message)
                return ConversationHandler.END

            entry = "{:.{}f}".format(float(context.user_data["entry"]), symbol_precision)
            targets = [utilities.separate_number("{:.{}f}".format(float(target), symbol_precision)) for target in
                       context.user_data["targets"]]
        except KeyError:
            entry = context.user_data["entry"]
            targets = context.user_data["targets"]

        qr = context.user_data["qr"]
        ref = context.user_data["ref"]

        media_group = []
        for target_id, target in enumerate(targets):
            deficit = abs(float(target) - float(entry))
            roi = deficit / float(entry) * 100 * float(leverage) if signal_type == "long" else deficit / float(
                target) * 100 * float(leverage)
            roi = f"+{str(round(roi, 2))}%"
            image_generator.generate_image(image_id, symbol, signal_type, f"{leverage}x", roi, entry, target, qr, ref,
                                           f"{image_id}_{target_id}")

            media_group.append(InputMediaPhoto(open(f"./images/{image_id}_{target_id}.png", 'rb')))

        await context.bot.send_media_group(chat_id=update.callback_query.message.chat.id, media=media_group)
        await utilities.send_message(context, update, "🎉 All done! use /start to generate another image.")
        return ConversationHandler.END

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

