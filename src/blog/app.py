from flask import Flask, jsonify, request
from pydantic import ValidationError

from src.blog.commands import CreateArticleCommand
from src.blog.queries import GetArticleByIDQuery, ListArticlesQuery

app = Flask(__name__)


@app.errorhandler(ValidationError)
def validation_error(e):
    return jsonify(e.errors()), 400


@app.route("/create-article/", methods=["POST"])
def create_article():
    cmd = CreateArticleCommand(
        **request.json
    )
    return jsonify(dict(cmd.execute()))


@app.route("/list-articles/", methods=["GET"])
def list_articles():
    articles = ListArticlesQuery()
    return jsonify([dict(el) for el in articles.execute()])


@app.route("/article/<article_id>/", methods=["GET"])
def get_article_by_id(article_id):
    article_query = GetArticleByIDQuery(id=article_id)
    return jsonify(dict(article_query.execute()))


if __name__ == "__main__":
    app.run()
