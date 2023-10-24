import re
import csv


async def send_message(context, update, message_text, keyboard=None, is_callback_query=False):
    chat_id = update.callback_query.message.chat_id if is_callback_query else update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text=message_text,
                                   reply_markup=keyboard)


def separate_number(number):
    number_str = str(number)
    integer_part, decimal_part = number_str.split(".")
    integer_part = integer_part[::-1]
    integer_parts = [integer_part[i:i + 3][::-1] for i in range(0, len(integer_part), 3)]
    integer_parts.reverse()
    return ",".join(integer_parts) + "." + decimal_part


def convert_string_to_list(signal_text, pattern):
    result_list = []

    match = re.search(pattern, signal_text)
    if match:
        stripped_result_list_numbered_list = re.findall(r"\d\)\s*\d+.?\d*", match.group())
        for result_numbered_item in stripped_result_list_numbered_list:
            stripped_result_match = re.search(r"\)\s*\d+.?\d*", result_numbered_item)
            result_list.append(stripped_result_match.group().replace(")", "").replace(" ", ""))
        return result_list
    else:
        return False


def get_pair_precision(pair, exchange):
    pair_precision_dict = {}
    with open('./precision.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            pair_name = row[0]
            if pair_name != "PAIR":
                pair_precision_dict[pair_name] = {
                    "binance": row[1],
                    "bybit": row[2],
                    "bitget": row[3]
                }

    return int(pair_precision_dict[pair][exchange])


class RegexPatterns:
    class Regular:
        @staticmethod
        def symbol(signal_text):
            pattern = r"#\w+\/\w+"
            match = re.search(pattern, signal_text)

            if match:
                return match.group().replace("#", "").replace("/", "").upper() + " Perpetual"
            else:
                return False

        @staticmethod
        def signal_type(signal_text):
            pattern = r"signal\stype:\s*\w*\s*\(\w+\)"

            match = re.search(pattern, signal_text)
            if match:
                match = re.search(r"\(\w+\)", match.group())
                if match:
                    return match.group().replace("(", "").replace(")", "")
                else:
                    return False
            else:
                return False

        @staticmethod
        def leverage(signal_text):
            pattern = r"leverage:\s*\w*\s*\(\d*\.?\d*"

            match = re.search(pattern, signal_text)
            if match:
                match = re.search(r"\(\d*\.?", match.group())
                return match.group().replace(".", "").replace("(", "")
            else:
                return False

        @staticmethod
        def entry(signal_text):
            pattern = r"entry\stargets:\n(\d*\s*\)\s\d+.*\d*\n)*\n*take"
            return convert_string_to_list(signal_text, pattern)

        @staticmethod
        def targets(signal_text):
            pattern = r"take-profit\stargets:\n(\d*\s*\)\s*\d+.*\d*\n)*\n*stop"
            return convert_string_to_list(signal_text, pattern)

        @staticmethod
        def stop(signal_text):
            pattern = r"stop\stargets:\n(\d*\s*\)\s*\d+.*\d*\n)*\n*"
            return convert_string_to_list(signal_text, pattern)

    class Turkish:
        @staticmethod
        def symbol(signal_text):
            pattern = r"#\w+\/\w+"
            match = re.search(pattern, signal_text)

            if match:
                return match.group().replace("#", "").replace("/", "").upper() + " Perpetual"
            else:
                return False

        @staticmethod
        def signal_type(signal_text):
            pattern = r"usdt\s*#\w*"

            match = re.search(pattern, signal_text)
            if match:
                found_string = match.group().replace("(", "").replace(")", "")
                if found_string.endswith("short"):
                    return "short"
                else:
                    return "long"

        @staticmethod
        def leverage(signal_text):

            pattern = r"kaldıraç:\s*\d*"

            match = re.search(pattern, signal_text)
            if match:
                found_string = match.group().replace("kaldıraç:", "").strip()
                return found_string
            else:
                return False

        @staticmethod
        def entry(signal_text):
            pattern = r"iriş:\s*\n(\d*\s*\)\s*\d*.\d*\n)*"
            return convert_string_to_list(signal_text, pattern)

        @staticmethod
        def targets(signal_text):
            pattern = r"edefler:\s*\n(\d*\s*\)\s*\d*.\d*\n)*"
            return convert_string_to_list(signal_text, pattern)

        @staticmethod
        def stop(signal_text):
            pattern = r"top:\s*\n(\d*\s*\)\s*\d*.\d*\n*)*"
            return convert_string_to_list(signal_text, pattern)


saved_setups = {
    "binance": {
        "Cryptolovers": {
            "qr": "binance_1",
            "referral": "936746824"
        },
        "CAN 1": {
            "qr": "binance_2",
            "referral": "632646513"
        },
        "CAN 2": {
            "qr": "binance_6",
            "referral": "309763251"
        },
        "Mentally": {
            "qr": "binance_4",
            "referral": "963258139"
        },
        "Bbland": {
            "qr": "binance_5",
            "referral": "697429381"
        },
        "Paid": {
            "qr": "binance_4",
            "referral": "589264387"
        },
        "Turk": {
            "qr": "binance_3",
            "referral": "834236982"
        },
    },
    "bybit": {
        "ByBit QR1": {
            "qr": "bybit_1",
            "referral": "NKE6GL"
        },
        "ByBit QR2": {
            "qr": "bybit_2",
            "referral": "HRB7WN"
        },
        "ByBit QR3": {
            "qr": "binance_3",
            "referral": "SOV2XR"
        },
        "ByBit QR4": {
            "qr": "binance_4",
            "referral": "WMT6QJ"
        }
    },
    "bitget": {
        "BitGet QR1": {
            "qr": "bitget_1",
            "referral": "NKE6GL"
        },
        "BitGet QR2": {
            "qr": "bitget_2",
            "referral": "HRB7WN"
        },
        "BitGet QR3": {
            "qr": "bitget_3",
            "referral": "SOV2XR"
        },
        "BitGet QR4": {
            "qr": "bitget_4",
            "referral": "WMT6QJ"
        }
    }
}
