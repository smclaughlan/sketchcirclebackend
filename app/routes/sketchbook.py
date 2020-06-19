from flask import Blueprint, request
from sqlalchemy import and_
from app.models import Follow, User, Sketchbook, Post, db
from ..util import token_required

bp = Blueprint("sketchbook", __name__, "")


@bp.route("/sketchbooks")
def getBasicSketchbooks():
    sketchbooks = Sketchbook.query.order_by(Sketchbook.timestamp).all()
    sketchbooks.reverse()
    sketchbookList = list()
    # i = 1
    for book in sketchbooks:
        sketchbookDict = dict()
        sketchbookDict[book.id] = {"owner_id": book.owner_id,
                                   "sketchbook_id": book.id,
                                   "title": book.title,
                                   "timestamp": str(book.timestamp)}
        sketchbookList.append(sketchbookDict)
        # i += 1
    print(sketchbookList)
    follows = Follow.query.all()
    followList = []
    for follow in follows:
        followSublist = [follow.follower_id, follow.sketchbook_id]
        followList.append(followSublist)
    returnDict = dict()
    returnDict['sketchbooks'] = sketchbookList
    returnDict['follows'] = followList
    print(returnDict)
    return returnDict


@bp.route("/sketchbooks/<int:sk_id>/follow", methods=["POST"])
@token_required
def addFollow(current_user, sk_id):
    newFollow = Follow(
        sketchbook_id=sk_id,
        follower_id=current_user.id
    )
    db.session.add(newFollow)
    db.session.commit()
    returnDict = {newFollow.sketchbook_id: True}
    return returnDict


@bp.route("/sketchbooks/<int:sk_id>/follow", methods=["DELETE"])
@token_required
def deleteFollow(current_user, sk_id):
    followToDelete = Follow.query.filter(and_(
        (Follow.follower_id == current_user.id), (Follow.sketchbook_id == sk_id))).first()
    db.session.delete(followToDelete)
    db.session.commit()
    return {"sketchbook_id": followToDelete.sketchbook_id}


@bp.route("/sketchbooks/<int:sk_id>", methods=["POST"])
@token_required
def addPost(current_user, sk_id):
    data = request.json
    print(data)
    newPost = Post(
        user_id=current_user.id,
        sketchbook_id=sk_id,
        body=data['msgBody']
    )
    db.session.add(newPost)
    db.session.commit()
    retPost = {
        'user_id': current_user.id,
        'username': current_user.username,
        'sketchbook_id': sk_id,
        'body': data['msgBody'],
        'timestamp': newPost.timestamp,
    }
    return retPost
