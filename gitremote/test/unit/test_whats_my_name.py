import pytest

from whats_my_name import my_name_is


def test_my_name_is():
    assert "lee" == my_name_is()