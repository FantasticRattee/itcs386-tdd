import pytest

from shipping import shipping_fee


# Rule 1: zero is invalid too; the original '< 0' guard accepts it.
@pytest.mark.parametrize("weight_kg", [-1, -0.1, 0])
def test_nonpositive_weight_is_rejected(weight_kg):
    with pytest.raises(ValueError, match="more than 0 kg"):
        shipping_fee(weight_kg)


# Rule 2: exactly 1 kg belongs to the 40-baht block, not the 60-baht block.
@pytest.mark.parametrize("weight_kg, expected", [(0.1, 40), (0.5, 40), (1, 40)])
def test_up_to_one_kilogram_costs_forty(weight_kg, expected):
    assert shipping_fee(weight_kg) == expected


# Rule 3: test the interior and both sides of this block's boundaries.
@pytest.mark.parametrize("weight_kg, expected", [(1.0001, 60), (3, 60), (5, 60)])
def test_over_one_up_to_five_kilograms_costs_sixty(weight_kg, expected):
    assert shipping_fee(weight_kg) == expected


# Rule 4: every started extra kilogram is charged; int() truncates fractions.
@pytest.mark.parametrize("weight_kg, expected", [
    (5.2, 70),
    (6, 70),
    (6.1, 80),
    (7, 80),
    (10.5, 120),
])
def test_started_kilograms_above_five_are_rounded_up(weight_kg, expected):
    assert shipping_fee(weight_kg) == expected
