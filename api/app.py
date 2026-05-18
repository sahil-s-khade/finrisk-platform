from flask import Flask, app, jsonify
from flask_jwt_extended import JWTManager

from config.settings import Config

from api.auth import auth_bp

from api.transactions import transaction_bp

from flask_cors import CORS

from api.routes.explainability \
import explainability_bp

# Initialize JWT manager
jwt = JWTManager()


def create_app():
    """
    Flask application factory.
    """

    app = Flask(__name__)

    CORS(app)

    # Load configuration
    app.config["SECRET_KEY"] = Config.SECRET_KEY
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY

    # Initialize JWT
    jwt.init_app(app)

    # Home route
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "message": "FinRisk Platform API is running"
        }), 200

    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health_check():
        return jsonify({
            "status": "healthy",
            "service": "finrisk-platform"
        }), 200
    
    # Register authentication routes
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    
    # Register transaction routes
    app.register_blueprint(
    transaction_bp,
    url_prefix="/api/v1"
)
    
    app.register_blueprint(
    explainability_bp,
    url_prefix="/api/v1"
)
    
    return app


# Run locally
if __name__ == "__main__":
    app = create_app()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )