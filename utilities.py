import re


async def send_message(context, update, message_text, keyboard=None, is_callback_query=False):
    chat_id = update.callback_query.message.chat_id if is_callback_query else update.message.chat_id
    await context.bot.send_message(chat_id=chat_id, text=message_text,
                                   reply_markup=keyboard)


def convert_string_to_list(signal_text, pattern):
    result_list = []

    match = re.search(pattern, signal_text)
    if match:
        stripped_result_list_numbered_list = re.findall(r"\d\)\s*\d+.?\d*", match.group())
        for result_numbered_item in stripped_result_list_numbered_list:
            stripped_result_match = re.search(r"\)\s*\d+.?\d*", result_numbered_item)
            result_list.append(float(stripped_result_match.group().replace(")", "").replace(" ", "")))
        return result_list
    else:
        return False



class RegexPatterns:
    @staticmethod
    def symbol(signal_text):
        pattern = r"#\w+\/\w+"
        match = re.search(pattern, signal_text)

        if match:
            return match.group().replace("#", "").upper()
        else:
            return False

    @staticmethod
    def signal_type(signal_text):
        pattern = r"signal\stype:\s*\w*\s*\(\w+\)"

        match = re.search(pattern, signal_text)
        if match:
            match = re.search(r"\(\w+\)", match.group())
            if match:
                return match.group().replace("(", "").replace(")", "").upper()
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
            return int(match.group().replace(".", "").replace("(", ""))
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
