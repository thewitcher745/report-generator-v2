from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from image_gen_classes.utils import two_char_long

class BitgetReport(Report):
    def draw_symbol(self, symbol):
        if self.image_id != "bitget_3":
            symbol = symbol.replace(" Perpetual", "")
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, gen_date: datetime.datetime, username):
        self.draw_leverage(leverage)
        self.draw_signal_type(signal_type)

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

    def draw_leverage(self, leverage):
        leverage_styling = self.styling["leverage"]
        leverage = leverage.upper()
        if self.image_id == "bitget_3":
            leverage = leverage.lower()
        font = ImageFont.truetype(leverage_styling.font, leverage_styling.font_size)

        xy = (leverage_styling.position.x * self.image.size[0], leverage_styling.position.y * self.image.size[1])
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

    def draw_signal_type(self, signal_type):
        signal_type_styling = self.styling["signal_type"]
        signal_type = signal_type.capitalize()
        if self.image_id.startswith("bitget_2"):
            signal_type = signal_type.upper()

        color = signal_type_styling.short_color if signal_type.lower() == "short" else signal_type_styling.long_color

        xy = (signal_type_styling.position.x * self.image.size[0], signal_type_styling.position.y * self.image.size[1])

        self.draw.text(xy, signal_type, font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size), fill=color)

    def draw_datetime(self, gen_date: datetime.datetime):
        datetime_styling = self.styling["gen_date"]

        gen_date = gen_date + datetime.timedelta(hours=-3)

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{gen_date.year}-{two_char_long(gen_date.month)}-{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}"
        if self.image_id.startswith("bitget_4"):
            datetime_string = f"{gen_date.year}/{two_char_long(gen_date.month)}/{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)} ( UTC-3 )"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)
