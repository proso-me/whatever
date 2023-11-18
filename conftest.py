from secrets import randbelow

import pytest


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
