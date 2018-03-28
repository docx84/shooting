import json

from flask import Flask, redirect, jsonify, request
from flask_cors import CORS
from tinydb import TinyDB, Query

app = Flask(__name__, static_url_path='', static_folder="vueProject/dist")
CORS(app)


class DB:
    def __init__(self):
        self.dbName = "default"
        self.db = None
        self.openDB()

    def openDB(self):
        self.db = TinyDB("db/%s.json" % self.dbName)


data = DB()


@app.route('/')
def hello_world():
    return redirect("/index.html", code=302)


@app.route("/data/_name", methods=["GET"])
def getDbName():
    return jsonify({"result": data.dbName})


@app.route("/data/_name", methods=["POST"])
def updateDbName():
    data.dbName = request.data.decode("utf-8")
    data.openDB()
    return jsonify({"result": data.dbName})


@app.route("/data/players", methods=["POST"])
def addPlayer():
    try:
        player = json.loads(request.data.decode("utf-8"))
        player.setdefault("series", [[None] * 25])
        doc_id = data.db.insert(player)
        return jsonify({"results": {
            "player": player,
            "doc_id": doc_id}})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/data/players", methods=["GET"])
def getPlayers():
    return jsonify({"results": data.db.all()})


@app.route("/data/players/<int:doc_id>", methods=["PUT"])
def updatePlayer(doc_id):
    try:
        oldPlayer = data.db.get(doc_id=doc_id)
        player = json.loads(request.data.decode("utf-8"))
        player.setdefault("series", oldPlayer["series"])
        data.db.update(player, doc_ids=[doc_id])
        return jsonify({"results": {
            "player": player,
            "doc_id": doc_id}})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/data/players/<int:doc_id>", methods=["GET"])
def getPlayer(doc_id):
    player = data.db.get(doc_id=doc_id)
    if player is None:
        return jsonify({"error": "missing player"}), 404
    return jsonify({"results": player})


@app.route("/data/players/<int:doc_id>/_addSerie", methods=["POST"])
def addSerie(doc_id):
    try:
        player = data.db.get(doc_id=doc_id)
        player["series"].append([None] * 25)
        data.db.write_back([player])
        return getPlayer(doc_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/data/players/<int:doc_id>/shoot/<int:serie>/<int:shoot>", methods=["POST"])
def markShoot(doc_id, serie, shoot):
    try:
        outcome = json.loads(request.data.decode("utf-8"))
        outcome = None if outcome is None else bool(outcome)
        player = data.db.get(doc_id=doc_id)
        player["series"][serie][shoot] = outcome
        data.db.write_back([player])
        return getPlayer(doc_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
