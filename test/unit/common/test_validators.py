from src.common.validators import empty_or_none_string, not_int


def test__is_empty_or_none_string__pass_none__return_true():
    assert empty_or_none_string(None) is True


def test__is_empty_or_none_string__pass_empty_string__return_true():
    assert empty_or_none_string("") is True
    assert empty_or_none_string("  ") is True


def test__is_not_int__pass_none__return_true():
    assert not_int(None) is True


def test__is_not_int__pass_float__return_true():
    assert not_int(1.02) is True


def test__is_not_int__pass_valid_int__return_false():
    assert not_int(3) is False


