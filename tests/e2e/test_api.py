import os

import requests

BASE_URL = os.getenv("API_URL", "https://monoapi-87eea2a4128e.herokuapp.com/")


def test_show_allbooks():
    r = requests.get(BASE_URL + "books/")
    assert r.status_code == 200
    response_body = r.json()
    assert list == type(response_body)

