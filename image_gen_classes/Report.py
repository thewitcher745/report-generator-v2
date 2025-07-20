from PIL import ImageFont

from image_gen_classes.utils import *


# General class containing methods common to all report types
class Report:
    def __init__(self, image_id, styling, img, draw_object):
        self.image_id = image_id
        self.styling = styling
        self.image = img
        self.draw = draw_object

    def draw_entry(self, entry, right_align=False, center_align=False):
        if self.image_id == "mexc_5":
            return

        entry_styling = self.styling["entry"]
        font = ImageFont.truetype(entry_styling.font, entry_styling.font_size)
        xy = (
            entry_styling.position.x * self.image.size[0],
            entry_styling.position.y * self.image.size[1],
        )

        if right_align:
            draw_right_aligned_text(entry, xy, entry_styling, font, self.draw)

        elif center_align:
            draw_centered_text(entry, xy, entry_styling, font, self.draw)

        else:
            self.draw.text(xy, entry, font=font, fill=entry_styling.color)

    def draw_target(self, target, right_align=False, center_align=False):
        if self.image_id == "mexc_5":
            return

        target_styling = self.styling["target"]
        font = ImageFont.truetype(target_styling.font, target_styling.font_size)
        xy = (
            target_styling.position.x * self.image.size[0],
            target_styling.position.y * self.image.size[1],
        )

        if right_align:
            draw_right_aligned_text(target, xy, target_styling, font, self.draw)

        elif center_align:
            draw_centered_text(target, xy, target_styling, font, self.draw)

        else:
            self.draw.text(xy, target, font=font, fill=target_styling.color)

    def draw_roi(self, roi):
        roi_styling = self.styling["roi"]
        font = ImageFont.truetype(roi_styling.font, roi_styling.font_size)
        xy = (
            roi_styling.position.x * self.image.size[0],
            roi_styling.position.y * self.image.size[1],
        )

        self.draw.text(xy, roi, font=font, fill=roi_styling.color)

    def draw_referral_code(self, referral):
        referral_styling = self.styling["referral"]
        font = ImageFont.truetype(referral_styling.font, referral_styling.font_size)
        xy = (
            referral_styling.position.x * self.image.size[0],
            referral_styling.position.y * self.image.size[1],
        )

        self.draw.text(xy, referral, font=font, fill=referral_styling.color)

    def draw_qr(self, qr):
        qr_styling = self.styling["qr_code"]
        xy = (
            int(qr_styling.position.x * self.image.size[0]),
            int(qr_styling.position.y * self.image.size[1]),
        )

        qr_image = Image.open(f"./qr/{qr}.png")
        qr_image = qr_image.resize((qr_styling.size, qr_styling.size))
        self.image.paste(qr_image, xy)

        # For better positioning
        # Define the coordinates of the rectangle (top-left and bottom-right corners)
        # top_left = xy
        # bottom_right = (xy[0] + qr_styling.size, xy[1] + qr_styling.size)

        # Draw the rectangle
        # self.draw.rectangle([top_left, bottom_right], outline=(255, 0, 0), width=1)
