import pytest

from gitremote.whats_my_name import my_name_is


def test_my_name_is():
    assert "John the Baptist" == my_name_is()
