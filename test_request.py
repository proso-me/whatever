from unittest import mock

import requests
from requests import Response


def get_my_ip():
    response = requests.get(
        'http://ipinfo.io/json'
    )
    return response.json().get('ip')


def test_get_my_ip(monkeypatch):
    my_ip = '123.123.123.123'
    response = mock.create_autospec(Response)
    response.json.return_value = {'ip': my_ip}

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: response
    )

    assert get_my_ip() == my_ip

