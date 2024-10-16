from flask import Flask, request, jsonify, Blueprint
from Middleware.auth import auth_token

todos_bb = Blueprint("todos", __name__)

Token = "secret"

todos = []

@todos_bb.before_request
def auth():
    # Authenticate the request using the auth_token function
    return auth_token()

@todos_bb.route("/", methods=["GET"])
def fetch_todo():
    # Return all todos
    return jsonify(todos)

@todos_bb.route("/<int:todo_id>", methods=["GET"])
def fetch_todo_id(todo_id):
    # Find the todo by ID
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(todo)

@todos_bb.route("/<int:todo_id>", methods=["POST"])
def create_todo(todo_id):
    # Ensure title is provided
    title = request.json.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Create a new todo
    todo = {
        "id": todo_id,
        "title": title,
        "completed": request.json.get("completed", False)
    }
    
    todos.append(todo)
    return jsonify(todo), 201

@todos_bb.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Not Found"}), 404

    todo["title"] = request.json.get("title", todo["title"])
    todo["completed"] = request.json.get("completed", todo["completed"])
    return jsonify(todo)

@todos_bb.route("/<int:todo_id>", methods=["DELETE"])
def delete_todos(todo_id):
    global todos
    # Delete the todo with the specified ID
    todos = [t for t in todos if t["id"] != todo_id]
    return jsonify({"message": "Todo deleted successfully"}), 200

