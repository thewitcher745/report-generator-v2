class ElementStyling:
    def __init__(self, **params):
        for key in params.keys():
            self.__setattr__(key, params[key])


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


styling_dict = {
    "binance_1": {
        "vertical_line_1": ElementStyling(position=Position(0.24, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.38, 0.2885)),
        "symbol": ElementStyling(position=Position(0.41, 0.285), font="./fonts/BinancePlex.otf", font_size=22, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.285), font="./fonts/BinancePlex.otf", font_size=22, color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.285), font="./fonts/BinancePlex.otf", font_size=22, color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=65, color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/BinancePlex.otf", font_size=20, color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/BinancePlex.otf", font_size=20, color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.23, 0.766), font="./fonts/BinancePlex.otf", font_size=28, color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(117 / 1035, 460 / 624), size=64)
    },
    "binance_2": {
        "vertical_line_1": ElementStyling(position=Position(0.2328, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.34, 0.2885)),
        "symbol": ElementStyling(position=Position(0.372, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=90, color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/DIN 2014 Demi.ttf", font_size=30, color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/DIN 2014 Demi.ttf", font_size=30, color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.23, 0.7836), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=40, color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(112 / 980, 457 / 619), size=94)
    },
    "binance_3": {
        "vertical_line_1": ElementStyling(position=Position(0.2328, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.34, 0.2885)),
        "symbol": ElementStyling(position=Position(0.372, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30, color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=90, color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/DIN 2014 Demi.ttf", font_size=30, color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/DIN 2014 Demi.ttf", font_size=30, color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.243, 0.79), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=40, color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(118 / 980, 460 / 619), size=94)
    },
    "bybit_1": {
        "symbol": ElementStyling(position=Position(0.045, 0.2), font="./fonts/IBMPlexSans-Bold.ttf", font_size=60, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.21), font="./fonts/IBMPlexSans-Medium.TTF", font_size=30, margin_x=10, margin_y=12,
                                      margin_y_mult=0.6, spacing=25, rect_radius=5,
                                      short_color=(220, 66, 90), long_color=(33, 182, 114),
                                      short_box_color=(64, 38, 39), long_box_color=(34, 51, 45)),
        "roi": ElementStyling(position=Position(0.045, 0.35), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=100, color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.045, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "target": ElementStyling(position=Position(0.222, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "referral": ElementStyling(position=Position(0.29, 0.88), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=50, color="black"),
        "qr_code": ElementStyling(position=Position(0.842, 0.793), size=150)
    },
    "bybit_2": {
        "symbol": ElementStyling(position=Position(0.062, 0.175), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=55, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.187), font="./fonts/IBMPlexSans-Regular.TTF", font_size=27, margin_x=8, margin_y=6,
                                      margin_y_mult=0.5, spacing=25, rect_radius=5, short_color=(220, 66, 90), long_color=(33, 182, 114),
                                      short_box_color=(64, 38, 39),
                                      long_box_color=(34, 51, 45)),
        "roi": ElementStyling(position=Position(0.065, 0.3), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=95, color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.063, 0.468), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "target": ElementStyling(position=Position(0.063, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "referral": ElementStyling(position=Position(0.425, 0.919), font="./fonts/IBMPlexSans-Medium.ttf", font_size=50, color="black"),
        "qr_code": ElementStyling(position=Position(722 / 930, 1084 / 1280), size=161)
    },
    "bybit_3": {
        "symbol": ElementStyling(position=Position(0.045, 0.2), font="./fonts/IBMPlexSans-Bold.ttf", font_size=60, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.21), font="./fonts/IBMPlexSans-Medium.TTF", font_size=30, margin_x=10, margin_y=12,
                                      margin_y_mult=0.7, spacing=25, rect_radius=5,
                                      short_color=(220, 66, 90), long_color=(33, 182, 114),
                                      short_box_color=(64, 38, 39), long_box_color=(34, 51, 45)),
        "roi": ElementStyling(position=Position(0.045, 0.35), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=100, color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.045, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "target": ElementStyling(position=Position(0.235, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45, color="white"),
        "referral": ElementStyling(position=Position(0.29, 0.88), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=50, color="black"),
        "qr_code": ElementStyling(position=Position(0.842, 0.793), size=150)
    },
    "bitget_1": {
        "symbol": ElementStyling(position=Position(0.062, 0.07), font="./fonts/avenir-next-medium.ttf", font_size=54, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.062, 0.225), font="./fonts/avenir-next-medium.ttf", font_size=35, margin_x=10, margin_y=12,
                                      margin_y_mult=0.7,
                                      short_color="#fb3832",
                                      long_color="#338d96"),
        "leverage": ElementStyling(position=Position(0.22, 0.225), font="./fonts/avenir-next-medium.ttf", font_size=35, color="#7e898b"),
        "roi": ElementStyling(position=Position(0.048, 0.43), font="./fonts/avenir-next-medium.ttf", font_size=100, color="#04a3c0"),
        "entry": ElementStyling(position=Position(0.34, 0.72), font="./fonts/avenir-next-bold.ttf", font_size=37, color="white"),
        "target": ElementStyling(position=Position(0.34, 0.82), font="./fonts/avenir-next-bold.ttf", font_size=37, color="white"),
    },
    "bitget_2": {
        "symbol": ElementStyling(position=Position(0.064, 0.395), font="./fonts/kommon-grotesk-medium.otf", font_size=29, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.062, 0.48), font="./fonts/kommon-grotesk-medium.otf", font_size=18, margin_x=10,
                                      margin_y=12, margin_y_mult=0.7,
                                      short_color="#fb3832",
                                      long_color="#338d96"),
        "leverage": ElementStyling(position=Position(0.225, 0.48), font="./fonts/kommon-grotesk-bold.otf", font_size=20, color="#7e898b"),
        "roi": ElementStyling(position=Position(0.063, 0.61), font="./fonts/Araboto Normal 400.ttf", font_size=60, color="#04a3c0"),
        "entry": ElementStyling(position=Position(0.37, 0.76), font="./fonts/Araboto Bold 400.ttf", font_size=23, color="white"),
        "target": ElementStyling(position=Position(0.37, 0.816), font="./fonts/Araboto Bold 400.ttf", font_size=23, color="white"),
        "username": ElementStyling(position=Position(0.175, 0.24), font="./fonts/Araboto Black 400.ttf", font_size=30, color="white"),
        "draw_username": True
    },
    "bitget_3": {
        "symbol": ElementStyling(position=Position(0.035, 0.072), font="./fonts/Araboto Bold 400.ttf", font_size=20, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.035, 0.155), font="./fonts/Araboto Normal 400.ttf", font_size=12, margin_x=10, margin_y=12,
                                      margin_y_mult=0.7,
                                      short_color="#aa4e81",
                                      long_color="#3ba3a3"),
        "leverage": ElementStyling(position=Position(0.116, 0.157), font="./fonts/kommon-grotesk-bold.otf", font_size=14, color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.035, 0.32), font="./fonts/Araboto Normal 400.ttf", font_size=49, color="#23b3aa"),
        "entry": ElementStyling(position=Position(0.18, 0.48), font="./fonts/Araboto Bold 400.ttf", font_size=12, color=(110, 85, 251)),
        "target": ElementStyling(position=Position(0.18, 0.553), font="./fonts/Araboto Bold 400.ttf", font_size=12, color=(110, 85, 251)),
        "gen_date": ElementStyling(position=Position(0.165, 0.65), font="./fonts/Araboto Normal 400.ttf", font_size=12, color=(101, 102, 120)),
        "referral": ElementStyling(position=Position(0.17, 0.84), font="./fonts/Araboto Bold 400.ttf", font_size=20, color="white"),
        "qr_code": ElementStyling(position=Position(0.045, 0.76), size=55),
        "draw_qr_referral": True,
        "draw_datetime": True
    },
    "bitget_4": {
        "symbol": ElementStyling(position=Position(0.07, 0.3664), font="./fonts/Araboto Normal 400.ttf", font_size=60, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.072, 0.448), font="./fonts/Araboto Normal 400.ttf", font_size=38, margin_x=10, margin_y=12,
                                      margin_y_mult=0.7,
                                      short_color="#ff474d",
                                      long_color="#299bb6"),
        "leverage": ElementStyling(position=Position(0.24, 0.448), font="./fonts/Araboto Normal 400.ttf", font_size=36, color="#818584"),
        "roi": ElementStyling(position=Position(0.07, 0.53), font="./fonts/Araboto Normal 400.ttf", font_size=110, color="#299bb6"),
        "entry": ElementStyling(position=Position(0.33, 0.67), font="./fonts/Araboto Bold 400.ttf", font_size=40, color="white"),
        "target": ElementStyling(position=Position(0.33, 0.725), font="./fonts/Araboto Bold 400.ttf", font_size=40, color="white"),
        "gen_date": ElementStyling(position=Position(0.07, 0.115), font="./fonts/Araboto Normal 400.ttf", font_size=33, color="#828282"),
        "referral": ElementStyling(position=Position(0.312, 0.894), font="./fonts/Araboto Bold 400.ttf", font_size=35, color="white"),
        "qr_code": ElementStyling(position=Position(0.748, 0.85), size=140),
        "username": ElementStyling(position=Position(0.215, 0.195), font="./fonts/Araboto Black 400.ttf", font_size=55, color="white"),
        "username_id": ElementStyling(position=Position(0.22, 0.257), font="./fonts/Araboto Normal 400.ttf", font_size=35, color=(124, 125, 127)),
        "draw_qr_referral": True,
        "draw_datetime": True,
        "draw_username": True
    },
    "mexc_1": {
        "symbol": ElementStyling(position=Position(0.058, 0.3), font="./fonts/Avenir LT Std 85 Heavy.otf", font_size=42, color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.058, 0.365), font="./fonts/Avenir LT Std 65 Medium.otf", font_size=42, margin_x=10,
                                      margin_y=12, margin_y_mult=0.7,
                                      short_color="#f44363", long_color="#18b37a"),
        "roi": ElementStyling(position=Position(0.058, 0.438), font="./fonts/Avenir LT Std 85 Heavy.otf", font_size=98, color="#11b67a"),
        "entry": ElementStyling(position=Position(0.268, 0.9), font="./fonts/Avenir LT Std 65 Medium.otf", font_size=36, color="white"),
        "target": ElementStyling(position=Position(0.268, 0.85), font="./fonts/Avenir LT Std 65 Medium.otf", font_size=36, color="white"),
        "gen_date": ElementStyling(position=Position(0.268, 0.95), font="./fonts/Avenir LT Std 65 Medium.otf", font_size=36, color="white"),
        "referral": ElementStyling(position=Position(0.312, 0.894), font="./fonts/Araboto Bold 400.ttf", font_size=35, color="white"),
        "qr_code": ElementStyling(position=Position(0.748, 0.85), size=140),
        "username": ElementStyling(position=Position(0.215, 0.195), font="./fonts/Araboto Black 400.ttf", font_size=55, color="white"),
        "username_id": ElementStyling(position=Position(0.22, 0.257), font="./fonts/Araboto Normal 400.ttf", font_size=35, color=(124, 125, 127)),
        "draw_datetime": True,
    },
}
