from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from src.webserver.routes import event_bp
    app.register_blueprint(event_bp)

    return app
