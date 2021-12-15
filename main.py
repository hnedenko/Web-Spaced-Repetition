from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, my dear world!"


@app.route('/about')
def about():
    return "It`s better app to interval repetition!"


if __name__ == "__main__":
    app.run(debug=True)