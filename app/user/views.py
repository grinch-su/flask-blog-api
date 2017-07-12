from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView
from app.user.models import User

user = Blueprint('user', __name__)


class UserView(MethodView):

    def get(self):
        pass
    def post(self):
        pass
    def put(self):
        pass
    def delete(self):
        pass
    def patch(self):
        pass
