import re
import csv
import random
import os


async def send_message(
    context, update, message_text, keyboard=None, is_callback_query=False
):
    chat_id = (
        update.callback_query.message.chat_id
        if is_callback_query
        else update.message.chat_id
    )
    await context.bot.send_message(
        chat_id=chat_id, text=message_text, reply_markup=keyboard
    )


def separate_number(number):
    number_str = str(number)
    split_number = number_str.split(".")
    if len(split_number) > 1:
        integer_part, decimal_part = split_number
        integer_part = integer_part[::-1]
        integer_parts = [
            integer_part[i : i + 3][::-1] for i in range(0, len(integer_part), 3)
        ]
        integer_parts.reverse()
        return ",".join(integer_parts) + "." + decimal_part
    else:
        integer_part = number_str
        integer_part = integer_part[::-1]
        integer_parts = [
            integer_part[i : i + 3][::-1] for i in range(0, len(integer_part), 3)
        ]
        integer_parts.reverse()
        return ",".join(integer_parts)


def convert_string_to_list(signal_text, pattern):
    result_list = []

    match = re.search(pattern, signal_text)
    if match:
        stripped_result_list_numbered_list = re.findall(
            r"\d\)\s*\d+.?\d*", match.group()
        )
        for result_numbered_item in stripped_result_list_numbered_list:
            stripped_result_match = re.search(r"\)\s*\d+.?\d*", result_numbered_item)
            result_list.append(
                stripped_result_match.group().replace(")", "").replace(" ", "")
            )
        return result_list
    else:
        return False


def get_pair_precision(pair, exchange):
    pair_precision_dict = {}
    with open("./precision.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            pair_name = row[0]
            if pair_name != "PAIR":
                pair_precision_dict[pair_name] = {
                    "binance": row[1],
                    "bybit": row[2],
                    "bitget": row[3],
                    "mexc": row[4],
                    "bingx": row[5],
                }

    if pair_precision_dict[pair][exchange]:
        return int(pair_precision_dict[pair][exchange])
    else:
        return None


class RegexPatterns:
    class Regular:
        @staticmethod
        def symbol(signal_text):
            pattern = r"#\w+\/\w+"
            match = re.search(pattern, signal_text)

            if match:
                return (
                    match.group().replace("#", "").replace("/", "").upper()
                    + " Perpetual"
                )
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
                return (
                    match.group().replace("#", "").replace("/", "").upper()
                    + " Perpetual"
                )
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
        "Board Main": {
            "qr": "binance_1",
            "referral": "237419134",
            "username": "User-89p2j",
        },
        "Board Free": {
            "qr": "binance_1",
            "referral": "928356471",
            "username": "User-89p2j",
        },
        "CAN Main": {
            "qr": "binance_2",
            "referral": "986438986",
            "username": "User-33c8d",
        },
        "Turk Main": {
            "qr": "binance_3",
            "referral": "39164953",
            "username": "User-27c4m",
        },
        "CAN Free": {
            "qr": "binance_6",
            "referral": "92435420",
            "username": "User-28c7w",
        },
        "Turk Free": {
            "qr": "binance_4",
            "referral": "891972154",
            "username": "User-64q9n",
        },
        "Extra 1": {
            "qr": "binance_7",
            "referral": "9746251829",
            "username": "User-27c4m",
        },
        "Extra 2": {
            "qr": "binance_8",
            "referral": "8463691712",
            "username": "User-34o2r",
        },
    },
    "bybit": {
        "CAN Main": {"qr": "bybit_1", "referral": "3YML5X"},
        "CAN Free": {"qr": "bybit_1", "referral": "6KXM2L"},
        "Turk Main": {"qr": "bybit_1", "referral": "4RST3K"},
        "Turk Free": {"qr": "bybit_1", "referral": "8TWN9E"},
    },
    "bitget": {
        "CAN Main": {
            "qr": "bitget_2",
            "referral": "1HN38KYX",
            "username": "BGUSER-1HN38KYX",
        },
        "CAN Free": {
            "qr": "bitget_3",
            "referral": "1KM84HWR",
            "username": "BGUSER-1KM84HWR",
        },
        "Turk Main": {
            "qr": "bitget_3",
            "referral": "1WC67QCZ",
            "username": "BGUSER-1WC67QCZ",
        },
        "Turk Free": {
            "qr": "bitget_2",
            "referral": "3VH98ACX",
            "username": "BGUSER-3VH98ACX",
        },
        "Board Main": {
            "qr": "bitget_1",
            "referral": "2BI76BMK",
            "username": "BGUSER-2BI76BMK",
        },
        "Board Free": {
            "qr": "bitget_1",
            "referral": "8LR12MLD",
            "username": "BGUSER-8LR12MLD",
        },
    },
    "mexc": {
        "Board Main": {"qr": "binance_1", "referral": "69r4f"},
        "CAN Main": {"qr": "binance_2", "referral": "34n5e"},
        "CAN Free": {"qr": "binance_6", "referral": "46k7u"},
        "Turk Free": {"qr": "binance_4", "referral": "53h6r"},
        "Board Free": {"qr": "binance_5", "referral": "67x8w"},
        "Extra 1": {"qr": "binance_4", "referral": "79g2q"},
        "Turk Main": {"qr": "binance_3", "referral": "58r3m"},
    },
    "bingx": {
        "CAN Main": {"qr": "bitget_1", "referral": "NKE6GL"},
        "CAN Free": {"qr": "bitget_2", "referral": "HRB7WN"},
        "Turk Main": {"qr": "bitget_3", "referral": "SOV2XR"},
        "Turk Free": {"qr": "bitget_4", "referral": "WMT6QJ"},
    },
    "okx": {"CAN Main": {"qr": "okx_1", "referral": "92843725"}},
    "lbank": {
        "CAN Main": {"qr": "lbank_1", "referral": "3MG8F"},
        "CAN Free": {"qr": "lbank_1", "referral": "5KN7R"},
        "Turk Main": {"qr": "lbank_1", "referral": "9LS6N"},
        "Turk Free": {"qr": "lbank_1", "referral": "7NT9L"},
        "Board Main": {"qr": "lbank_1", "referral": "2SH6L"},
        "Board Free": {"qr": "lbank_1", "referral": "3CL4A"},
    },
}


