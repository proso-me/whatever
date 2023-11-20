from typing import List

from pydantic import BaseModel

from src.blog.models import Article


class ListArticlesQuery(BaseModel):
    @staticmethod
    def execute() -> List[Article]:
        articles = Article.get_list()

        return articles


class GetArticleByIDQuery(BaseModel):
    id: str

    def execute(self) -> Article:
        article = Article.get_by_id(self.id)

        return article
