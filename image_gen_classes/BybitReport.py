from PIL import ImageFont, Image, ImageDraw

from image_gen_classes.Report import Report
from image_gen_classes.utils import get_text_width, get_text_height, draw_transparent_rrect
class BybitReport(Report):
    def draw_symbol(self, symbol):
        symbol = symbol.replace(" Perpetual", "")
        self.symbol = symbol
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, datetime, username):
        self.draw_signal_type_and_leverage(signal_type, leverage)

    def draw_prices(self, entry, target):
        self.draw_entry(entry)
        self.draw_target(target)

    def draw_referral_and_qr(self, referral, qr):
        self.draw_referral_code(referral)
        self.draw_qr(qr)

    def draw_signal_type_and_leverage(self, signal_type, leverage):
        leverage = leverage.lower().replace("x", "")
        text = f"{signal_type.capitalize()} {f'{float(leverage)}'}X"

        signal_type_styling = self.styling["signal_type"]
        symbol_styling = self.styling["symbol"]
        margin_x = signal_type_styling.margin_x
        margin_y = signal_type_styling.margin_y
        spacing = signal_type_styling.spacing
        margin_y_mult = signal_type_styling.margin_y_mult
        radius = signal_type_styling.rect_radius
        font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)
        symbol_font = ImageFont.truetype(symbol_styling.font, symbol_styling.font_size)

        # The horizontal position of the box is the sum of the length of the symbol, plus its distance from the left edge,
        # plus a certain distance between the two
        box_x = get_text_width(self.symbol, symbol_font) + symbol_styling.position.x * self.image.size[0] + spacing
        box_xy = (int(box_x), int(signal_type_styling.position.y * self.image.size[1]))
        text_xy = (box_x + margin_x, box_xy[1] + margin_y_mult * margin_y)

        box_width = get_text_width(text, font) + 2 * margin_x
        box_height = get_text_height(text, font) + 2 * margin_y

        text_color = signal_type_styling.short_color if signal_type.lower() == "short" else signal_type_styling.long_color
        box_color = signal_type_styling.short_box_color if signal_type.lower() == "short" else signal_type_styling.long_box_color
        alpha = 190

        if self.image_id == "bybit_4":
            alpha = 100

        draw_transparent_rrect(box_xy, (box_width, box_height), radius, box_color, alpha, self.image)
        self.draw.text(text_xy, text,
                       font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size),
                       fill=text_color)

