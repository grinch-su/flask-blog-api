from app import db

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name
        
    def to_json(self):
        tag = {
            "id": self.id,
            "name": self.name
        }
        return tag
