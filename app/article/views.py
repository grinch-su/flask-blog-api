from datetime import datetime

from flask import Blueprint, abort, jsonify, request
from flask.views import MethodView

from app import db, app
from app.article.models import Article

article = Blueprint('article', __name__)

class ArticleView(MethodView):
    def get(self, id=None, page=1):

        if not id:
            articles = Article.query.paginate(page, 10).items
            res = {}
            for al in articles:
                res[al.id] = {
                    'title': al.title,
                    'content': al.content,
                    'timestamp': al.timestamp,
                    'edit_date': al.edit_date
                }
            return jsonify(posts=res)
        else:
            al = Article.query.get(id=id)
            if not al:
                abort(404)
            res = {
                'title': al.title,
                'content': al.content,
                'timestamp': al.timestamp,
                'edit_date': al.edit_date
            }
            return jsonify(article=res)


    def post(self):
        title = request.get_json()["title"]
        content = request.get_json()["content"]
        post = Article(title=title, content=content)
        curr_session = db.session
        try:
            curr_session.add(post)
            curr_session.commit()
        except:
            curr_session.rollback()
            curr_session.flush()
        
        postId = post.id
        data = Article.query.filter_by(id=postId).first()
        return jsonify(post=data.to_json())


    def put(self, id=None):
        global post
        title = request.get_json()["title"]
        content = request.get_json()["content"]
        curr_session = db.session
        try:
            post = Article.query.filter_by(id=id).first()
            post.title = title
            post.content = content
            post.edit_date = datetime.now()
            curr_session.commit()
        except:
            curr_session.rollback()
            curr_session.flush()
            return jsonify(message='No post found')
        postId = post.id
        data = Article.query.filter_by(id=postId).first()

        return jsonify(post=data.to_json())


    def delete(self, id=None):
        curr_session = db.session
        Article.query.filter_by(id=id).delete()
        curr_session.commit()
        return self.get()

article_view = ArticleView.as_view('article_view')
app.add_url_rule(
    '/article/', view_func=article_view, methods=['GET','POST']
)
app.add_url_rule(
    '/article/<int:id>', view_func=article_view, methods=['GET','PUT','DELETE']
)