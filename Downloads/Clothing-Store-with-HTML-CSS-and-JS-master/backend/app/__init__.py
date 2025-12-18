from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app) # Enable CORS for all routes

    # Register Blueprints
    from app.routes.auth import bp as auth_bp
    from app.routes.products import bp as products_bp
    from app.routes.orders import bp as orders_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(orders_bp, url_prefix='/api/orders')

    return app
