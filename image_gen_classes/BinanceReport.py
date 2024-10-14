from PIL import ImageFont

from image_gen_classes.Report import Report
from styling_dict import Position
from image_gen_classes.utils import draw_centered_text

class BinanceReport(Report):
    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        self.draw.text(xy, symbol, font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)

    def draw_details(self, signal_type, leverage, datetime, username):
        self.draw_vertical_lines()
        self.draw_leverage(leverage)
        self.draw_signal_type(signal_type)

    def draw_prices(self, entry, target):
        self.draw_entry(entry, right_align=True)
        self.draw_target(target, right_align=True)

    def draw_referral_and_qr(self, referral, qr):
        self.draw_referral_code(referral)
        self.draw_qr(qr)

    def draw_vertical_lines(self):
        color = (164, 165, 167)
        starting_position_1 = Position(self.styling["vertical_line_1"].position.x * self.image.size[0],
                                       self.styling["vertical_line_1"].position.y * self.image.size[1])
        starting_position_2 = Position(self.styling["vertical_line_2"].position.x * self.image.size[0],
                                       self.styling["vertical_line_2"].position.y * self.image.size[1])
        length = 28
        self.draw.line(
            (starting_position_1.x, starting_position_1.y, starting_position_1.x, starting_position_1.y + length),
            fill=color, width=2)
        self.draw.line(
            (starting_position_2.x, starting_position_2.y, starting_position_2.x, starting_position_2.y + length),
            fill=color, width=2)

    def draw_leverage(self, leverage):
        leverage_styling = self.styling["leverage"]
        leverage = leverage.lower()
        font = ImageFont.truetype(leverage_styling.font, leverage_styling.font_size)
        # Center_position_x represents the center point horizontally between the two vertical lines
        center_position_x = self.image.size[0] * (self.styling["vertical_line_2"].position.x + self.styling["vertical_line_1"].position.x) / 2
        xy = (center_position_x, leverage_styling.position.y * self.image.size[1])

        draw_centered_text(leverage, xy, leverage_styling, font, self.draw)

    def draw_signal_type(self, signal_type):
        signal_type = signal_type.capitalize()
        signal_type_styling = self.styling["signal_type"]
        color = "#b6536c" if signal_type.lower() == "short" else "#438A70"
        xy = (signal_type_styling.position.x * self.image.size[0], signal_type_styling.position.y * self.image.size[1])

        self.draw.text(xy, signal_type, font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size), fill=color)
