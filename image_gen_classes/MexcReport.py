from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from image_gen_classes.utils import two_char_long, get_text_width

class MexcReport(Report):
    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])

        if self.image_id == "mexc_2" or self.image_id == "mexc_3":
            symbol = symbol.replace("USDT", " USDT").replace("Perpetual", "Sürekli")

        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, gen_date: datetime.datetime, username):
        self.draw_signal_type_and_leverage(signal_type, leverage)

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

    def draw_roi(self, roi):
        roi_styling = self.styling["roi"]

        if self.image_id == "mexc_2" or self.image_id == "mexc_3":
            roi = roi.replace("%", "").replace("+", "+%").replace(".", ",")

        font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
        xy = (roi_styling.position.x * self.image.size[0], roi_styling.position.y * self.image.size[1])

        self.draw.text(xy, roi, font=font, fill=roi_styling.color)

    def draw_prices(self, entry, target):
        entry = "$" + entry
        target = "$" + target
        if self.image_id == "mexc_2":
            entry = entry.replace(".", ",")
            target = target.replace(".", ",")
        self.draw_entry(entry)
        self.draw_target(target)

    def draw_referral_and_qr(self, referral, qr):
        try:
            if self.styling["draw_qr_referral"]:
                self.draw_qr(qr)
                self.draw_referral_code(referral)
        except KeyError:
            pass

    def draw_signal_type_and_leverage(self, signal_type, leverage):
        signal_type_styling = self.styling["signal_type"]
        leverage = leverage.upper()
        signal_type = signal_type.capitalize()

        if self.image_id == "mexc_3":
            signal_type += " Kapat"

        font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)

        # MEXC_1
        signal_type_width = get_text_width(signal_type, font)
        signal_type_color = signal_type_styling.long_color if signal_type.lower() == "long" else signal_type_styling.short_color
        starting_xy = (signal_type_styling.position.x * self.image.size[0], signal_type_styling.position.y * self.image.size[1])

        self.draw.text(starting_xy, signal_type, font=font, fill=signal_type_color)
        leverage_xy = (starting_xy[0] + signal_type_width + 5, starting_xy[1])
        self.draw.text(leverage_xy, "/" + leverage, font=font, fill="white")

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

        gen_date = gen_date + datetime.timedelta(hours=-1)

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{gen_date.year}-{two_char_long(gen_date.month)}-{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}:{two_char_long(gen_date.second)}"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)
