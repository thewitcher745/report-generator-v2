from PIL import ImageFont
import datetime

from image_gen_classes.Report import Report
from image_gen_classes.utils import two_char_long, get_text_width, draw_transparent_rrect


class LbankReport(Report):

    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]

        symbol = symbol.replace("Perpetual", "Perp")
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        font = ImageFont.truetype(symbol_styling.font, symbol_styling.font_size)

        # Save the top right coordinates of the symbol for drawing the "Futures" rounded rect after it. Check the draw_details method
        self.symbol_tr_xy = (xy[0] + get_text_width(symbol, font), xy[1])

        self.draw.text(xy, symbol, font=font, fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, gen_date: datetime.datetime, username):
        self.draw_futures_rrect()
        self.draw_signal_type_and_leverage(signal_type, leverage)

        try:
            if self.styling["draw_datetime"]:
                self.draw_datetime(gen_date)
        except KeyError:
            pass

    def draw_futures_rrect(self):
        rrect_styling = self.styling["futures_rrect"]

        xy = (int(self.symbol_tr_xy[0] + rrect_styling.x_spacing), int(self.symbol_tr_xy[1] + rrect_styling.y_spacing))
        size = (rrect_styling.box_width, rrect_styling.box_height)

        draw_transparent_rrect(xy, size, rrect_styling.rect_radius, rrect_styling.box_color, 255, self.image)

        text_font = ImageFont.truetype(rrect_styling.font, rrect_styling.font_size)
        text_xy = (xy[0] + rrect_styling.padding_x, xy[1] + rrect_styling.padding_y)
        self.draw.text(text_xy, "Futures", font=text_font, fill=rrect_styling.text_color)

    def draw_datetime(self, gen_date: datetime.datetime):
        datetime_styling = self.styling["gen_date"]

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{gen_date.year}-{two_char_long(gen_date.month)}-{two_char_long(gen_date.day)} {two_char_long(gen_date.hour)}:{two_char_long(gen_date.minute)}:{two_char_long(gen_date.second)}"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)

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

    def draw_signal_type_and_leverage(self, signal_type, leverage):
        signal_type_styling = self.styling["signal_type"]
        leverage_styling = self.styling["leverage"]

        leverage_stripped = int(leverage.lower().replace("x", ""))
        leverage = f"{leverage_stripped}X"
        signal_type = signal_type.capitalize()

        signal_type_font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)

        signal_type_text = f"Close {signal_type} "

        if self.image_id == "lbank_1":
            signal_type_color = signal_type_styling.color
        else:
            signal_type_color = signal_type_styling.short_color if signal_type == "short" else signal_type_styling.long_color
        signal_type_xy = (signal_type_styling.position.x * self.image.size[0], signal_type_styling.position.y * self.image.size[1])

        self.draw.text(signal_type_xy, signal_type_text, font=signal_type_font, fill=signal_type_color)

        leverage_text = f" | {leverage}"
        leverage_color = leverage_styling.color
        leverage_xy = (signal_type_xy[0] + get_text_width(signal_type_text, signal_type_font), signal_type_xy[1])

        self.draw.text(leverage_xy, leverage_text, font=signal_type_font, fill=leverage_color)


