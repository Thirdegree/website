from webapp import app
import flask
@app.route('/')
def home():
    return flask.render_template("home.html")
