from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import pytz


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    avatarurl = db.Column(db.Text)
    username = db.Column(db.String(20), unique=True, nullable=False)
    hashed_password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    usertofollow = db.relationship(
        "Follow", back_populates="followtouser")

    usertopost = db.relationship("Post", back_populates="posttouser")
    usertochatmessage = db.relationship(
        "ChatMessage", back_populates="chatmessagetouser")
    usertosketchbook = db.relationship(
        "Sketchbook", back_populates="sketchbooktouser")
    userstogoals = db.relationship("Goal", back_populates="goalstousers")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, testpass):
        return check_password_hash(self.hashed_password, testpass)


class Follow(db.Model):
    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True)
    sketchbook_id = db.Column(db.Integer, db.ForeignKey("sketchbooks.id"))
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    db.UniqueConstraint(sketchbook_id, follower_id)

    followedsketchbook = db.relationship("Sketchbook",
                                         foreign_keys=[sketchbook_id])
    followtouser = db.relationship("User", foreign_keys=[follower_id])

    def dictify(self):
        return {
            'id': self.id,
            'follower_id': self.follower_id,
            'sketchbook_id': self.sketchbook_id
        }


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    sketchbook_id = db.Column(db.Integer, db.ForeignKey("sketchbooks.id"),
                              nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
                          nullable=False)

    posttouser = db.relationship("User", back_populates="usertopost")
    posttosketchbook = db.relationship(
        "Sketchbook", back_populates="sketchbooktopost")

    def dictify(self):
        return {
            'id': self.id,
            'body': self.body,
            'username': self.posttouser.username,
            'avatar': self.posttouser.avatarurl,
            'sketchbook_id': self.sketchbook_id,
            'user_id': self.user_id,
            'timestamp': self.timestamp
        }


class ChatMessage(db.Model):
    __tablename__ = "chatmessages"
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                        nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
                          nullable=False)

    chatmessagetouser = db.relationship(
        "User", back_populates="usertochatmessage")

    def dictify(self):
        return {
            'id': self.id,
            'body': self.body,
            'username': self.chatmessagetouser.username,
            'user_id': self.user_id,
            'timestamp': self.timestamp
        }


class Sketchbook(db.Model):
    __tablename__ = "sketchbooks"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
                          nullable=False)

    sketchbooktopost = db.relationship(
        "Post", back_populates="posttosketchbook")
    sketchbooktouser = db.relationship(
        "User", back_populates="usertosketchbook")
    sketchbookstogoals = db.relationship(
        "Goal", back_populates="goalstosketchbooks")

    def dictify(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'title': self.title,
            'timestamp': self.timestamp
        }


class Goal(db.Model):
    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    Sketchbook_id = db.Column(db.Integer, db.ForeignKey(
        "sketchbooks.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000))
    target = db.Column(db.Integer, nullable=False)
    targetdate = db.Column(db.DateTime, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
                          nullable=False)

    goalstousers = db.relationship("User", back_populates="userstogoals")
    goalstosketchbooks = db.relationship(
        "Sketchbook", back_populates="sketchbookstogoals")
    goaltodatapoint = db.relationship(
        "Datapoint", back_populates="datapointtogoal")

    def dictify(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id,
            'sketchbook_id': self.Sketchbook_id,
            'title': self.title,
            'description': self.description,
            'target': self.target,
            'targetdate': self.targetdate,
            'timestamp': self.timestamp
        }


class Datapoint(db.Model):
    __tablename__ = "datapoints"
    id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goals.id"), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
                          nullable=False)

    datapointtogoal = db.relationship("Goal", back_populates="goaltodatapoint")

    def dictify(self):
        return {
            'id': self.id,
            'goal_id': self.goal_id,
            'value': self.value,
            'timestamp': self.timestamp
        }
