import pytest

from CSC256PublicGitRemotefork.gitremote.whats_my_name import my_name_is

def test_my_name_is():
    assert "Jacob" == my_name_is()