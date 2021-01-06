def is_none(value) -> bool:
    return value is None


def is_empty_or_none_string(value) -> bool:
    return is_none(value) or (str(value).strip() == "")


def is_not_int(value) -> bool:
    return is_none(value) or not isinstance(value, int)

