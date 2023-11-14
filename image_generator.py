from PIL import Image, ImageDraw, ImageFont
import datetime
from dotenv import dotenv_values

from styling_dict import styling_dict, Position

mode = dotenv_values(".env.secret")["MODE"]


def generate_image(image_name, symbol, signal_type, leverage, roi, entry, target, qr_code, referral, filename, gen_date: datetime.datetime,
                   username: str):
    image_id = image_name.split(".")[0]

    styling = styling_dict[image_id]
    img = Image.open(f'./background_images/{image_name}')
    draw = ImageDraw.Draw(img)

    report = BinanceReport(image_id, styling, img, draw)

    if image_id.startswith("bybit"):
        report = BybitReport(image_id, styling, img, draw)

    elif image_id.startswith("bitget"):
        report = BitgetReport(image_id, styling, img, draw)

    elif image_id.startswith("mexc"):
        report = MexcReport(image_id, styling, img, draw)

    report.draw_symbol(symbol)
    report.draw_details(signal_type, leverage, gen_date, username)
    report.draw_roi(roi)
    report.draw_prices(entry, target)
    report.draw_referral_and_qr(referral, qr_code)

    img.save(f"./images/{filename}.png")
    if mode == "dev":
        img.show()


def get_text_width(text, font):
    return font.getmask(text).getbbox()[2]


def get_text_height(text, font):
    ascent, descent = font.getmetrics()
    return font.getmask(text).getbbox()[3] + descent


# This function draws a text based on a horizontal center and a Y position
def draw_centered_text(text, position, styling, font, draw_object):
    text_width = get_text_width(text, font)
    position = (position[0] - text_width / 2, position[1])

    draw_object.text(position, text, font=font, fill=styling.color)


# This function draws a right aligned text based on top right position
def draw_right_aligned_text(text, position, styling, font, draw_object):
    text_width = get_text_width(text, font)
    position = (position[0] - text_width, position[1])

    draw_object.text(position, text, font=font, fill=styling.color)


# General class containing methods common to all report types
class Report:
    def __init__(self, image_id, styling, img, draw_object):
        self.image_id = image_id
        self.styling = styling
        self.image = img
        self.draw = draw_object

    def draw_entry(self, entry, right_align=False):
        entry_styling = self.styling["entry"]
        font = ImageFont.truetype(entry_styling.font, entry_styling.font_size)
        xy = (entry_styling.position.x * self.image.size[0], entry_styling.position.y * self.image.size[1])

        if right_align:
            draw_right_aligned_text(entry, xy, entry_styling, font, self.draw)
        else:
            self.draw.text(xy, entry, font=font, fill=entry_styling.color)

    def draw_target(self, target, right_align=False):
        target_styling = self.styling["target"]
        font = ImageFont.truetype(target_styling.font, target_styling.font_size)
        xy = (target_styling.position.x * self.image.size[0], target_styling.position.y * self.image.size[1])

        if right_align:
            draw_right_aligned_text(target, xy, target_styling, font, self.draw)
        else:
            self.draw.text(xy, target, font=font, fill=target_styling.color)

    def draw_roi(self, roi):
        roi_styling = self.styling["roi"]
        font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
        xy = (roi_styling.position.x * self.image.size[0], roi_styling.position.y * self.image.size[1])

        self.draw.text(xy, roi, font=font, fill=roi_styling.color)

    def draw_referral_code(self, referral):
        referral_styling = self.styling["referral"]
        font = ImageFont.truetype(referral_styling.font, referral_styling.font_size)
        xy = (referral_styling.position.x * self.image.size[0], referral_styling.position.y * self.image.size[1])

        self.draw.text(xy, referral, font=font, fill=referral_styling.color)

    def draw_qr(self, qr):
        qr_styling = self.styling["qr_code"]
        xy = (int(qr_styling.position.x * self.image.size[0]), int(qr_styling.position.y * self.image.size[1]))

        qr_image = Image.open(f"./qr/{qr}.png")
        qr_image = qr_image.resize((qr_styling.size, qr_styling.size))
        self.image.paste(qr_image, xy)


# Binance images have lowercase "x" in leverage and "Perpetual" in symbol
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


# Bybit images have uppercase "X" in leverage and no "Perpetual" in symbol
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
        def draw_transparent_rrect(xy, size, rect_radius, color, alpha, background_image):
            img_f = Image.new("RGB", size, color=color)
            img_b = background_image

            img_alpha = Image.new("L", img_f.size, 0)
            draw_alpha = ImageDraw.Draw(img_alpha)
            draw_alpha.rounded_rectangle((0, 0, size[0], size[1]), fill=alpha,
                                         radius=rect_radius)

            im_rgba = img_f.copy()
            im_rgba.putalpha(img_alpha)

            img_b.paste(img_f, xy, mask=im_rgba)

        text = f"{signal_type.capitalize()} {leverage}"

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
        draw_transparent_rrect(box_xy, (box_width, box_height), radius, box_color, 190, self.image)
        self.draw.text(text_xy, text,
                       font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size),
                       fill=text_color)


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

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{gen_date.year}-{gen_date.month}-{gen_date.day} {gen_date.hour}:{gen_date.minute}"
        if self.image_id.startswith("bitget_4"):
            datetime_string = f"{gen_date.year}/{gen_date.month}/{gen_date.day} {gen_date.hour}:{gen_date.minute} ( UTC-4 )"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)


class MexcReport(Report):
    def draw_symbol(self, symbol):
        symbol_styling = self.styling["symbol"]
        xy = (symbol_styling.position.x * self.image.size[0], symbol_styling.position.y * self.image.size[1])
        symbol = symbol.replace("USDT", " USDT")
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

    def draw_prices(self, entry, target):
        entry = "$" + entry
        target = "$" + target
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

        font = ImageFont.truetype(datetime_styling.font, datetime_styling.font_size)
        xy = (datetime_styling.position.x * self.image.size[0], datetime_styling.position.y * self.image.size[1])
        datetime_string = f"{gen_date.year}-{gen_date.month}-{gen_date.day} {gen_date.hour}:{gen_date.minute}:{gen_date.second}"
        if self.image_id.startswith("bitget_4"):
            datetime_string = f"{gen_date.year}/{gen_date.month}/{gen_date.day} {gen_date.hour}:{gen_date.minute} ( UTC-4 )"

        self.draw.text(xy, datetime_string, font=font, fill=datetime_styling.color)


if mode == "dev":
    generate_image("bitget_3.png", "LOOMUSDT Perpetual", "short", "9X", "+403.14%", "0.0968", "0.1402", "mexc_1", "K01A8CF0", "test.png",
                   datetime.datetime.now(), "CANPREMIUM")
