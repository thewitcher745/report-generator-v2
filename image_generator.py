from PIL import Image, ImageDraw
import datetime
from dotenv import dotenv_values

from styling_dict import styling_dict
from image_gen_classes.BinanceReport import BinanceReport
from image_gen_classes.BingxReport import BingxReport
from image_gen_classes.BitgetReport import BitgetReport
from image_gen_classes.BybitReport import BybitReport
from image_gen_classes.MexcReport import MexcReport
from image_gen_classes.OkxReport import OkxReport
from image_gen_classes.LbankReport import LbankReport

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

    elif image_id.startswith("bingx"):
        report = BingxReport(image_id, styling, img, draw)

    elif image_id.startswith("okx"):
        report = OkxReport(image_id, styling, img, draw)

    elif image_id.startswith("lbank"):
        report = LbankReport(image_id, styling, img, draw)

    report.draw_symbol(symbol)
    report.draw_details(signal_type, leverage, gen_date, username)
    report.draw_roi(roi)
    report.draw_prices(entry, target)
    report.draw_referral_and_qr(referral, qr_code)

    img.save(f"./images/{filename}.png")
    # if mode == "dev":
    #     img.show()


if mode == "dev":
    generate_image("lbank_1.png", "MEWUSDT Perpetual", "long", "3X", "+53.11%", "0.005840", "0.006873", "okx_1", "3WZ8B", "test.png",
                   datetime.datetime.now(), "CANPREMIUM")
