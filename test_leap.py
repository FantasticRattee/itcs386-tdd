import pytest

from leap import is_leap

def test_2024_is_a_leap_year():
    assert is_leap(2024)


def test_1900_is_not_a_leap_year():
    assert not is_leap(1900)#Space before 'assert'




@pytest.mark.parametrize("year, expected", [
    (2000, True),   # หาร 400 ลงตัว
    (1900, False),  # หาร 100 ลงตัว แต่หาร 400 ไม่ลงตัว
    (2024, True),   # หาร 4 ลงตัว แต่หาร 100 ไม่ลงตัว
    (2023, False),  # หาร 4 ไม่ลงตัว
    (2028, True),   # Additional case: divisible by 4 but not by 100
    (2100, False),  # Additional case: divisible by 100 but not by 400
])
def test_is_leap(year, expected):
    assert is_leap(year) == expected



def test_year_zero_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(0)


def test_negative_year_is_rejected():
    with pytest.raises(ValueError, match="1 or later"):
        is_leap(-1)
