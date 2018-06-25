from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    返回 '欢迎来到千峰教育！'


if __name__ == '__main__':
    app.run()
