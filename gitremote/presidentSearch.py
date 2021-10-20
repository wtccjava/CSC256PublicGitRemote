import requests

import pytest
import sys


url2 = 'https://api.duckduckgo.com/?q=presidents%20of%20the%20united%20states&format=json&pretty=1'

def test_ddg0():

    response2 = requests.get(url2)
    rsp_data = response2.json()
    assert "Lincoln" in rsp_data['RelatedTopics'][0]['Text']