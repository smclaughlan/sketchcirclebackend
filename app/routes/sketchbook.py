from flask import Blueprint, request
from sqlalchemy import and_
from app.models import Follow, Goal, User, Sketchbook, Post, Datapoint, db
from ..util import token_required
from datetime import datetime

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


@bp.route("/sketchbooks/<int:sk_id>")
def getSketchbookPosts(sk_id):
    posts = Post.query.filter(Post.sketchbook_id == sk_id).all()
    postsList = []
    for post in posts:
        currPost = {
            'id': post.id,
            'user_id': post.user_id,
            'username': post.posttouser.username,
            'avatar': post.posttouser.avatarurl,
            'sketchbook_id': post.sketchbook_id,
            'body': post.body,
            'timestamp': post.timestamp,
        }
        postsList.append(currPost)

    goals = Goal.query.filter(Goal.Sketchbook_id == sk_id).all()
    goalsList = []
    for goal in goals:
        currGoal = {
            'id': goal.id,
            'owner_id': goal.owner_id,
            'sketchbook_id': goal.Sketchbook_id,
            'title': goal.title,
            'description': goal.description,
            'target': goal.target,
            'targetdate': goal.targetdate,
            'timestamp': goal.timestamp
        }
        goalsList.append(currGoal)
    returnDict = {
        'posts': postsList,
        'goals': goalsList
    }
    return returnDict


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
        'id': newPost.id,
        'user_id': current_user.id,
        'username': current_user.username,
        'avatar': current_user.avatarurl,
        'sketchbook_id': sk_id,
        'body': data['msgBody'],
        'timestamp': newPost.timestamp,
    }
    return retPost


@bp.route("/goal", methods=["POST"])
@token_required
def addGoal(current_user):
    data = request.json
    splitTargetDate = data['targetDate'].split('-')
    joinedTargetDate = ' '.join(splitTargetDate)
    print(data)
    datetimeOfTarget = datetime.strptime(
        joinedTargetDate, '%Y %m %d')
    print(datetimeOfTarget)
    userSketchbook = Sketchbook.query.filter(
        Sketchbook.owner_id == current_user.id).first()
    newGoal = Goal(
        owner_id=current_user.id,
        Sketchbook_id=userSketchbook.id,
        title=data['title'],
        description=data['description'],
        target=data['target'],
        targetdate=datetimeOfTarget,
    )
    db.session.add(newGoal)
    db.session.commit()
    returnDict = {
        'id': newGoal.id,
        'owner_id': newGoal.owner_id,
        'sketchbook_id': newGoal.Sketchbook_id,
        'title': newGoal.title,
        'description': newGoal.description,
        'target': newGoal.target,
        'targetdate': newGoal.targetdate,
        'timestamp': newGoal.timestamp
    }
    return returnDict


@bp.route("/goal/newdata", methods=["POST"])
@token_required
def addDataPoint(current_user):
    data = request.json
    newDataPoint = Datapoint(
        goal_id=data['goalid'],
        value=data['value']
    )
    db.session.add(newDataPoint)
    db.session.commit()
    returnDict = {
        'goal_id': newDataPoint.goal_id,
        'value': newDataPoint.value,
        'timestamp': newDataPoint.timestamp
    }
    return returnDict
