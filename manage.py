"""
manage.py
- provides a command line utility for interacting with the
  application to perform interactive debugging and setup
"""

from flask_script import Manager

from geocens_api.application import create_app

app = create_app()

manager = Manager(app)


# enable python shell with application context
@manager.shell
def shell_ctx():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
