from flask import Blueprint
from app.models import User, Sketchbook, db

bp = Blueprint("sketchbook", __name__, "")


@bp.route("/sketchbooks")
def getBasicSketchbooks():
    sketchbooks = Sketchbook.query.order_by(Sketchbook.timestamp).all()
    sketchbooks.reverse()
    returnDict = dict()
    i = 1
    for book in sketchbooks:
        returnDict[i] = {"owner_id": book.owner_id,
                         "title": book.title,
                         "timestamp": str(book.timestamp)}
        i += 1
    return returnDict
