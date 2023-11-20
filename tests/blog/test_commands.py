import pytest

from src.blog.commands import AlreadyExists, CreateArticleCommand
from src.blog.models import Article


def test_create_article():
    """
    GIVEN Create Article Command with valid author, title, content
    WHEN executed
    THEN a new Article must exist in db holding these attrs
    """
    cmd = CreateArticleCommand(
        author="some@some.com",
        title="some",
        content="some",
    )
    article = cmd.execute()

    db_article = Article.get_by_id(article.id)

    assert db_article.id == article.id
    assert db_article.author == article.author
    assert db_article.title == article.title
    assert db_article.content == article.content


def test_create_article_already_exists():
    """
    GIVEN CreateArticleCommand with a title of some article in database
    WHEN the execute method is called
    THEN the AlreadyExists exception must be raised
    """

    Article(
        author="jane@doe.com",
        title="New Article",
        content="Super extra awesome article",
    ).save()

    cmd = CreateArticleCommand(
        author="john@doe.com", title="New Article", content="Super awesome article"
    )

    with pytest.raises(AlreadyExists):
        cmd.execute()