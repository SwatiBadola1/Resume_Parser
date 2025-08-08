from flask import Flask
from src.api.routes import api_bp

def create_app():
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object('config')

    # Register API blueprints
    app.register_blueprint(api_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)