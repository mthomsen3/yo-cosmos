from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from yocosmos.config import Config
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# by using this design pattern (rather than db = SQLAlchemy(app), etc.)
# no application-specific state is stored on the extension object
# so one extension object can be used for multiple apps
# they are instead

# requires memcached docker container to be running
#db = SQLAlchemy()
#mail = Mail()
#limiter = Limiter(key_func=get_remote_address,
#                  storage_uri="memcached://localhost:11211",
#                  storage_options={})

db = SQLAlchemy()
mail = Mail()
limiter = Limiter(key_func=get_remote_address,
                  storage_uri="memory://",
                  storage_options={})


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mail.init_app(app)
    limiter.init_app(app)

    # must be done after db initialization to avoid circular import errors
    # load routes from blueprints

    from yocosmos.posts.routes import posts
    from yocosmos.main.routes import main
    from yocosmos.errors.handlers import errors
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
