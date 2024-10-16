from flask import Flask,request,jsonify


Token = "secret"


def auth_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {Token}":
        return jsonify({"error":"unauthorized access"}),401