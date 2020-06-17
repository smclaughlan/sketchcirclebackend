from flask import Blueprint
from app.models import User, Sketchbook, db

bp = Blueprint("sketchbook", __name__, "")


@bp.route("/sketchbooks")
def getBasicSketchbooks():
    sketchbooks = Sketchbook.query.all()
    returnDict = dict()
    for book in sketchbooks:
        returnDict[book.id] = {"owner_id": book.owner_id, "title": book.title}
    return returnDict
