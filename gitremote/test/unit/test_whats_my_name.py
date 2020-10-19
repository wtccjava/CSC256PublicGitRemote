import pytest

from CSC256PublicGitRemote.gitremote.whats_my_name import my_name_is


def test_my_name_is():
    assert "Stavros Bannoura" == my_name_is()
