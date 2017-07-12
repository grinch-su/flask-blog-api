from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView


comment = Blueprint('comment', __name__)


class CommentView(MethodView):

    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
    def path(self):
        pass
