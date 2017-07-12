from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_json(self):
        user = {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
        return user
    def __repr__(self):
        return '<User %d>' % self.username