def random_referral(exchange):
    def range_char(start, stop):
        return [chr(n) for n in range(ord(start), ord(stop) + 1)]

    if exchange == "binance":
        char_set_1 = range_char("1", "9")
        char_set_2 = range_char("0", "9")

        return "".join(random.sample(char_set_1, 1) + random.sample(char_set_2, 8))

    elif exchange == "bybit":
        char_set = range_char("A", "Z") + range_char("0", "9")
        return "".join(random.sample(char_set, 6))

    elif exchange == "bitget":
        char_set = range_char("A", "Z") + range_char("a", "z") + range_char("0", "9")
        string_1 = "".join(random.sample(char_set, 4))
        string_2 = "".join(random.sample(char_set, 4))
        return f"0x{string_1}......{string_2}"

    elif exchange == "mexc":
        char_set = range_char("A", "Z") + range_char("a", "z") + range_char("0", "9")
        return "".join(random.sample(char_set, 5))

    elif exchange == "bingx":
        char_set = range_char("A", "Z")
        return "".join(random.sample(char_set, 6))

    elif exchange == "okx":
        char_set = range_char("0", "9")
        return "".join(random.sample(char_set, 8))

    elif exchange == "lbank":
        char_set = range_char("A", "Z") + range_char("0", "9")
        return "".join(random.sample(char_set, 5))


def random_qr(exchange):
    qrs = []
    for filename in os.listdir("./qr/"):
        if filename.startswith(exchange):
            qrs.append(filename.replace(".png", ""))

    return random.sample(qrs, 1)[0]
