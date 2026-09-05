from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/submitdoitem", methods=["POST"])
def submit_do_item():
    data = request.get_json()
    item_name = data.get("item_name")

    if not item_name:
        return jsonify({"error": "Item name is required"}), 400

    return jsonify({
        "message": "Item received successfully",
        "item_name": item_name
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)