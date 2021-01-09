import re


def is_none(value) -> bool:
    return value is None


def empty_or_none_string(value) -> bool:
    return is_none(value) or (str(value).strip() == "")


def not_int(value) -> bool:
    return is_none(value) or not isinstance(value, int)


def not_valid_email(value) -> bool:
    return is_none(value) or not bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", value))
