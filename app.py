from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        json = request.get_json()
        return jsonify({'you sent': json}), 200
    else:
        return jsonify({"about": "Hello world"})


if __name__ == '__main__':
    app.run()
