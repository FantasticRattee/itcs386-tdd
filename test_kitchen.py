# Test list (worksheet Part A):
# [x] 200 g x 3 = 600 g
# [x] multiplying a quantity does not modify the original
# [x] two quantities with the same amount and unit are equal
# [x] 1 oz is not the same as 1 g
# [x] scaling preserves ounces as well as grams
# [x] 200 g + 300 g = 500 g
# [x] plus retains both operands in an unevaluated Sum
# [ ] 200 g + 1 oz, reduced to grams, using a conversion rate
# [ ] (200 g + 1 oz) x 2 (optional A8)

from kitchen import Converter, Quantity, grams, ounces


def test_multiplication():
    flour = grams(200)
    assert flour.times(3) == grams(600)


def test_multiplication_returns_a_new_quantity():
    flour = grams(200)
    tripled = flour.times(3)
    assert tripled == grams(600)
    assert flour.times(2) == grams(400)
    assert flour == grams(200)
    assert tripled is not flour


def test_equality():
    assert grams(200) == grams(200)
    assert grams(200) != grams(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_multiplication_preserves_unit():
    assert ounces(2).times(3) == ounces(6)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)


def test_plus_returns_an_unevaluated_sum():
    from kitchen import Sum

    left = grams(200)
    right = grams(300)
    total = left.plus(right)
    assert isinstance(total, Sum)
    assert total.left is left
    assert total.right is right
