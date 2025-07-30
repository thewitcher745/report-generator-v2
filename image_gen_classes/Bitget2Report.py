from PIL import ImageFont
import datetime

from image_gen_classes.BitgetReport import BitgetReport
from image_gen_classes.utils import get_text_width, two_char_long


class Bitget2Report(BitgetReport):
    def draw_symbol(self, symbol):
        pass

    def draw_details(
        self, signal_type, leverage, gen_date: datetime.datetime, username, symbol
    ):
        self.draw_symbol_signal_type(symbol, signal_type)

        self.draw_datetime(gen_date)

        self.draw_username(username)

    def draw_symbol_signal_type(self, symbol, signal_type):
        """
        Draw symbol and signal type on the image, in the format SYMBOL SignalType | Cross

        Args:
            symbol (str): The symbol of the trade
            signal_type (str): The type of the trade (Long/Short)
        """
        signal_type = signal_type.capitalize()
        symbol = symbol.replace("Perpetual", "")

        symbol_styling = self.styling["symbol"]
        signal_type_styling = self.styling["signal_type"]

        spacing = 14

        signal_type_color = (
            signal_type_styling.long_color
            if signal_type.lower() == "long"
            else signal_type_styling.short_color
        )

        symbol_font = ImageFont.truetype(symbol_styling.font, symbol_styling.font_size)

        xy = (
            symbol_styling.position.x * self.image.size[0],
            symbol_styling.position.y * self.image.size[1],
        )
        self.draw.text(xy, symbol, font=symbol_font, fill=symbol_styling.color)

        signal_type_font = ImageFont.truetype(
            signal_type_styling.font, signal_type_styling.font_size
        )

        xy = (
            symbol_styling.position.x * self.image.size[0]
            + get_text_width(symbol, symbol_font)
            + spacing,
            symbol_styling.position.y * self.image.size[1],
        )
        self.draw.text(xy, signal_type, font=signal_type_font, fill=signal_type_color)

        # Draw the | Cross at the end
        cross_font = ImageFont.truetype(
            signal_type_styling.font, signal_type_styling.font_size
        )

        xy = (
            symbol_styling.position.x * self.image.size[0]
            + get_text_width(symbol, symbol_font)
            + spacing
            + get_text_width(signal_type, signal_type_font),
            symbol_styling.position.y * self.image.size[1],
        )
        self.draw.text(xy, "   |  Cross", font=cross_font, fill=symbol_styling.color)

    def draw_roi(self, roi):
        roi = f"+{roi.replace('%', '').replace('+', '')}"

        roi_styling = self.styling["roi"]
        font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
        xy = (
            roi_styling.position.x * self.image.size[0],
            roi_styling.position.y * self.image.size[1],
        )

        self.draw.text(xy, roi, font=font, fill=roi_styling.color)

    def draw_username(self, username):
        username_styling = self.styling["username"]

        font = ImageFont.truetype(username_styling.font, username_styling.font_size)

        xy = (
            username_styling.position.x * self.image.size[0],
            username_styling.position.y * self.image.size[1],
        )
        self.draw.text(xy, username, font=font, fill=username_styling.color)

        try:
            username_id_styling = self.styling["username_id"]
            username_id = f"@{username}"

            font = ImageFont.truetype(
                username_id_styling.font, username_id_styling.font_size
            )

            xy = (
                username_id_styling.position.x * self.image.size[0],
                username_id_styling.position.y * self.image.size[1],
            )

            self.draw.text(xy, username_id, font=font, fill=username_id_styling.color)
        except KeyError:
            pass
