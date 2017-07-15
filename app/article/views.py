from datetime import datetime

from flask import Blueprint, abort, jsonify, request
from flask.views import MethodView

from app import db, app
from app.article.models import Article, Language

article = Blueprint('article', __name__)

class ArticleView(MethodView):
    def get(self, id=None, page=1):

        if not id:
            articles = Article.query.paginate(page, 10).items
            res = []
            for article in articles:
                res.append(article.to_json())
            return jsonify(articles=res)
        else:
            al = Article.query.get(id)
            if not al:
                abort(404)
            return jsonify(article=al.to_json())


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
        article = Article.query.filter_by(id=postId).first()
        res = {
                'title': article.title,
                'content': article.content,
                'timestamp': article.timestamp,
                'edit_date': article.edit_date
            }
        return jsonify(article=res)


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


class LangView(MethodView):
    def get(self, name=None):
        if not name:
            languages = Language.query.all()
            res = []
            for lang in languages:
                res.append(lang.to_json())
            return jsonify(languages=res)
        else:
            lang = Language.query.filter_by(name=name).first()
            if not lang:
                abort(404)
            return jsonify(language=lang.to_json())

    def post(self):
        name = request.get_json()["name"]
        lang = Language(name=name)
        curr_session = db.session
        try:
            curr_session.add(lang)
            curr_session.commit()
        except:
            curr_session.rollback()
            curr_session.flush()
        
        langId = lang.id
        res = None
        return jsonify(article=res)
    
    def put(self):
        pass
    
    def delete(self):
        pass

article_view = ArticleView.as_view('article_view')
lang_view = LangView.as_view('lang_view')

# articles
app.add_url_rule(
    '/articles/', view_func=article_view, methods=['GET','POST']
)
app.add_url_rule(
    '/articles/page=<int:page>', view_func=article_view, methods=['GET']
)
app.add_url_rule(
    '/article/<int:id>', view_func=article_view, methods=['GET','PUT','DELETE']
)

# languages
app.add_url_rule(
    '/lang/', view_func=lang_view, methods=['GET','POST']
)
app.add_url_rule(
    '/lang/<name>', view_func=lang_view, methods=['GET','PUT']
)
