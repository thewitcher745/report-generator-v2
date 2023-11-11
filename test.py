from datetime import datetime

utc_offset = datetime.fromtimestamp(1) - datetime.utcfromtimestamp(1)


class ElementStyling:
    def __init__(self, **params):
        print(params)


ElementStyling(a=1)
