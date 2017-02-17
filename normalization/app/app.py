from flask import Flask, request, jsonify
from normalization import normalize

app = Flask(__name__)


@app.route('/', methods=['POST'])
def run_normalization():
    json_content = request.get_json()

    if "array" in json_content:
        array = json_content["array"]
        norm_array = normalize(array)
        return jsonify({
            "status": "ok",
            "result": norm_array
        })

    return jsonify({
        "status": "failed",
        "message": "No array"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
