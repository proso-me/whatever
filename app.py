import uuid

from flask import Flask, jsonify
from flask_pydantic import validate
from pydantic import ValidationError, BaseModel, EmailStr, Field


app = Flask(__name__)


@app.route('/health-check/')
def health_check():
    return 'OK'


@app.errorhandler(ValidationError)
def handle_validation_exception(error):
    response = jsonify(error.erorrs())
    response.status_code = 400
    return response


class Blog(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    author: EmailStr
    title: str
    content: str


@app.route('/create-blog/', methods=["POST"])
@validate()
def create_blog(body: Blog):
    return body


if __name__ == '__main__':
    app.run()

