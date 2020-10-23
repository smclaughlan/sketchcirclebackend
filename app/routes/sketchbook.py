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
    for book in sketchbooks:
        sketchbookDict = dict()
        sketchbookDict[book.id] = {"owner_id": book.owner_id,
                                   "sketchbook_id": book.id,
                                   "avatar": book.sketchbooktouser.avatarurl,
                                   "title": book.title,
                                   "timestamp": str(book.timestamp)}
        sketchbookList.append(sketchbookDict)

    follows = Follow.query.all()
    followList = []
    for follow in follows:
        followSublist = [follow.follower_id, follow.sketchbook_id]
        followList.append(followSublist)
    returnDict = dict()
    returnDict['sketchbooks'] = sketchbookList
    returnDict['follows'] = followList

    return returnDict


@bp.route("/posts/<int:postId>", methods=["DELETE"])
@token_required
def deletePost(current_user, postId):
    postToDelete = Post.query.filter(Post.id == postId).first()
    if postToDelete.user_id == current_user.id:
        db.session.delete(postToDelete)
        db.session.commit()
    return {"message": "post deleted"}


@bp.route("/posts/<int:postId>", methods=["PUT"])
@token_required
def updatePost(current_user, postId):
    data = request.json
    postToUpdate = Post.query.filter(Post.id == postId).first()
    if postToUpdate.user_id == current_user.id:
        postToUpdate.body = data['body']
        db.session.commit()
    return {"message": "post updated"}


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
    postsDict = dict()
    for post in posts:
        skbId = post.sketchbook_id
        postId = post.id
        if not skbId in postsDict.keys():
            postsDict[skbId] = {postId: None}
        postsDict[skbId][postId] = post.dictify()

    goals = Goal.query.filter(Goal.Sketchbook_id == sk_id).all()
    goalsDict = dict()
    datapointsDict = dict()
    for goal in goals:
        if not goal.Sketchbook_id in goalsDict.keys():
            goalsDict[goal.Sketchbook_id] = {goal.id: None}
        goalsDict[goal.Sketchbook_id][goal.id] = goal.dictify()
        datapoints = Datapoint.query.filter(Datapoint.goal_id == goal.id).all()
        for datapoint in datapoints:
            if not datapoint.goal_id in datapointsDict.keys():
                datapointsDict[datapoint.goal_id] = {datapoint.id: None}
            datapointsDict[datapoint.goal_id][datapoint.id] = datapoint.dictify()

    returnDict = {
        'posts': postsDict,
        'goals': goalsDict,
        'datapoints': datapointsDict
    }
    return returnDict


@bp.route("/sketchbooks/<int:sk_id>", methods=["POST"])
@token_required
def addPost(current_user, sk_id):
    data = request.json

    newPost = Post(
        user_id=current_user.id,
        sketchbook_id=sk_id,
        body=data['msgBody'],
        timestamp=datetime.now()
    )
    db.session.add(newPost)
    db.session.commit()

    skb = Sketchbook.query.filter(Sketchbook.id == sk_id).first()
    skb.timestamp = datetime.now()
    db.session.commit()

    # retPost = {
    #     'posts': {
    #         sk_id: {
    #             newPost.id: {
    #                 'id': newPost.id,
    #                 'user_id': current_user.id,
    #                 'username': current_user.username,
    #                 'avatar': current_user.avatarurl,
    #                 'sketchbook_id': sk_id,
    #                 'body': data['msgBody'],
    #                 'timestamp': newPost.timestamp,
    #             }
    #         }
    #     }
    # }
    # return retPost
    return getSketchbookPosts(sk_id)


@bp.route("/goal", methods=["POST"])
@token_required
def addGoal(current_user):
    data = request.json
    splitTargetDate = data['targetDate'].split('-')
    joinedTargetDate = ' '.join(splitTargetDate)

    datetimeOfTarget = datetime.strptime(
        joinedTargetDate, '%Y %m %d')

    userSketchbook = Sketchbook.query.filter(
        Sketchbook.owner_id == current_user.id).first()
    newGoal = Goal(
        owner_id=current_user.id,
        Sketchbook_id=userSketchbook.id,
        title=data['title'],
        description=data['description'],
        target=data['target'],
        targetdate=datetimeOfTarget,
        timestamp=datetime.now()
    )
    db.session.add(newGoal)
    db.session.commit()

    # check for goals that have passed finished date, and delete them
    goalsForCurrUser = Goal.query.filter(
        Goal.owner_id == current_user.id).all()
    currDate = datetime.now()
    for goal in goalsForCurrUser:
        if goal.targetdate < currDate:
            datapoints = Datapoint.query.filter(
                Datapoint.goal_id == goal.id).all()
            for datapoint in datapoints:
                db.session.delete(datapoint)
            db.session.delete(goal)

    db.session.commit()

    returnDict = {
        newGoal.Sketchbook_id: {
            newGoal.id: {
                'id': newGoal.id,
                'owner_id': newGoal.owner_id,
                'sketchbook_id': newGoal.Sketchbook_id,
                'title': newGoal.title,
                'description': newGoal.description,
                'target': newGoal.target,
                'targetdate': newGoal.targetdate,
                'timestamp': newGoal.timestamp
            }
        }
    }
    return returnDict


@bp.route("/goal/newdata", methods=["POST"])
@token_required
def addDataPoint(current_user):
    data = request.json
    newDataPoint = Datapoint(
        goal_id=data['goalid'],
        value=data['value'],
        timestamp=datetime.now()
    )
    db.session.add(newDataPoint)
    db.session.commit()
    returnDict = {
        newDataPoint.goal_id: {
            newDataPoint.id: {
                'goal_id': newDataPoint.goal_id,
                'value': newDataPoint.value,
                'timestamp': newDataPoint.timestamp
            }
        }
    }
    return returnDict
