#!/usr/bin/env python3
from datetime import datetime
import os

from github import Github

from flask import Flask, request, jsonify, Blueprint, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_cors import CORS, cross_origin

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:8497@localhost/blog',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=False
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('run', Server(host='0.0.0.0', port=8080))
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()
    return ('All tables created')


# class User(db.Model):
#     __tablename__ = 'users'
#     name = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)

# class Lang(db.Model):
#     __tablename__ = 'languages'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    # lang = db.Column(db.String)
    timestamp = db.Column(db.DateTime, nullable=False)
    edit_date = db.Column(db.DateTime)

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.timestamp = datetime.now()

    def to_json(self):
        post_json = {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date": self.timestamp,
            "edit_date": self.edit_date
        }
        return post_json

    def __repr__(self):
        return '<Posts {}{})>'.format(self.title, self.content)

api = Blueprint('api',__name__, url_prefix='/api')

CORS(api)


# create post
@api.route('/post', methods=['POST'])
def createPost():
    title = request.get_json()["title"]
    content = request.get_json()["content"]
    post = Post(title=title, content=content)
    curr_session = db.session
    try:
        curr_session.add(post)
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()
    postId = post.id
    data = Post.query.filter_by(id=postId).first()
    return jsonify(post=data.to_json())


# get all posts
@api.route('/posts', methods=['GET'])
def getPosts():
    data = Post.query.all()
    if not data:
        return jsonify(posts=None)
    return jsonify(posts=[post.to_json()for post in data])


# get post
@api.route('/post/<int:postId>', methods=['GET'])
def get_post(postId):
    data = Post.query.get(postId)
    if not data:
        abort(404)
    return jsonify(post=data.to_json())


# edit post
@api.route('/post/<int:postId>', methods=['PUT'])
def updatePost(postId):
    global post

    title = request.get_json()["title"]
    content = request.get_json()["content"]
    curr_session = db.session
    try:
        post = Post.query.filter_by(id=postId).first()
        post.title = title
        post.content = content
        post.edit_date = datetime.now()
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()
        return jsonify(message='No post found')
    postId = post.id
    data = Post.query.filter_by(id=postId).first()

    return jsonify(post=data.to_json())


# delete post
@api.route('/post/<int:postId>', methods=['DELETE'])
def deletePost(postId):
    curr_session = db.session
    Post.query.filter_by(id=postId).delete()
    curr_session.commit()
    return getPosts()


@api.route('/repos', methods=['GET'])
def get_all_repos_with_GitHub():
    gh = Github(os.environ['APP_GITHUB_TOKEN'])
    repos = []
    for repo in gh.get_user().get_repos():
        repos.append({
            "name": repo.name,
            "updated_at": repo.updated_at,
            "homepage": repo.homepage,
            "url": repo.html_url,
            "description": repo.description,
            "lang": repo.language
        })
    return jsonify(repos=repos)
app.register_blueprint(api)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/api-map", methods=['GET'])
def site_map():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        methods = []
        for m in rule.methods:
            meth = urllib.parse.unquote("{}".format(m))
            if m not in ('OPTIONS','HEAD'):
                methods.append(meth)
        line = {
            'methods': methods,
            'rule': urllib.parse.unquote("{}".format(rule))
        }
        if '/api/' in urllib.parse.unquote("{}".format(rule)):
            output.append(line)
        else:
            continue
    return jsonify(links=output)

if __name__ == '__main__':
    manager.run()
