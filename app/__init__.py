from flask import Flask
from flask_sqlalchemy import SQLAclhemy
from flask_migrate import Migrate, MigrateCommand

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

db = SQLAclhemy(app)
migrate = Migrate(app, db)

from app.article.views import article
from app.comment.views import comment
from app.user.views import user

app.register_blueprint(article)
app.register_blueprint(user)