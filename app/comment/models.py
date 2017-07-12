from app import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    article_id = db.Column(db.Integet, db.ForeignKey('article.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    to_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, content):
        self.content = content
        
    def to_json(self):
        comment = {
            "id": self.id,
            "content": self.content,
            "user_id": self.user_id,
            "to_user_id": self.to_user_id
        }
        return comment