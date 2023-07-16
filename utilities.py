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
                    "bybit": row[2]
                }

    return pair_precision_dict[pair][exchange]


class RegexPatterns:
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
