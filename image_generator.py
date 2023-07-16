from PIL import Image, ImageDraw, ImageFont

from styling_dict import styling_dict, Position


def generate_image(image_id, symbol, signal_type, leverage, roi, entry, target, qr_code, referral, filename):
    styling = styling_dict[image_id]

    img = Image.open(f'./background_images/{image_id}.png')
    draw = ImageDraw.Draw(img)

    if image_id.startswith("binance"):
        draw_vertical_lines(styling, draw, img)
        draw_signal_type(signal_type, styling, draw, img)
        draw_leverage(leverage, styling, draw, img)
        draw_entry(entry, styling, draw, img, right_align=True)
        draw_target(target, styling, draw, img, right_align=True)

    elif image_id.startswith("bybit"):
        leverage = leverage.upper()
        draw_bybit_signal_type(signal_type, leverage, symbol, styling, draw, img)
        draw_entry(entry, styling, draw, img)
        draw_target(target, styling, draw, img)

    draw_symbol(symbol, styling, draw, img)
    draw_roi(roi, styling, draw, img)
    draw_referral(referral, styling, draw, img)
    draw_qr(qr_code, styling, draw, img)

    img.save(f"./images/{filename}.png")


def draw_vertical_lines(styling, draw_object, image):
    color = (164, 165, 167)
    starting_position_1 = Position(styling["vertical_line_1"].position.x * image.size[0],
                                   styling["vertical_line_1"].position.y * image.size[1])
    starting_position_2 = Position(styling["vertical_line_2"].position.x * image.size[0],
                                   styling["vertical_line_2"].position.y * image.size[1])
    length = 28
    draw_object.line(
        (starting_position_1.x, starting_position_1.y, starting_position_1.x, starting_position_1.y + length),
        fill=color, width=2)
    draw_object.line(
        (starting_position_2.x, starting_position_2.y, starting_position_2.x, starting_position_2.y + length),
        fill=color, width=2)


def draw_symbol(symbol, styling, draw_object, image):
    symbol_styling = styling["symbol"]
    xy = (symbol_styling.position.x * image.size[0], symbol_styling.position.y * image.size[1])
    draw_object.text(xy, symbol,
                     font=ImageFont.truetype(symbol_styling.font, symbol_styling.font_size), fill=symbol_styling.color)


def draw_signal_type(signal_type, styling, draw_object, image):
    signal_type_styling = styling["signal_type"]
    color = "#b6536c" if signal_type.lower() == "short" else "#438A70"
    xy = (signal_type_styling.position.x * image.size[0], signal_type_styling.position.y * image.size[1])

    draw_object.text(xy, signal_type, font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size),
                     fill=color)


def draw_leverage(leverage, styling, draw_object, image):
    leverage_styling = styling["leverage"]
    font = ImageFont.truetype(leverage_styling.font, leverage_styling.font_size)
    # Center_position_x represents the center point horizontally between the two vertical lines
    center_position_x = image.size[0] * (
            styling["vertical_line_2"].position.x + styling["vertical_line_1"].position.x) / 2
    xy = (center_position_x, leverage_styling.position.y * image.size[1])

    draw_centered_text(leverage, xy, leverage_styling,
                       font, draw_object)


def draw_bybit_signal_type(signal_type, leverage, symbol, styling, draw_object, img):
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

    signal_type_styling = styling["signal_type"]
    symbol_styling = styling["symbol"]
    margin_x = signal_type_styling.margin_x
    margin_y = signal_type_styling.margin_y
    spacing = signal_type_styling.spacing
    margin_y_mult = signal_type_styling.margin_y_mult
    radius = signal_type_styling.rect_radius
    font = ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size)
    symbol_font = ImageFont.truetype(symbol_styling.font, symbol_styling.font_size)

    # The horizontal position of the box is the sum of the length of the symbol, plus its distance from the left edge,
    # plus a certain distance between the two
    box_x = get_text_width(symbol, symbol_font) + symbol_styling.position.x * img.size[0] + spacing
    box_xy = (int(box_x), int(signal_type_styling.position.y * img.size[1]))
    text_xy = (box_x + margin_x, box_xy[1] + margin_y_mult * margin_y)

    box_width = get_text_width(text, font) + 2 * margin_x
    box_height = get_text_height(text, font) + 2 * margin_y

    box_color = (64, 38, 39) if signal_type.lower() == "short" else (34, 51, 45)
    text_color = (220, 66, 90) if signal_type.lower() == "short" else (33, 182, 114)
    draw_transparent_rrect(box_xy, (box_width, box_height), radius, box_color, 190, img)
    draw_object.text(text_xy, text,
                     font=ImageFont.truetype(signal_type_styling.font, signal_type_styling.font_size),
                     fill=text_color)


def draw_roi(roi, styling, draw_object, image):
    roi_styling = styling["roi"]
    font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
    xy = (roi_styling.position.x * image.size[0], roi_styling.position.y * image.size[1])

    draw_object.text(xy, roi, font=font, fill=roi_styling.color)


def draw_entry(entry, styling, draw_object, image, right_align=False):
    entry_styling = styling["entry"]
    font = ImageFont.truetype(entry_styling.font, entry_styling.font_size)
    xy = (entry_styling.position.x * image.size[0], entry_styling.position.y * image.size[1])

    if right_align:
        draw_right_aligned_text(entry, xy, entry_styling, font, draw_object)
    else:
        draw_object.text(xy, entry, font=font, fill=entry_styling.color)


def draw_target(target, styling, draw_object, image, right_align=False):
    target_styling = styling["target"]
    font = ImageFont.truetype(target_styling.font, target_styling.font_size)
    xy = (target_styling.position.x * image.size[0], target_styling.position.y * image.size[1])

    if right_align:
        draw_right_aligned_text(target, xy, target_styling, font, draw_object)
    else:
        draw_object.text(xy, target, font=font, fill=target_styling.color)


def draw_referral(referral, styling, draw_object, image):
    referral_styling = styling["referral"]
    font = ImageFont.truetype(referral_styling.font, referral_styling.font_size)
    xy = (referral_styling.position.x * image.size[0], referral_styling.position.y * image.size[1])

    draw_object.text(xy, referral, font=font, fill=referral_styling.color)


def draw_qr(qr, styling, draw_object, image):
    qr_styling = styling["qr_code"]
    xy = (int(qr_styling.position.x * image.size[0]), int(qr_styling.position.y * image.size[1]))

    qr_image = Image.open(f"./qr/{qr}.png")
    qr_image = qr_image.resize((qr_styling.size, qr_styling.size))
    image.paste(qr_image, xy)


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


