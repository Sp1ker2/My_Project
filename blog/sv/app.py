from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
@app.route("/")
def main ():
    return render_template("index.html")

@app.route("/about")
def about ():
    return render_template("about.html")




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)