from flask import Flask, render_template, request
from py_backend.logger.log_db import Logger
from py_backend.mongo_db.crud import Operations
import config

app = Flask(__name__)
config.logger = Logger()
config.mongo_db = Operations("ExamPortal", config.logger)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('Home.html')


@app.route('/auth/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        record = request.get_json()
        print(record)


if __name__ == '__main__':
    config.logger.log("INFO", "App starting")
    app.run(debug=True)
