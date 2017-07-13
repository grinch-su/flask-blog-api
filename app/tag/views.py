from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView

from app import db
from app.tag.models import Tag

tag = Blueprint('tag', __name__, url_prefix='/api')


class TagView(MethodView):
    def get(self, name=None):
        if not name:
            tags = Tag.query.all()
            res = []
            for tag in tags:
                res.append(tag.to_json())
            return jsonify(tags=res)
        else:
            tag = Tag.query.filter_by().first_or_404()
            return jsonify(tag=tag.to_json())

    def post(self):
        name = request.get_json()["name"]
        tag = Tag(name=name)
        db.session.add(tag)
        db.session.commit()
        return jsonify(language=tag.to_json())

    def put(self, name=None):
        data_name = request.get_json()["name"]
        tag = Tag.query.filter_by(name=name).first_or_404()
        tag.name = data_name
        db.session.commit()
        return jsonify(language=tag.to_json())

    def delete(self, name=None):
        Tag.query.filter_by(name=name).delete()
        db.session.commit()
        return self.get()

tag_view = TagView.as_view('tag_view')

tag.add_url_rule('/tags/', view_func=tag_view, methods=['GET'])
tag.add_url_rule('/tag/<name>', view_func=tag_view, methods=['GET', 'DELETE', 'POST', 'PUT'])
