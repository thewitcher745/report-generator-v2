from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from image_gen_classes.utils import get_text_width, two_char_long

class BingxReport(Report):
    v_line_spacing_1 = 27
    v_line_spacing_2 = 32
    v_line_length = 35
    v_line_width = 2
    v_line_color = "#4e4e4e"
    v_line_y_offset = 21

    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        symbol = symbol.replace(" Perpetual", "")
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])

        symbol_width = get_text_width(symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size))
        self.signal_type_x = xy[0] + symbol_width + 2 * BingxReport.v_line_spacing_1 + BingxReport.v_line_width
        self.draw_vertical_line(xy[0] + symbol_width + BingxReport.v_line_spacing_1, xy[1] + BingxReport.v_line_y_offset)

        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, gen_date: datetime.datetime, username):
        self.draw_signal_type(signal_type)
        self.draw_leverage(leverage)

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

    def draw_prices(self, entry, target):
        self.draw_entry(entry)
        self.draw_target(target)

    def draw_referral_and_qr(self, referral, qr):
        try:
            if self.styling["draw_qr_referral"]:
                self.draw_qr(qr)
                self.draw_referral_code(referral)
        except KeyError:
            pass

    def draw_signal_type(self, signal_type):
        signal_type_styling = self.styling["signal_type"]
        signal_type = signal_type.capitalize()
        font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)

        signal_type_color = signal_type_styling.long_color if signal_type.lower() == "long" else signal_type_styling.short_color
        xy = (self.signal_type_x, signal_type_styling.position.y * self.image.size[1])
        signal_type_styling.color = signal_type_color

        signal_type_width = get_text_width(signal_type, font=font)
        self.leverage_x = xy[0] + signal_type_width + 2 * BingxReport.v_line_spacing_2 + BingxReport.v_line_width
        self.draw_vertical_line(xy[0] + signal_type_width + BingxReport.v_line_spacing_2, xy[1] + BingxReport.v_line_y_offset)

        self.draw.text(xy, signal_type, font=font, fill=signal_type_styling.color)

    def draw_leverage(self, leverage):
        leverage_styling = self.styling["leverage"]
        leverage = leverage.upper()
        font = ImageFont.truetype(leverage_styling.font, leverage_styling.font_size)

        xy = (self.leverage_x, leverage_styling.position.y * self.image.size[1])

        self.draw.text(xy, leverage, font=font, fill=leverage_styling.color)

    def draw_username(self, username):
        username_styling = self.styling["username"]

        font = ImageFont.truetype(username_styling.font, username_styling.font_size)

        xy = (username_styling.position.x * self.image.size[0], username_styling.position.y * self.image.size[1])
        self.draw.text(xy, username, font=font, fill=username_styling.color)

        try:
            username_id_styling = self.styling["username_id"]
            username_id = f"@{username.lower()}"

            font = ImageFont.truetype(username_id_styling.font, username_id_styling.font_size)

            xy = (username_id_styling.position.x * self.image.size[0], username_id_styling.position.y * self.image.size[1])

            self.draw.text(xy, username_id, font=font, fill=username_id_styling.color)
        except KeyError:
            pass

    def draw_datetime(self, gen_date: datetime.datetime):
        datetime_styling = self.styling["gen_date"]

        gen_date = gen_date + datetime.timedelta(hours=3)

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{two_char_long(gen_date.month)}/{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)

    def draw_vertical_line(self, line_x, line_y):
        self.draw.line(
            (line_x, line_y, line_x, line_y + BingxReport.v_line_length), fill=BingxReport.v_line_color, width=BingxReport.v_line_width)

