from flask import Flask, jsonify, request
import main

app = Flask(__name__)

@app.route('/run-test', methods=['GET','POST'])
def run_test():
    results = main.run_test()

    return jsonify(results)


if __name__ == "__main__":
    app.run(debug=True)