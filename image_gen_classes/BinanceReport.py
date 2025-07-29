from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from styling_dict import Position
from image_gen_classes.utils import (
    draw_centered_text,
    get_text_width,
    two_char_long,
    draw_centered_text,
)


class BinanceReport(Report):
    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        xy = (
            symbol_styling.position.x * self.image.size[0],
            symbol_styling.position.y * self.image.size[1],
        )
        font = ImageFont.truetype(symbol_styling.font, symbol_styling.font_size)

        if self.image_id in ["binance_4", "binance_5"]:
            draw_centered_text(symbol, xy, symbol_styling, font, self.draw)
        else:
            self.draw.text(
                xy,
                symbol,
                font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size),
                fill=symbol_styling.color,
            )

    def draw_roi(self, roi):
        roi_styling = self.styling["roi"]
        font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
        xy = (
            roi_styling.position.x * self.image.size[0],
            roi_styling.position.y * self.image.size[1],
        )

        if self.image_id in ["binance_4", "binance_5"]:
            roi = roi.replace(".", ",").replace("%", "")
            draw_centered_text(roi, xy, roi_styling, font, self.draw)

        else:
            self.draw.text(xy, roi, font=font, fill=roi_styling.color)

    def draw_details(self, signal_type, leverage, gen_date, username):
        try:
            if self.styling["draw_datetime"]:
                self.draw_datetime(gen_date)
        except KeyError:
            pass

        try:
            if self.styling["draw_username"]:
                self.draw_username(username)
        except KeyError:
            pass

        if self.image_id in ["binance_6", "binance_7", "binance_8"]:
            self.draw_signal_type_and_leverage(signal_type, leverage)

            return

        else:
            self.draw_signal_type(signal_type)
            self.draw_leverage(leverage)

        if self.image_id not in ["binance_4", "binance_5"]:
            self.draw_vertical_lines()

    def draw_signal_type_and_leverage(self, signal_type, leverage):
        # Draw the signal type and the leverage with a | character in between
        # The | character needs to be a larger font size

        signal_type = signal_type.capitalize()
        leverage = leverage.lower()
        separator_text = "|"

        signal_type_color = (
            self.styling["signal_type"].short_color
            if signal_type.lower() == "short"
            else self.styling["signal_type"].long_color
        )

        leverage_color = self.styling["leverage"].color

        font = ImageFont.truetype(
            self.styling["signal_type"].font,
            int(self.styling["signal_type"].font_size * 1.3),
        )
        smaller_font = ImageFont.truetype(
            self.styling["signal_type"].font, self.styling["signal_type"].font_size
        )

        spacing = get_text_width("Long", smaller_font) / 6

        xy = (
            self.styling["signal_type"].position.x * self.image.size[0],
            self.styling["signal_type"].position.y * self.image.size[1],
        )

        self.draw.text(xy, signal_type, font=smaller_font, fill=signal_type_color)
        self.draw.text(
            (xy[0] + get_text_width(signal_type, smaller_font) + spacing, xy[1]),
            separator_text,
            font=font,
            fill=leverage_color,
        )
        self.draw.text(
            (
                xy[0]
                + get_text_width(signal_type, smaller_font)
                + get_text_width(separator_text, font=font)
                + 2 * spacing,
                xy[1],
            ),
            leverage,
            font=ImageFont.truetype(
                self.styling["leverage"].font,
                int(self.styling["leverage"].font_size),
            ),
            fill=leverage_color,
        )

    def draw_datetime(self, gen_date: datetime.datetime):
        datetime_styling = self.styling["gen_date"]

        gen_date = gen_date + datetime.timedelta(hours=2)

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (
            datetime_styling.position.x * self.image.size[0],
            datetime_styling.position.y * self.image.size[1],
        )
        datetime_string = f"Shared on {gen_date.year}-{two_char_long(gen_date.month)}-{two_char_long(gen_date.day)} at {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)} (UTC+2)"
        if self.image_id in ["binance_6", "binance_7", "binance_8"]:
            datetime_string = f"{gen_date.year}-{two_char_long(gen_date.month)}-{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}:{two_char_long(gen_date.second)}"

        if self.image_id in ["binance_4", "binance_5"]:
            draw_centered_text(datetime_string, xy, datetime_styling, font, self.draw)

        else:
            self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)

    def draw_prices(self, entry, target):
        if self.image_id in ["binance_4", "binance_5"]:
            entry = entry.replace(".", ",")
            target = target.replace(".", ",")
            self.draw_entry(entry, center_align=True)
            self.draw_target(target, center_align=True)
        elif self.image_id in ["binance_6", "binance_7", "binance_8"]:
            self.draw_entry(entry)
            self.draw_target(target)
        else:
            self.draw_entry(entry, right_align=True)
            self.draw_target(target, right_align=True)

    def draw_referral_and_qr(self, referral, qr):
        self.draw_referral_code(referral)
        self.draw_qr(qr)

    def draw_vertical_lines(self):
        color = (164, 165, 167)
        if self.image_id in ["binance_6", "binance_7", "binance_8"]:
            color = (140, 140, 140)

        width = 2
        if self.image_id in ["binance_6", "binance_7", "binance_8"]:
            width = 3
        starting_position_1 = Position(
            self.styling["vertical_line_1"].position.x * self.image.size[0],
            self.styling["vertical_line_1"].position.y * self.image.size[1],
        )
        starting_position_2 = Position(
            self.styling["vertical_line_2"].position.x * self.image.size[0],
            self.styling["vertical_line_2"].position.y * self.image.size[1],
        )
        length = 28
        if self.image_id in ["binance_6", "binance_7", "binance_8"]:
            length = 33
        self.draw.line(
            (
                starting_position_1.x,
                starting_position_1.y,
                starting_position_1.x,
                starting_position_1.y + length,
            ),
            fill=color,
            width=width,
        )
        self.draw.line(
            (
                starting_position_2.x,
                starting_position_2.y,
                starting_position_2.x,
                starting_position_2.y + length,
            ),
            fill=color,
            width=width,
        )

    def draw_leverage(self, leverage):
        leverage_styling = self.styling["leverage"]
        leverage = leverage.lower()
        font = ImageFont.truetype(leverage_styling.font, leverage_styling.font_size)
        # Center_position_x represents the center point horizontally between the two vertical lines
        center_position_x = (
            self.image.size[0]
            * (
                self.styling["vertical_line_2"].position.x
                + self.styling["vertical_line_1"].position.x
            )
            / 2
        )
        xy = (center_position_x, leverage_styling.position.y * self.image.size[1])

        draw_centered_text(leverage, xy, leverage_styling, font, self.draw)

    def draw_signal_type(self, signal_type):
        signal_type = signal_type.capitalize()
        signal_type_styling = self.styling["signal_type"]

        color = (
            signal_type_styling.short_color
            if signal_type.lower() == "short"
            else signal_type_styling.long_color
        )

        xy = (
            signal_type_styling.position.x * self.image.size[0],
            signal_type_styling.position.y * self.image.size[1],
        )

        if self.image_id in ["binance_4", "binance_5"]:
            draw_centered_text(
                signal_type,
                xy,
                color,
                ImageFont.truetype(
                    signal_type_styling.font, signal_type_styling.font_size
                ),
                self.draw,
            )
        else:
            self.draw.text(
                xy,
                signal_type,
                font=ImageFont.truetype(
                    signal_type_styling.font, signal_type_styling.font_size
                ),
                fill=color,
            )

    def draw_username(self, username):
        username_styling = self.styling["username"]
        font = ImageFont.truetype(username_styling.font, username_styling.font_size)
        xy = (
            username_styling.position.x * self.image.size[0],
            username_styling.position.y * self.image.size[1],
        )
        self.draw.text(xy, username, font=font, fill=username_styling.color)
