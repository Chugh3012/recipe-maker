from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app