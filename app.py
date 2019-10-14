import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGODB_NAME"] = "task_manager"
app.config["MONGO_URI"] = os.getenv("mongoURI")

mongo = PyMongo(app)


@app.route("/")
@app.route("/add_task")
def add_task():
    return render_template('addtask.html', categories=mongo.db.categories.find())


@app.route('/insert_task', methods=["POST"])
def insert_task():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

    

if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=(os.getenv("PORT")), debug=True)