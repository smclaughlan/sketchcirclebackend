from flask import Blueprint, request
from werkzeug.security import generate_password_hash
from app.models import User, Sketchbook, db
import jwt
from ..config import Configuration
from ..util import token_required
from datetime import datetime


bp = Blueprint('user', __name__, url_prefix='')


@bp.route('/users', methods=['POST'])
def registration():
    data = request.json

    # check if username or email are already taken
    # send error msg if so
    foundUsername = User.query.filter(
        User.username == data['username']).first()
    if foundUsername and foundUsername.username == data['username']:
        return {'message': 'Username already in use'}, 403

    foundEmail = User.query.filter(
        User.email == data['email']).first()
    if foundEmail and foundEmail.email == data['email']:
        return {'message': 'Email already in use'}, 403

    hashedPassword = generate_password_hash(data["hashed_password"])
    newUser = User(username=data['username'],
                   email=data['email'],
                   hashed_password=hashedPassword)
    db.session.add(newUser)
    db.session.commit()
    newSketchbook = Sketchbook(owner_id=newUser.id,
                               title=f"{newUser.username}'s sketchbook",
                               timestamp=datetime.now())
    db.session.add(newSketchbook)
    db.session.commit()
    token = jwt.encode({'user_id': newUser.id}, Configuration.SECRET_KEY)
    return {
        'token': token.decode('UTF-8'),
        'currentUserId': newUser.id,
    }


@bp.route('/users', methods=['PUT'])
@token_required
def userUpdate(current_user):
    data = request.json
    avaUrl = data['avatarUrl']
    updateUser = User.query.filter(User.id == current_user.id).first()
    updateUser.avatarurl = avaUrl
    db.session.commit()
    return {'message': 'avatar updated'}


@bp.route('/users/login', methods=['POST'])
def login():
    data = request.json
    userEmail = data['email']
    userPassword = data['password']
    userToLogin = User.query.filter_by(email=userEmail).first()
    if userToLogin and userToLogin.check_password(userPassword):
        token = jwt.encode({'user_id': userToLogin.id},
                           Configuration.SECRET_KEY)
        return {
            'token': token.decode('UTF-8'),
            'currentUserId': userToLogin.id,
        }
    else:
        return {'message': 'Invalid user credentials'}, 401
