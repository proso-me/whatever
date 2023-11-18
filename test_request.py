from secrets import randbelow
from unittest import mock
import pytest

import requests
from requests import Response


def get_my_ip():
    response = requests.get(
        'https://ipinfo.io/json'
    )
    return response.json().get('ip')


@pytest.fixture
def ipv4address():
    """
    Generates a random ipv4 address.
    """
    class IPv4AddrFactory:
        """Generates random ipv4 addresses."""
        @staticmethod
        def get():
            """Return an ipv4 address."""
            ipaddr = f"{randbelow(255) + 1}."
            f"{randbelow(255) + 1}."
            f"{randbelow(255) + 1}."
            f"{randbelow(255) + 1}"
            return ipaddr
    return IPv4AddrFactory()


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
