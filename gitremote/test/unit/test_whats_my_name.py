import pytest

from gitremote.whats_my_sjhale import my_name_is


def test_my_name_is():
    assert "bob" == my_name_is()