import os
import random
import tempfile

import pytest

from src.blog.models import Article


@pytest.fixture
def random_name():
    return random.choice(["A", "B", "C"])


def test_fixture_usage(random_name):
    assert random_name


@pytest.fixture(autouse=True)
def database():
    _, filename = tempfile.mkstemp()
    os.environ['WEVER_DB_NAME'] = filename
    Article.create_table(database_name=filename)
    yield
    os.unlink(filename)
