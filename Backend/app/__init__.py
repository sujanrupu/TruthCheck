from flask import Flask
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.utils.config.Config")
    
    # Register Routes
    register_routes(app)
    
    return app
