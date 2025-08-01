from telegram import InputMediaPhoto
from telegram.ext import ConversationHandler

import image_generator
import keyboards
import utilities
import os
import datetime

from styling_dict import styling_dict


async def welcome(update, context):
    await utilities.send_message(
        context,
        update,
        "🙏 Welcome. Choose an option below:",
        keyboard=keyboards.welcome,
    )


async def cancel(update, context):
    await utilities.send_message(
        context, update, "❌ Operation canceled. Use /start to start over."
    )
    return ConversationHandler.END


class NormalReportConv:
    SYMBOL, TRADE_TYPE, ENTRY_PRICE, EXIT_PRICE = range(4)

    @staticmethod
    async def start(update, context):
        await update.callback_query.answer()
        await utilities.send_message(
            context, update, "❓ Please enter the symbol:", is_callback_query=True
        )

        return NormalReportConv.SYMBOL

    @staticmethod
    async def symbol(update, context):
        context.user_data["symbol"] = update.message.text

        await utilities.send_message(
            context,
            update,
            "❓ Now enter the type of the trade (Short/Long):",
            keyboards.signal_type,
        )

        return NormalReportConv.TRADE_TYPE

    @staticmethod
    async def trade_type(update, context):
        query = update.callback_query
        await query.answer()
        context.user_data["trade_type"] = query.data

        await utilities.send_message(
            context, update, "❓ Now enter the entry price:", is_callback_query=True
        )

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
        await utilities.send_message(
            context, update, f"{context.user_data['trade_type']}"
        )

        return ConversationHandler.END


