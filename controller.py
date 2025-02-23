from flask import Flask, request, jsonify
from connect import connect
from config import load_config
from meal_planner_service import create_item, get_all_items, get_item_by_id

app = Flask(__name__)

@app.route("/get-item/<item_id>")
def get_item(item_id):
    return jsonify(get_item_by_id(item_id)), 200

@app.route("/get-items")
def get_items():
    return jsonify(get_all_items()), 200
    
@app.route("/create-item", methods=["POST"])
def post_item():
    data = request.get_json()
    print(data.get('name'))
    
    return jsonify(create_item(data.get("name"), data.get("price"))), 201


if __name__ == "__main__":
    config = load_config()
    connect(config)
    app.run(debug=True)