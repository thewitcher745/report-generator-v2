class ElementStyling:
    def __init__(self, position, font="arial.ttf", font_size=12, color=(255, 255, 255), size=150, margin_x=12,
                 margin_y=12, margin_y_mult: float = 1, spacing=40, rect_radius=7):
        self.position = position
        self.font = font
        self.font_size = font_size
        self.color = color
        self.size = size
        self.margin_x = margin_x
        self.margin_y = margin_y
        self.spacing = spacing
        self.margin_y_mult = margin_y_mult
        self.rect_radius = rect_radius


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


styling_dict = {
    "binance_1": {
        "vertical_line_1": ElementStyling(position=Position(0.24, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.38, 0.2885)),
        "symbol": ElementStyling(position=Position(0.41, 0.285), font="./fonts/BinancePlex.otf", font_size=22,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.285), font="./fonts/BinancePlex.otf", font_size=22,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.285), font="./fonts/BinancePlex.otf", font_size=22,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=65,
                              color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/BinancePlex.otf", font_size=20,
                                color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/BinancePlex.otf", font_size=20,
                                 color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.23, 0.766), font="./fonts/BinancePlex.otf", font_size=28,
                                   color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(117 / 1035, 460 / 624), size=64)
    },
    "binance_2": {
        "vertical_line_1": ElementStyling(position=Position(0.2328, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.34, 0.2885)),
        "symbol": ElementStyling(position=Position(0.372, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=90,
                              color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/DIN 2014 Demi.ttf", font_size=30,
                                color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/DIN 2014 Demi.ttf", font_size=30,
                                 color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.23, 0.7836), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=40,
                                   color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(112 / 980, 457 / 619), size=94)
    },
    "binance_3": {
        "vertical_line_1": ElementStyling(position=Position(0.2328, 0.2885)),
        "vertical_line_2": ElementStyling(position=Position(0.34, 0.2885)),
        "symbol": ElementStyling(position=Position(0.372, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.11, 0.35), font="./fonts/BinancePlex.otf", font_size=90,
                              color=(52, 183, 133)),
        "entry": ElementStyling(position=Position(0.4792, 0.548), font="./fonts/DIN 2014 Demi.ttf", font_size=30,
                                color=(237, 187, 54)),
        "target": ElementStyling(position=Position(0.4792, 0.6), font="./fonts/DIN 2014 Demi.ttf", font_size=30,
                                 color=(237, 187, 54)),
        "referral": ElementStyling(position=Position(0.243, 0.79), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=40,
                                   color=(255, 255, 255)),
        "qr_code": ElementStyling(position=Position(118 / 980, 460 / 619), size=94)
    },
    "bybit_1": {
        "symbol": ElementStyling(position=Position(0.045, 0.2), font="./fonts/IBMPlexSans-Bold.ttf", font_size=60,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.21), font="./fonts/IBMPlexSans-Medium.TTF",
                                      font_size=30,
                                      margin_x=10,
                                      margin_y=12,
                                      margin_y_mult=0.6,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.045, 0.35), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=100,
                              color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.045, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                color="white"),
        "target": ElementStyling(position=Position(0.222, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                 color="white"),
        "referral": ElementStyling(position=Position(0.29, 0.88), font="./fonts/IBMPlexSans-SemiBold.ttf",
                                   font_size=50,
                                   color="black"),
        "qr_code": ElementStyling(position=Position(0.842, 0.793), size=150)
    },
    "bybit_2": {
        "symbol": ElementStyling(position=Position(0.062, 0.175), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=55,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.187), font="./fonts/IBMPlexSans-Regular.TTF",
                                      font_size=27,
                                      margin_x=8,
                                      margin_y=6,
                                      margin_y_mult=0.5,
                                      spacing=25,
                                      rect_radius=5,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.065, 0.3), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=95,
                              color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.063, 0.468), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                color="white"),
        "target": ElementStyling(position=Position(0.063, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                 color="white"),
        "referral": ElementStyling(position=Position(0.425, 0.919), font="./fonts/IBMPlexSans-Medium.ttf",
                                   font_size=50,
                                   color="black"),
        "qr_code": ElementStyling(position=Position(722 / 930, 1084 / 1280), size=161)
    },
    "bybit_3": {
        "symbol": ElementStyling(position=Position(0.045, 0.2), font="./fonts/IBMPlexSans-Bold.ttf", font_size=60,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.116, 0.21), font="./fonts/IBMPlexSans-Medium.TTF",
                                      font_size=30,
                                      margin_x=10,
                                      margin_y=12,
                                      margin_y_mult=0.7,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.2734, 0.287), font="./fonts/BAHNSCHRIFT 1.TTF", font_size=30,
                                   color=(255, 255, 255)),
        "roi": ElementStyling(position=Position(0.045, 0.35), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=100,
                              color=(33, 182, 114)),
        "entry": ElementStyling(position=Position(0.045, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                color="white"),
        "target": ElementStyling(position=Position(0.235, 0.57), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=45,
                                 color="white"),
        "referral": ElementStyling(position=Position(0.29, 0.88), font="./fonts/IBMPlexSans-SemiBold.ttf",
                                   font_size=50,
                                   color="black"),
        "qr_code": ElementStyling(position=Position(0.842, 0.793), size=150)
    },
    "bitget_1": {
        "symbol": ElementStyling(position=Position(0.062, 0.07), font="./fonts/IBMPlexSans-Medium.ttf", font_size=54,
                                 color=(255, 255, 255)),
        "signal_type": ElementStyling(position=Position(0.062, 0.225), font="./fonts/IBMPlexSans-Medium.TTF",
                                      font_size=35,
                                      margin_x=10,
                                      margin_y=12,
                                      margin_y_mult=0.7,
                                      color=(255, 255, 255)),
        "leverage": ElementStyling(position=Position(0.22, 0.225), font="./fonts/IBMPlexSans-SemiBold.TTF", font_size=35,
                                   color="#7e898b"),
        "roi": ElementStyling(position=Position(0.048, 0.43), font="./fonts/IBMPlexSans-Medium.ttf", font_size=100,
                              color="#04a3c0"),
        "entry": ElementStyling(position=Position(0.34, 0.72), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=37,
                                color="white"),
        "target": ElementStyling(position=Position(0.34, 0.82), font="./fonts/IBMPlexSans-SemiBold.ttf", font_size=37,
                                 color="white"),
    },
}