class AutomaticSignalConv:
    EXCHANGE, SAVED_SETUP, USERNAME, IMAGE, SIGNAL, TARGET, QR, REF, MARGIN = range(9)

    @staticmethod
    async def start(update, context):
        await update.callback_query.answer()
        context.user_data["full_auto_signal"] = False

        await utilities.send_message(
            context,
            update,
            "❓ Please select an exchange:",
            keyboard=keyboards.exchange,
            is_callback_query=True,
        )

        return AutomaticSignalConv.EXCHANGE

    @staticmethod
    # This handler takes the forwarded/copied signal and processes it using RegEx using functions provided in utilities
    async def start_full_auto(update, context):
        signal_text = update.message.text.lower()
        context.user_data["full_auto_signal"] = True

        symbol = utilities.RegexPatterns.Regular.symbol(signal_text)
        signal_type = utilities.RegexPatterns.Regular.signal_type(signal_text)
        leverage = utilities.RegexPatterns.Regular.leverage(signal_text)
        entry = utilities.RegexPatterns.Regular.entry(signal_text)[0]
        targets = utilities.RegexPatterns.Regular.targets(signal_text)
        stop = utilities.RegexPatterns.Regular.stop(signal_text)[0]

        if not symbol:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find symbol. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not signal_type:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find signal type. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not leverage:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find leverage. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not entry:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find entry target. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not targets:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find targets. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not stop:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find stop target. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        context.user_data["symbol"] = symbol
        context.user_data["signal_type"] = signal_type
        context.user_data["leverage"] = leverage
        context.user_data["entry"] = entry
        context.user_data["targets"] = targets
        context.user_data["stop"] = stop

        confirmation_message = f"""
    💰 Symbol: {symbol}
    💰 Type: {signal_type}
    ⬆️ Leverage: {leverage}
    ⏎ Entry: {entry}
    ☑️ Targets: {targets}
    🚪 Stop: {stop}

    If the information is incorrect, use /cancel to end the process.
            """
        await utilities.send_message(context, update, confirmation_message)
        await utilities.send_message(
            context,
            update,
            "❓ Please select an exchange:",
            keyboard=keyboards.exchange,
        )

        return AutomaticSignalConv.EXCHANGE

    @staticmethod
    async def exchange(update, context):
        await update.callback_query.answer()
        context.user_data["exchange"] = update.callback_query.data

        exchange = context.user_data["exchange"]
        symbol = context.user_data["symbol"]
        stripped_symbol = (
            symbol.replace(" ", "").replace("Perpetual", "").replace("/", "")
        )
        try:
            symbol_precision = utilities.get_pair_precision(
                stripped_symbol, context.user_data["exchange"]
            )

            if symbol_precision is None:
                error_message = "❌ The selected coin hasn't been listed. Will use the default signal precision."
                await utilities.send_message(
                    context, update, error_message, is_callback_query=True
                )
        except KeyError:
            error_message = "❌ The selected coin hasn't been listed. Will use the default signal precision."
            await utilities.send_message(
                context, update, error_message, is_callback_query=True
            )

        media_group = [
            InputMediaPhoto(open(f"./background_images/{exchange}_images.png", "rb"))
        ]
        await context.bot.send_media_group(
            chat_id=update.callback_query.message.chat.id, media=media_group
        )
        if exchange == "bybit":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_bybit,
                is_callback_query=True,
            )
        elif exchange == "binance":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_binance,
                is_callback_query=True,
            )
        elif exchange == "bitget":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_bitget,
                is_callback_query=True,
            )
        elif exchange == "mexc":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_mexc,
                is_callback_query=True,
            )

        elif exchange == "bingx":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_bingx,
                is_callback_query=True,
            )

        elif exchange == "okx":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_okx,
                is_callback_query=True,
            )

        elif exchange == "lbank":
            await utilities.send_message(
                context,
                update,
                "❓ Please select an image:",
                keyboard=keyboards.image_lbank,
                is_callback_query=True,
            )

        return AutomaticSignalConv.IMAGE

    @staticmethod
    async def image(update, context):
        await update.callback_query.answer()
        context.user_data["image_id"] = update.callback_query.data

        if context.user_data["full_auto_signal"]:
            keyboard = keyboards.bybit_setups
            if context.user_data["exchange"] == "binance":
                keyboard = keyboards.binance_setups
            elif context.user_data["exchange"] == "bitget":
                keyboard = keyboards.bitget_setups
            elif context.user_data["exchange"] == "mexc":
                keyboard = keyboards.mexc_setups
            elif context.user_data["exchange"] == "bingx":
                keyboard = keyboards.bingx_setups
            elif context.user_data["exchange"] == "okx":
                keyboard = keyboards.okx_setups

            setup_message = "❓ Select a saved setup below, press custom to enter your own referral info, or random for a randomized QR/Referral:"
            await utilities.send_message(
                context,
                update,
                setup_message,
                keyboard=keyboard,
                is_callback_query=True,
            )

            return AutomaticSignalConv.SAVED_SETUP
        else:
            await utilities.send_message(
                context,
                update,
                "❓ Please forward or copy a signal:",
                is_callback_query=True,
            )
            return AutomaticSignalConv.SIGNAL

    @staticmethod
    async def saved_setup(update, context):
        exchange = context.user_data["exchange"]
        await update.callback_query.answer()

        # If user asks to type the qr and referral
        if update.callback_query.data == "custom":
            qr_message = "❓ Please select a QR code from below: "
            keyboard = keyboards.qr_bybit
            if exchange == "binance":
                keyboard = keyboards.qr_binance
            elif exchange == "bitget":
                keyboard = keyboards.qr_bitget
            elif exchange == "okx":
                keyboard = keyboards.qr_okx

            await utilities.send_message(
                context, update, qr_message, keyboard=keyboard, is_callback_query=True
            )
            return AutomaticSignalConv.QR

        # If randomized data is requested
        elif update.callback_query.data == "random":
            context.user_data["ref"] = utilities.random_referral(
                context.user_data["exchange"]
            )
            context.user_data["qr"] = utilities.random_qr(context.user_data["exchange"])

            random_setup_message = f"Random setup selected: \nReferral code: {context.user_data['qr']}\n{context.user_data['qr']}"
            if context.user_data["image_id"] not in ["bitget_2", "bitget_4", "bybit_5"]:
                await utilities.send_message(
                    context, update, random_setup_message, is_callback_query=True
                )
                await utilities.send_message(
                    context,
                    update,
                    "🎉 Confirmed! Generating image...",
                    is_callback_query=True,
                )

                media_group = await AutomaticSignalConv.generate_images(context, update)

                for media in media_group:
                    await context.bot.send_media_group(
                        chat_id=update.callback_query.message.chat.id, media=[media]
                    )
                await utilities.send_message(
                    context,
                    update,
                    "🎉 All done! use /start to generate another image.",
                    is_callback_query=True,
                )

            elif context.user_data["image_id"] == "bybit_5":
                # Since bybit_5 prints the margin instead of the ROI
                await utilities.send_message(
                    context,
                    update,
                    "❓ Setup selected. Type a margin as the image needs a margin...",
                    is_callback_query=True,
                )

                return AutomaticSignalConv.MARGIN

            else:
                await utilities.send_message(
                    context,
                    update,
                    "❓ Setup selected. Type a username as the image needs a username...",
                    is_callback_query=True,
                )

                return AutomaticSignalConv.USERNAME

        # If a preset setup is selected
        else:
            setup = update.callback_query.data
            context.user_data["saved_setup"] = setup
            context.user_data["qr"] = utilities.saved_setups[exchange][setup]["qr"]
            context.user_data["ref"] = utilities.saved_setups[exchange][setup][
                "referral"
            ]
            # If the setup contains a username, add it to user_data
            if "username" in utilities.saved_setups[exchange][setup].keys():
                context.user_data["username"] = utilities.saved_setups[exchange][setup][
                    "username"
                ]

            if context.user_data["image_id"] not in [
                "bitget_2",
                "bitget_4",
                "bybit_5",
                "bitget_2",
            ]:
                await utilities.send_message(
                    context,
                    update,
                    "🎉 Confirmed! Generating image...",
                    is_callback_query=True,
                )

                media_group = await AutomaticSignalConv.generate_images(context, update)

                for media in media_group:
                    await context.bot.send_media_group(
                        chat_id=update.callback_query.message.chat.id, media=[media]
                    )
                await utilities.send_message(
                    context,
                    update,
                    "🎉 All done! use /start to generate another image.",
                    is_callback_query=True,
                )

            elif context.user_data["image_id"] in [
                "binance_6",
                "binance_7",
                "binance_8",
            ]:
                await utilities.send_message(
                    context,
                    update,
                    "🎉 Confirmed! Generating image...",
                    is_callback_query=True,
                )

                media_group = await AutomaticSignalConv.generate_images(context, update)

                for media in media_group:
                    await context.bot.send_media_group(
                        chat_id=update.callback_query.message.chat.id, media=[media]
                    )
                await utilities.send_message(
                    context,
                    update,
                    "🎉 All done! use /start to generate another image.",
                    is_callback_query=True,
                )

            elif context.user_data["image_id"] in ["bybit_5", "bitget_2"]:
                # Since bybit_5 prints the margin instead of the ROI
                await utilities.send_message(
                    context,
                    update,
                    "❓ Setup selected. Type a margin as the image needs a margin...",
                    is_callback_query=True,
                )

                return AutomaticSignalConv.MARGIN

            else:
                await utilities.send_message(
                    context,
                    update,
                    "❓ Setup selected. Type a username as the image needs a username...",
                    is_callback_query=True,
                )

                return AutomaticSignalConv.USERNAME

            return ConversationHandler.END

    @staticmethod
    async def username(update, context):
        if context.user_data["image_id"] not in [
            "bitget_2",
            "bitget_4",
            "binance_6",
            "binance_7",
            "binance_8",
        ]:
            context.user_data["username"] = update.message.text

        await utilities.send_message(
            context, update, "🎉 Confirmed! Generating image..."
        )

        media_group = await AutomaticSignalConv.generate_images(context, update)

        for media in media_group:
            await context.bot.send_media_group(
                chat_id=update.message.chat.id, media=[media]
            )

        await utilities.send_message(
            context, update, "🎉 All done! use /start to generate another image."
        )

        return ConversationHandler.END

    @staticmethod
    # This handler takes the forwarded/copied signal and processes it using RegEx using functions provided in utilities
    async def signal(update, context):
        signal_text = update.message.text.lower()

        symbol = utilities.RegexPatterns.Regular.symbol(signal_text)
        signal_type = utilities.RegexPatterns.Regular.signal_type(signal_text)
        leverage = utilities.RegexPatterns.Regular.leverage(signal_text)
        entry = utilities.RegexPatterns.Regular.entry(signal_text)[0]
        targets = utilities.RegexPatterns.Regular.targets(signal_text)
        stop = utilities.RegexPatterns.Regular.stop(signal_text)[0]

        if not symbol:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find symbol. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not signal_type:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find signal type. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not leverage:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find leverage. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not entry:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find entry target. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not targets:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find targets. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        if not stop:
            await utilities.send_message(
                context,
                update,
                "❌ Couldn't find stop target. Check if signal was copied/forwarded "
                + "correctly and send it again or use /cancel to cancel the operation.",
            )
            return AutomaticSignalConv.SIGNAL

        context.user_data["symbol"] = symbol
        context.user_data["signal_type"] = signal_type
        context.user_data["leverage"] = leverage
        context.user_data["entry"] = entry
        context.user_data["targets"] = targets
        context.user_data["stop"] = stop

        confirmation_message = f"""
💰 Symbol: {symbol}
💰 Type: {signal_type}
⬆️ Leverage: {leverage}
⏎ Entry: {entry}
☑️ Targets: {targets}
🚪 Stop: {stop}
        
If the information is incorrect, use /cancel to end the process.
        """
        await utilities.send_message(context, update, confirmation_message)

        keyboard = keyboards.qr_bybit
        if context.user_data["exchange"] == "binance":
            keyboard = keyboards.qr_binance
        elif context.user_data["exchange"] == "bitget":
            keyboard = keyboards.qr_bitget
        elif context.user_data["exchange"] == "okx":
            keyboard = keyboards.qr_okx

        qr_message = "❓ Select a QR code from below: "
        await utilities.send_message(context, update, qr_message, keyboard=keyboard)

        return AutomaticSignalConv.QR

    @staticmethod
    async def qr(update, context):
        await update.callback_query.answer()
        context.user_data["qr"] = update.callback_query.data
        await utilities.send_message(
            context, update, "❓ Please type a referral code:", is_callback_query=True
        )

        return AutomaticSignalConv.REF

    @staticmethod
    async def ref(update, context):
        context.user_data["ref"] = update.message.text

        # Skip to username for images that need a username
        if context.user_data["image_id"] not in [
            "bitget_2",
            "bitget_4",
            "bybit_5",
            "bitget_2",
        ]:
            await utilities.send_message(
                context, update, "🎉 Confirmed! Generating image..."
            )

            media_group = await AutomaticSignalConv.generate_images(context, update)

            for media in media_group:
                await context.bot.send_media_group(
                    chat_id=update.message.chat.id, media=[media]
                )

            await utilities.send_message(
                context, update, "🎉 All done! use /start to generate another image."
            )

            return ConversationHandler.END

        elif context.user_data["image_id"] in ["bybit_5", "bitget_2"]:
            # Since bybit_5 and bitget_2 print the margin instead of the ROI
            await utilities.send_message(
                context,
                update,
                "❓ Referral set. Type a margin as the image needs a margin...",
                is_callback_query=True,
            )

            return AutomaticSignalConv.MARGIN

        else:
            await utilities.send_message(
                context,
                update,
                "❓ Referral set. Type a username as the image needs a username...",
            )

            return AutomaticSignalConv.USERNAME

    @staticmethod
    async def margin(update, context):
        context.user_data["margin"] = update.message.text

        await utilities.send_message(
            context, update, "🎉 Confirmed! Generating image..."
        )

        media_group = await AutomaticSignalConv.generate_images(context, update)

        for media in media_group:
            await context.bot.send_media_group(
                chat_id=update.message.chat.id, media=[media]
            )

        await utilities.send_message(
            context, update, "🎉 All done! use /start to generate another image."
        )

        return ConversationHandler.END

    @staticmethod
    async def generate_images(context, update):
        # Clear the /images subdirectory
        for filename in os.listdir("./images"):
            os.remove("./images/" + filename)

        image_name = context.user_data["image_id"] + ".png"
        image_id = image_name.split(".")[0]
        symbol = context.user_data["symbol"]
        signal_type = context.user_data["signal_type"].capitalize()
        leverage = context.user_data["leverage"]

        if "username" in context.user_data.keys():
            username = context.user_data["username"]
        else:
            username = ""

        stripped_symbol = (
            symbol.replace(" ", "").replace("Perpetual", "").replace("/", "")
        )
        try:
            symbol_precision = utilities.get_pair_precision(
                stripped_symbol, context.user_data["exchange"]
            )
            if symbol_precision is not None:
                message = f"The selected coin has a precision of {symbol_precision}"
                try:
                    await utilities.send_message(
                        context, update, message, is_callback_query=True
                    )
                except:
                    await utilities.send_message(
                        context, update, message, is_callback_query=False
                    )

                entry = "{:.{}f}".format(
                    float(context.user_data["entry"]), symbol_precision
                )
                targets = [
                    "{:.{}f}".format(float(target), symbol_precision)
                    for target in context.user_data["targets"]
                ]
            else:
                error_message = "❌ The selected coin hasn't been listed. Will use the default signal precision."
                try:
                    await utilities.send_message(
                        context, update, error_message, is_callback_query=True
                    )
                except:
                    await utilities.send_message(
                        context, update, error_message, is_callback_query=False
                    )

                entry = str(context.user_data["entry"])
                targets = [
                    str(float(target)) for target in context.user_data["targets"]
                ]

        except KeyError:
            entry = str(context.user_data["entry"])
            targets = [str(float(target)) for target in context.user_data["targets"]]

        qr = context.user_data["qr"]
        ref = context.user_data["ref"]

        media_group = []
        used_money = 10

        if context.user_data["image_id"] == "bybit_5":
            used_money = float(context.user_data["margin"])

        qty = (
            used_money
            * float(context.user_data["leverage"])
            / float(context.user_data["entry"])
        )
        for target_id, target in enumerate(targets):
            if signal_type.lower() == "long":
                loss = float(context.user_data["entry"]) * qty
                gain = float(target) * qty
            else:
                loss = float(target) * qty
                gain = float(context.user_data["entry"]) * qty

            net_profit = gain - loss
            roi = net_profit / used_money * 100
            roi = f"+{str(round(roi, 2))}%"

            if context.user_data["image_id"] in ["bybit_5", "bitget_2"]:
                roi = f"+{str(round(net_profit, 2))}"

            image_generator.generate_image(
                image_name,
                symbol,
                signal_type,
                f"{leverage}x",
                roi,
                utilities.separate_number(entry),
                utilities.separate_number(target),
                qr,
                ref,
                f"{image_id}_{target_id}",
                gen_date=datetime.datetime.now(),
                username=username,
            )

            media_group.append(
                InputMediaPhoto(open(f"./images/{image_id}_{target_id}.png", "rb"))
            )

        return media_group

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
