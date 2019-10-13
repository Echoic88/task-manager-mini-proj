import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=(os.getenv("PORT")), debug=False)