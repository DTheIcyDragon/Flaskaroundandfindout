import flask
import werkzeug.exceptions

from blueprints import dnd
import exceptions

app = flask.Flask(__name__)


@app.route('/')
def index():
    user = flask.request.cookies.get("user")
    return flask.render_template('index.html', user=user)


app.register_blueprint(dnd.dnd_bp)


@app.route("/wip")
def wip():
    raise exceptions.UnderConstruction()


@app.errorhandler(exceptions.UnderConstruction)
def underConstruction(e: werkzeug.exceptions.HTTPException):
    return flask.render_template('errors/error.html', title = "Under Construction", error = "This website is being built, soon™ something will be here", web_dev = True)

@app.errorhandler(404)
def underConstruction(e: werkzeug.exceptions.HTTPException):
    return flask.render_template('errors/error.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=80,
        debug=True
    )
