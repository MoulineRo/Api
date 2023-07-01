import json
import pathlib
import unittest

import responses

root = pathlib.Path(__file__).parent


class TestStringMethods(unittest.TestCase):
    @responses.activate
    def test_books(self):
        mocked_response = json.load(open(root / "fixtures/books.json"))
        responses.get(
            "http://127.0.0.1:8000/books/",
            json=mocked_response,
        )
        assert mocked_response[1]["id"] == 2
        assert mocked_response[1]["book"] == "Napaleon"
        assert mocked_response[1]["author"] == "Mukola"
        assert mocked_response[1]["genre"] == "Drama"
        assert mocked_response[1]["date"] == "2005-12-10"
        assert (
            responses.get(
                "http://127.0.0.1:8000/books/",
                json=mocked_response,
            ).url
            == "http://127.0.0.1:8000/books/"
        )
        assert (
            responses.get(
                "http://127.0.0.1:8000/books/",
                json=mocked_response,
            ).status
            == 200
        )

    @responses.activate
    def test_authors(self):
        mocked_response = json.load(open(root / "fixtures/authors.json"))
        responses.get(
            "http://127.0.0.1:8000/authors/",
            json=mocked_response,
        )
        assert len(mocked_response) == 13
        assert mocked_response[0]["author"] == "Allan"
        assert (
            responses.get(
                "http://127.0.0.1:8000/authors/",
                json=mocked_response,
            ).url
            == "http://127.0.0.1:8000/authors/"
        )
        assert (
            responses.get(
                "http://127.0.0.1:8000/authors/",
                json=mocked_response,
            ).status
            == 200
        )

    @responses.activate
    def test_books_id(self):
        mocked_response = json.load(open(root / "fixtures/books_id.json"))
        responses.get(
            "http://127.0.0.1:8000/books/1/",
            json=mocked_response,
        )
        assert mocked_response[0]["genre"] == "Comedy"
        assert mocked_response[0]["date"] == "1855-12-10"
        assert (
            responses.get(
                "http://127.0.0.1:8000/books/1/",
                json=mocked_response,
            ).url
            == "http://127.0.0.1:8000/books/1/"
        )
        assert (
            responses.get(
                "http://127.0.0.1:8000/books/1/",
                json=mocked_response,
            ).status
            == 200
        )

    @responses.activate
    def test_authors_id(self):
        mocked_response = json.load(open(root / "fixtures/authors_id.json"))
        responses.get(
            "http://127.0.0.1:8000/authors/5/",
            json=mocked_response,
        )
        assert mocked_response[0]["author"] == "Raul Madan"
        assert mocked_response[0]["id"] == 5
        assert (
            responses.get(
                "http://127.0.0.1:8000/authors/5/",
                json=mocked_response,
            ).url
            == "http://127.0.0.1:8000/authors/5/"
        )
        assert (
            responses.get(
                "http://127.0.0.1:8000/authors/5/",
                json=mocked_response,
            ).status
            == 200
        )
