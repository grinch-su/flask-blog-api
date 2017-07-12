from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from app import app, db, manager


manager.add_command('run', Server(host='0.0.0.0', port=8080))
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()
    return ('All tables created')


@manager.command
def drop_db():
    db.drop_all()
    return('All tables drops')


if __name__ == '__main__':
    manager.run()