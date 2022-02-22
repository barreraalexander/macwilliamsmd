from flask import Flask
from flask_assets import Environment
from flask_caching import Cache
from flask_mail import Mail

from website.configs import Config, cacheConfig
from website.utils.assets import bundles

assets = Environment()
cache = Cache(config=cacheConfig)
mail = Mail ()

def create_app(config_class=Config):
    app = Flask (__name__)
    app.config.from_object(Config)

    assets.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    
    from website.blueprints.main.routes import main
    from website.blueprints.api.routes import api
    from website.blueprints.errors.handlers import errors


    assets.register(bundles)
    app.register_blueprint (main)
    app.register_blueprint (api)
    # app.register_blueprint (errors)

    return app
