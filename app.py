from flask import Flask, request, jsonify
from flask import render_template

from search import search_topic

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def post():
    data = request.get_json()
    user_input = data.get("userInput")

    output = search_topic(user_input)

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
