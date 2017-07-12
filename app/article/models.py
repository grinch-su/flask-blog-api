from datetime import datetime
from app import db

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    articles = db.relationship('Article', backref='language',
                                lazy='dynamic')

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '< Lang %d >' % self.name


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    lang_id = db.Column(db.Integer, db.ForeignKey('article.id'))
    timestamp = db.Column(db.DateTime, nullable=False)
    edit_date = db.Column(db.DateTime)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()

    def __repr__(self):
        return '<Posts {} {}>'.format(self.title, self.content)
