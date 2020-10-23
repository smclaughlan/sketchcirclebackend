from flask import Blueprint, request
from sqlalchemy import and_
from app.models import ChatMessage, User, db
from ..util import token_required
from datetime import datetime

bp = Blueprint("chat", __name__, "")


@bp.route("/chatmessages")
def getChatMessages():
    chats = ChatMessage.query.order_by(ChatMessage.timestamp).all()
    chats.reverse()
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
def addChatMessage(current_user, chatbody):
    newChatMessage = ChatMessage(
        body=chatbody,
        user_id=current_user.id,
        timestamp=datetime.now()
    )
    db.session.add(newChatMessage)
    db.session.commit()
