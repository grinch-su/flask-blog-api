from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import app
from app import db

manager = Manager(app)
manager.add_command('run', Server(host='0.0.0.0', port=8080))
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()
    return ('All tables created')


if __name__ == '__main__':
    manager.run()