from flask import Flask,request,jsonify,Blueprint
from Routes.todo import todos_bb

app = Flask(__name__)
app.register_blueprint(todos_bb,url_prefix="/todos")

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error":"Not Found"}), 404


if __name__ == "__main__":
    app.run(port=5000)
