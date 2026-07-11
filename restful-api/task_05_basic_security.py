#!/usr/bin/python3
"""A Flask API demonstrating Basic and JWT authentication."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    jwt_required
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "your-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify a username and password for Basic Authentication."""
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        return username

    return None


@auth.error_handler
def basic_auth_error(status):
    """Return a 401 response when Basic Authentication fails."""
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return a message to an authenticated Basic Auth user."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Verify credentials and return a JWT access token."""
    login_data = request.get_json(silent=True)

    if login_data is None:
        return jsonify({"error": "Invalid credentials"}), 401

    username = login_data.get("username")
    password = login_data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]}
    )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return a message when a valid JWT is provided."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Allow access only to users with the admin role."""
    claims = get_jwt()

    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(error):
    """Handle a missing JWT."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(error):
    """Handle an invalid or malformed JWT."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle an expired JWT."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle a revoked JWT."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle a JWT that is not fresh."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
