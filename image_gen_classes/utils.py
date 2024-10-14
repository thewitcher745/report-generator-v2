from PIL import Image, ImageDraw

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


def two_char_long(string):
    string = str(string)
    if len(string) != 2:
        string = "0" + string
        return string
    else:
        return string

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
