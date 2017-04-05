import pandas as pd
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)


@app.route('/', methods=['POST'])
def run_normalization():
    print("am in normalization")
    json_content = request.get_json()

    if "data" not in json_content:
        return jsonify({
            "status": "failed",
            "message": "No data"
        })

    dataframe = pd.read_json(json_content["data"])

    # hard coded for now
    attr_cols = [1,2,3,4,5,6,7,8,9]

    sc = StandardScaler()
    dataframe[attr_cols] = sc.fit_transform(dataframe[attr_cols])

    return jsonify({
        "status": "ok",
        "result": dataframe.to_json(orient='values')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
