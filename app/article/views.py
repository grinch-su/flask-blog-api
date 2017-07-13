from datetime import datetime

from flask import Blueprint, abort, jsonify, request
from flask.views import MethodView

from app import db, app
from app.article.models import Article, Language, Category

article = Blueprint('article', __name__, url_prefix='/api')

class CategoryView(MethodView):
    def get(self, name=None):
        if not name:
            categories = Category.query.all()
            res = []
            for category in categories:
                res.append(category.to_json())
            return jsonify(categories=res)
        else:
            category = Category.query.filter_by(name=name).first_or_404()
            return jsonify(category=category.to_json())

    def post(self):
        name = request.get_json()["name"]
        description = request.get_json()["description"]
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return jsonify(category=category.to_json())

    def put(self, name=None):
        name = request.get_json()["name"]
        description = request.get_json()["description"]
        category = Article.query.filter_by(name=name).first_or_404()
        category.name = name
        category.description = description
        db.session.commit()
        return jsonify(category=category.to_json())

    def delete(self, name=None):
        Category.query.filter_by(name=name).delete()
        db.session.commit()
        return self.get()

class ArticleView(MethodView):
    def get(self, category=None, lang=None, id=None, per_page=None, page=1):
        if not id:
            if lang != None:
                lang = Language.query.filter_by(name=lang).first_or_404()
                res = []
                for article in lang.articles.paginate(page, per_page).items:
                    res.append(article.to_json())
                return jsonify(articles=res)
            else:
                articles = Article.query.paginate(page, per_page).items
                res = []
                for article in articles:
                    res.append(article.to_json())
                return jsonify(articles=res)
        else:
            article = Article.query.get(id)
            if not article:
                abort(404)
            return jsonify(article=article.to_json())

    def post(self):
        title = request.get_json()["title"]
        content = request.get_json()["content"]
        lang_id = request.get_json()["lang_id"]
        article = Article(title=title, content=content, lang_id=lang_id)
        db.session.add(article)
        db.session.commit()
        return jsonify(article=article.to_json())

    def put(self, id=None):
        title = request.get_json()["title"]
        content = request.get_json()["content"]
        lang_id = request.get_json()["lang_id"]
        article = Article.query.filter_by(id=id).first_or_404()
        article.title = title
        article.content = content
        article.edit_date = datetime.now()
        article.lang_id = lang_id
        db.session.commit()
        return jsonify(article=article.to_json())


    def delete(self, id=None):
        Article.query.filter_by(id=id).delete()
        db.session.commit()
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
            lang = Language.query.filter_by(name=name).first_or_404()
            if not lang:
                abort(404)
            return jsonify(language=lang.to_json())

    def post(self):
        name = request.get_json()["name"]
        lang = Language(name=name)
        db.session.add(lang)
        db.session.commit()
        language = Language.query.filter_by(id=lang.id).first_or_404()
        return jsonify(language=language.to_json())
    
    def put(self, name=None):
        data_name = request.get_json()["name"]
        lang = Language.query.filter_by(name=name).first_or_404()
        lang.name = data_name
        db.session.commit()
        res = Language.query.filter_by(id=lang.id).first_or_404()
        return jsonify(language=res.to_json())

    def delete(self, name=None):
        Language.query.filter_by(name=name).delete()
        db.session.commit()
        return self.get()

article_view = ArticleView.as_view('article_view')
lang_view = LangView.as_view('lang_view')
category_view = CategoryView.as_view('category_view')

# articles
article.add_url_rule(
    '/article/', view_func=article_view, methods=['POST']
)
article.add_url_rule(
    '/article/<int:id>', view_func=article_view, methods=['GET','PUT','DELETE']
)
article.add_url_rule(
    '/articles/per_page=<int:per_page>/page=<int:page>', view_func=article_view, methods=['GET']
)
article.add_url_rule(
    '/articles/<lang>/per_page=<int:per_page>/page=<int:page>', view_func=article_view, methods=['GET']
)

# languages
article.add_url_rule(
    '/languages/', view_func=lang_view, methods=['GET']
)
article.add_url_rule(
    '/language/', view_func=lang_view, methods=['POST']
)
article.add_url_rule(
    '/language/<name>', view_func=lang_view, methods=['GET','PUT','DELETE']
)

# Categories
article.add_url_rule(
    '/categories/', view_func=category_view, methods=['GET']
)
article.add_url_rule(
    '/category/', view_func=category_view, methods=['POST']
)
article.add_url_rule(
    '/category/<name>', view_func=category_view, methods=['GET','PUT','DELETE']
)
