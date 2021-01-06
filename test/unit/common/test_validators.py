from src.common.validators import is_empty_or_none_string, is_not_int


def test__is_empty_or_none_string__pass_none__return_true():
    assert is_empty_or_none_string(None) == True


def test__is_empty_or_none_string__pass_empty_string__return_true():
    assert is_empty_or_none_string("") == True
    assert is_empty_or_none_string("  ") == True


def test__is_not_int__pass_none__return_true():
    assert is_not_int(None) == True


def test__is_not_int__pass_float__return_true():
    assert is_not_int(1.02) == True


def test__is_not_int__pass_valid_int__return_false():
    assert is_not_int(3) == False


