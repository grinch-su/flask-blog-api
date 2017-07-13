from datetime import datetime
from app import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, unique=True, nullable=False)

    def __init__(self, name, description):
        self.name = name,
        self.description = description

    def to_json(self):
        category = {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }
        return category

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        lang_json = {
            "id": self.id,
            "name": self.name
        }
        return lang_json

    def __repr__(self):
        return '< Lang %d >' % self.name


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',
        backref=db.backref('articles', lazy='dynamic'))
    lang_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    language = db.relationship('Language',
        backref=db.backref('articles', lazy='dynamic'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('articles', lazy='dynamic'))
    timestamp = db.Column(db.DateTime, nullable=False)
    edit_date = db.Column(db.DateTime)

    def __init__(self, title, content, lang_id):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()
        self.lang_id = lang_id

    def to_json(self):
        article_json = {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "category_id": self.category_id,
            "lang_id": self.lang_id,
            "user_id": self.user_id,
            "date": self.timestamp,
            "edit_date": self.edit_date
        }
        return article_json

    def __repr__(self):
        return '<Posts %d %d>' % self.title, self.content
