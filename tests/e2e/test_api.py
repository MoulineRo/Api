import requests


def test_create_book():
    r = requests.post(
        "http://127.0.0.1:8000/api/v2/books/",
        json={
            "book": "Create",
            "author": "Allan",
            "genre": "Comedy",
            "date": "1855-12-10",
        },
    )
    assert r.status_code == 200
    response_body = r.json()
    assert "book" in response_body[-1]
    assert "author" in response_body[-1]
    assert "genre" in response_body[-1]
    assert "date" in response_body[-1]


def test_show_allbooks():
    r = requests.get("http://127.0.0.1:8000/api/v2/books/")
    assert r.status_code == 200
    response_body = r.json()
    assert list == type(response_body)


def test_show_book_id(id=1):
    r = requests.get(f"http://127.0.0.1:8000/api/v2/books/{id}")
    assert r.status_code == 200
    response_body = r.json()
    assert "id" in response_body
    assert "book" in response_body
    assert "author" in response_body
    assert "genre" in response_body
    assert "date" in response_body


def test_update_book_id(id=4):
    r = requests.put(
        f"http://127.0.0.1:8000/api/v2/books/{id}/",
        json={
            "book": "Updated",
            "author": "Allan",
            "genre": "Comedy",
            "date": "1855-12-10",
        },
    )
    assert r.status_code == 200
    response_body = r.json()
    assert "id" in response_body
    assert "book" in response_body
    assert "author" in response_body
    assert "genre" in response_body
    assert "date" in response_body


def test_delete_book_id(id=41):
    r = requests.delete(f"http://127.0.0.1:8000/api/v2/books/{id}/")
    assert r.status_code == 200
    response_body = r.json()
    assert list == type(response_body)


def test_show_allauthors():
    r = requests.get("http://127.0.0.1:8000/api/v2/authors/")
    assert r.status_code == 200
    response_body = r.json()
    assert list == type(response_body)


def test_show_author_id(id=9):
    r = requests.get(f"http://127.0.0.1:8000/api/v2/authors/{id}/")
    assert r.status_code == 200
    response_body = r.json()
    assert "id" in response_body
    assert "book" in response_body
    assert "author" in response_body
    assert "genre" in response_body
    assert "date" in response_body
