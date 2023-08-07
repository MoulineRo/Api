import os

import requests

BASE_URL = os.getenv("API_URL", "https://monoapi-87eea2a4128e.herokuapp.com/")


def test_create_book():
    r = requests.post(
        BASE_URL + "books/",
        json={
            "book": "Create",
            "author": "Allan",
            "price": 1500,
            "quantity": 3,
        },
    )
    assert r.status_code == 200
    response_body = r.json()
    assert "book" in response_body[-1]
    assert "author" in response_body[-1]
    assert "price" in response_body[-1]
    assert "quantity" in response_body[-1]


def test_show_allbooks():
    r = requests.get(BASE_URL + "books/")
    assert r.status_code == 200
    response_body = r.json()
    assert list == type(response_body)

