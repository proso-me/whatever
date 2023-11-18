from unittest import mock

import requests
from requests import Response


def get_my_ip():
    response = requests.get(
        'https://ipinfo.io/json'
    )
    return response.json().get('ip')


def test_get_my_ip(monkeypatch, ipv4address):
    my_ip = ipv4address
    response = mock.create_autospec(Response)
    response.json.return_value = {'ip': my_ip}

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: response
    )

    assert get_my_ip() == my_ip
