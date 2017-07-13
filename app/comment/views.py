from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView


comment = Blueprint('comment', __name__, url_prefix='/api')


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


comment_view = CommentView.as_view('comment_view')

comment.add_url_rule('/comments/',
                     view_func=comment_view,
                     methods=['GET'])
comment.add_url_rule('/comments/article=<int:id>',
                     view_func=comment_view,
                     methods=['GET'])
comment.add_url_rule('/comment/article=<int:article_id>/user=<int:user_id>',
                     view_func=comment_view,
                     methods=['POST', 'PUT', 'DELETE'])
comment.add_url_rule('/comment/article=<int:id>/user=<int:user_id>&to_user=<int:to_user_id>',
                     view_func=comment_view,
                     methods=['POST', 'PUT', 'DELETE'])
