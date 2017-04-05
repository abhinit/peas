from flask import Flask, request, jsonify

import pandas as pd

import urllib2

from taskflow import engines
from taskflow.patterns import linear_flow
from taskflow import task


class FileReadTask(task.Task):


    default_provides = 'file_read_result'

    def execute(self):
        print("in the file read")
        with open('small.data') as f:
            dataframe = pd.read_csv(f)
            return dataframe.to_json()


class StandardizationTask(task.Task):

    default_provides = 'standardization_result'

    def execute(self, standardization_input):
        print("in the standardisation task")
        req = urllib2.Request('http://192.168.99.100:30583')
        req.add_header('Content-Type', 'application/json')
        req_data = '{\"data\": \"' + standardization_input + '\"}'

        print(req_data)
        response = urllib2.urlopen(req, req_data)
        return req_data
        # return response["result"]


class ClassificationTask(task.Task):
    def execute(self, classification_input):
        print("in classification task")
        print("Executing '%s'" % (self.name))
        print("Got input '%s'" % (a))


app = Flask(__name__)


@app.route("/")
def run_app():

    print("got request")

    wf = linear_flow.Flow("flow")
    wf.add(FileReadTask(), StandardizationTask(rebind={'standardization_input': 'file_read_result'}))

    e = engines.load(wf)

    print("Compiling...")
    e.compile()

    print("Preparing...")
    e.prepare()

    print("Running...")
    result = e.run()

    print("Done...")
    return jsonify({
        "status": "ok",
        "result": "test"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    