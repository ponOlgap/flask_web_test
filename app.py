from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    st = "проект"
    return '<h1>Flask web-сайт</h1>' + st


if __name__ == '__main__':
    app.run()
