from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config.update(
    DEBUG=True,
    SECRET_KEY='key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:8497@localhost/simpleblog',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=True
)
db = SQLAlchemy(api)


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Posts {}{})>'.format(self.title, self.content)


@api.route('/post', methods=['POST'])
def createPost():
    title = request.get_json()["title"]
    content = request.get_json()["content"]

    post = Posts(title=title, content=content)

    curr_session = db.session

    try:
        curr_session.add(post)
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    postId = post.id
    data = Posts.query.filter_by(id=postId).first()

    result = [data.title, data.content]

    return jsonify(session=result)


@api.route('/posts', methods=['GET'])
def getPosts():
    data = Posts.query.all()
    data_all = []
    for post in data:
        data_all.append([post.id,
                         post.title,
                         post.content])

    return jsonify(posts=data_all)


@api.route('/post/<int:postId>', methods=['PATCH'])
def updatePost(postId):
    global post

    title = request.get_json()["title"]
    content = request.get_json()["content"]
    curr_session = db.session
    try:
        post = Posts.query.filter_by(id=postId).first()
        post.title = title
        post.content = content

        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    postId = post.id
    data = Posts.query.filter_by(id=postId).first()
    result = [data.title, data.content]
    return jsonify(session=result)


@api.route('/post/<int:postId>')
def deletePost(postId):
    curr_session = db.session
    Posts.query.filter_by(id=postId).delete()
    curr_session.commit()

    return getPosts()

if __name__ == '__main__':
    api.run()
