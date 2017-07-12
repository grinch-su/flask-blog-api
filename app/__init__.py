from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

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

app = CustomFlask(__name__,template_folder='templates')

app.config.update(
    DEBUG=True,
    SECRET_KEY='key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:8497@localhost/blog',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=False
)

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)

from app.article.views import article
from app.comment.views import comment
from app.user.views import user

app.register_blueprint(user)
app.register_blueprint(article)
app.register_blueprint(comment)


@app.route("/", methods=['GET'])
def index():
    return render_template('map-api.html')


# @app.route("/api-map", methods=['GET'])
# def site_map():
#     import urllib
#     output = []
#     for rule in app.url_map.iter_rules():
#         methods = []
#         for m in rule.methods:
#             meth = urllib.parse.unquote("{}".format(m))
#             if m not in ('OPTIONS','HEAD'):
#                 methods.append(meth)
#         line = {
#             'methods': methods,
#             'rule': urllib.parse.unquote("{}".format(rule))
#         }
#         if '/' in urllib.parse.unquote("{}".format(rule)):
#             output.append(line)
#         else:
#             continue
#     return jsonify(links=output)