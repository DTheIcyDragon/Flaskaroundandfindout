import flask
import sqlite3
import os
import pathlib


dnd_bp = flask.Blueprint("dnd", __name__, url_prefix="/dnd")
DND_DB = pathlib.Path("database/dnd.sqlite")

@dnd_bp.route("/main")
def dnd_main():
    if not DND_DB.exists():
        DND_DB.open(mode="x").close()
    conn = sqlite3.connect(DND_DB)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS story (id INTEGER PRIMARY KEY AUTOINCREMENT, heading TEXT, act TEXT)")
    response = cursor.execute("SELECT id, heading, act FROM story ORDER BY id DESC")
    response = response.fetchall()
    return flask.render_template("dnd/main.html", entries = response)


@dnd_bp.route("/create", methods=["POST"])
def dnd_create():
    return flask.render_template()
