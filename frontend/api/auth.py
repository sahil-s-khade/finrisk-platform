from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

# Create Blueprint
auth_bp = Blueprint("auth", __name__)

# Demo credentials
DEMO_USER = {
    "username": "admin",
    "password": "password123"
}


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Authenticate user and return JWT token.
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Missing JSON body"
        }), 400

    username = data.get("username")
    password = data.get("password")

    # Validate credentials
    if (
        username != DEMO_USER["username"]
        or password != DEMO_USER["password"]
    ):
        return jsonify({
            "error": "Invalid credentials"
        }), 401

    # Generate JWT token
    access_token = create_access_token(identity=username)

    return jsonify({
        "access_token": access_token
    }), 200


@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    """
    Example protected endpoint.
    """

    current_user = get_jwt_identity()

    return jsonify({
        "message": "Protected route accessed successfully",
        "user": current_user
    }), 200