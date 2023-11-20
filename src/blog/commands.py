from pydantic import BaseModel, EmailStr

from src.blog.models import NotFound, Article


class AlreadyExists(Exception):
    pass


class CreateArticleCommand(BaseModel):
    author: EmailStr
    title: str
    content: str

    def execute(self):
        try:
            Article.get_by_title(self.title)
            raise AlreadyExists
        except NotFound:
            pass

        article = Article(
            author=self.author,
            title=self.title,
            content=self.content
        ).save()

        return article
