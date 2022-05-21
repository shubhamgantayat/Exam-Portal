from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('Home.html')


if __name__ == '__main__':
    app.run(debug=True)
