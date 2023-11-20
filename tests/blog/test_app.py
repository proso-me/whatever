import json
import pathlib

import pytest
import requests
from jsonschema.validators import Draft4Validator
from referencing import Registry, Resource

from src.blog.app import app
from src.blog.models import Article


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def schemas():
    return ([
        Resource.from_contents(json.loads(schema_file.read_text()))
        for schema_file
        in (pathlib.Path(__file__).parent / "schemas").glob("*.json")
    ] @ Registry()).crawl()


def test_create_article(client, schemas):
    """
    GIVEN Create Article request with valid author, title, content
    WHEN executed
    THEN a new Article must exist in db holding these attrs
    """
    response = client.post("/create-article/", json={
        "author": "a@article.author",
        "title": "article.title",
        "content": "article.content"
    }, content_type="application/json")

    Draft4Validator(schemas.get("usn:article").contents).validate(response.json)


def test_get_article(client, schemas):
    """
    GIVEN Id of article stored in the database
    WHEN endpoint is called
    THEN should return Article in json with format matching schema
    """
    article = Article(
        author="some@some.com",
        title="some",
        content="some",
    ).save()

    response = client.get(f'/article/{article.id}/', content_type="application/json")
    assert response.status_code == 200
    Draft4Validator(schemas.get("usn:article").contents).validate(response.json)


def test_list_articles(client, schemas):
    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article",
    ).save()
    response = client.get("/list-articles/", content_type="application/json")
    # noinspection PyArgumentList
    Draft4Validator(schemas.get("usn:articles_list").contents, registry=schemas).validate(response.json)


@pytest.mark.parametrize(
    "data",
    [{
        "author": "article.author",
        "title": "article.title",
        "content": "article.content",
    }, {
        "author": "article.author",
        "title": "article.title",
    }, {
        "author": "article.author",
        "title": None,
        "content": "article.content",
    }]
)
def test_create_article_invalid(client, data):
    """
    GIVEN Create Article request with invalid author, title, content
    WHEN endpoint create-article is called
    THEN should return 400
    """
    response = client.post("/create-article/", json=data, content_type="application/json")
    assert response.status_code == 400


@pytest.mark.e2e
def test_create_list_get(client):
    requests.post(
        "http://localhost:5000/cre"
    )
