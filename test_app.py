import pytest
import json

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_METHODS'] = []

    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/health-check/')

    assert response.status_code == 200


def test_create_blog_bad_request(client):
    """
    GIVEN request data with invalid values or missing attributes
    WHEN endpoint /create-blog/ is called
    THEN it should return status 400 and JSON body
    """
    response = client.post(
        '/create-blog/',
        data=json.dumps({
            'author': 'Oleksiy Gideonov',
            'title': None,
            'content': 'Some extra awesome content'
        }),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert response.json is not None
