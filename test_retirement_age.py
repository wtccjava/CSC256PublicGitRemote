import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from FullRetirementAge import *
from FullRetirementAge import _validate_birth_year, _validate_birth_month, _validate_age_year, _validate_age_month

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'birthYear': int,
    'birthMonth': int,
    'retireAge': int,
    'retireMonth': int,
    'resultYear': int,
    'resultMonth': int,
}

scenarios('../features/retirement_age.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('the birth year entered is "{birthYear:Number}"', extra_types=EXTRA_TYPES))
@given('the birth year entered is "<birthYear>"')
def birth_year(birthYear):
    birthYear = _validate_birth_year(birthYear)
    return birthYear


@when(parsers.cfparse('the birth month entered is "{birthMonth:Number}"', extra_types=EXTRA_TYPES))
@when('the birth month entered is "<birthMonth>"')
def birth_month(birthMonth):
    birthMonth = _validate_birth_month(birthMonth)
    return birthMonth


@when(parsers.cfparse('the retirement age is "{retireAge:Number}"', extra_types=EXTRA_TYPES))
@when('the retirement age is "<retireAge>"')
def retirement_age(retireAge):
    retireAge = _validate_age_year(retireAge)
    return retireAge


@when(parsers.cfparse('the retirement month is "{retireMonth:Number}"', extra_types=EXTRA_TYPES))
@when('the retirement month is "<retireMonth>"')
def retirement_month(retireMonth):
    retireMonth = _validate_age_month(retireMonth)
    return retireMonth


@then(parsers.cfparse('the retirement date is "{resultYear:Number}" years and "{resultMonth:Number}" months', extra_types=EXTRA_TYPES))
@then('the retirement date is "<resultYear>" years and "<resultMonth>" months')
def result(resultYear, resultMonth):
    age_nums = (int(resultYear), int(resultMonth))
    assert calculate_retirement_date(birth_year, birth_month, retirement_age, retirement_month) == age_nums


def test_1():
    pass


@given("the value entered is a number")
def year_is_number():
    pass


@when('the year entered is "1900"')
def year_input():
    return calculate_retirement_age(1900)


@then('the retirement age is "65, 0"')
def result(year_input):
    assert year_input == 65, 0


def test_2():
    pass


@when('the year entered is "1899"')
def year_input2():
    return calculate_retirement_age(1899)


@then('the result is a "ValueError"')
def result(year_input2):
    with pytest.raises(ValueError):
        assert year_input2 == 65, 0


def test_3():
    pass


@when('the year entered is "2019"')
def year_input3():
    return calculate_retirement_age(2019)


@then('the retirement age is "67, 0"')
def result(year_input3):
    assert year_input3 == 67, 0


def test_4():
    pass


@when('the year entered is "2020"')
def year_input4():
    return calculate_retirement_age(2020)


@then('the result is a "ValueError"')
def result(year_input4):
    with pytest.raises(ValueError):
        assert year_input4 == 67, 0
