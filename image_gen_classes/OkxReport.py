from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from image_gen_classes.utils import two_char_long, get_text_width


class OkxReport(Report):
    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, gen_date: datetime.datetime, username):
        self.draw_signal_type_and_leverage(signal_type, leverage)

        try:
            if self.styling["draw_datetime"]:
                self.draw_datetime(gen_date)
        except KeyError:
            pass

    def draw_datetime(self, gen_date: datetime.datetime):
        datetime_styling = self.styling["gen_date"]

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{two_char_long(gen_date.month)}/{two_char_long(gen_date.day)}/{gen_date.year}, {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}:{two_char_long(gen_date.second)}"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)

    def draw_prices(self, entry, target):
        self.draw_entry(entry)
        self.draw_target(target)

    def draw_referral_and_qr(self, referral, qr):
        try:
            if self.styling["draw_qr_referral"]:
                # self.draw_qr(qr)
                self.draw_referral_code(referral)
        except KeyError:
            pass

    def draw_signal_type_and_leverage(self, signal_type, leverage):
        signal_type_styling = self.styling["signal_type_leverage"]
        leverage_stripped = float(leverage.lower().replace("x", ""))
        leverage = f"{leverage_stripped:.2f}x"
        signal_type = signal_type.capitalize()

        font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)

        signal_type_leverage_text = f"{signal_type}  |  {leverage}  |  Closed"
        # OKX_1
        signal_type_width = get_text_width(signal_type, font)
        signal_type_color = signal_type_styling.color
        xy = (signal_type_styling.position.x * self.image.size[0], signal_type_styling.position.y * self.image.size[1])

        self.draw.text(xy, signal_type_leverage_text, font=font, fill=signal_type_color)
