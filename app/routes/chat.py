from flask import Blueprint, request
from sqlalchemy import and_
from app.models import ChatMessage, User, db
from ..util import token_required
from datetime import datetime

bp = Blueprint("chat", __name__, "")

# TODO delete all chat related code or implement chat


@bp.route("/chatmessages")
def getChatMessages():
    chats = ChatMessage.query.order_by(ChatMessage.timestamp).all()
    returnDict = dict()
    for chat in chats:
        returnDict[chat.id] = {
            'body': chat.body,
            'username': chat.chatmessagetouser.username,
            'user_id': chat.user_id,
            'timestamp': chat.timestamp
        }
    return returnDict


@bp.route("/chatmessages", methods=["POST"])
@token_required
def addChatMessage(current_user):
    data = request.json
    newChatMessage = ChatMessage(
        body=data['body'],
        user_id=current_user.id,
        timestamp=datetime.now()
    )
    chatDict = dict(
        body=data['body'],
        user_id=current_user.id,
        timestamp=datetime.now()
    )
    db.session.add(newChatMessage)

    allChats = ChatMessage.query.order_by(ChatMessage.timestamp).all()
    while len(allChats) > 5:
        chatToDelete = allChats.pop(0)
        db.session.delete(chatToDelete)

    db.session.commit()
    return chatDict
