from datetime import datetime
from app.models import User, Follow, Post, Sketchbook
from app import app, db
from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.


with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(
        username='DigitalPainter',
        hashed_password='pbkdf2:sha256:150000$5cEZurmB$db355487fa715a469c081f7a99c29bd77c1b4303d5418b8bde0118e52795b1ef',
        email='DigitalPainter@email.com',
    )
    skb1 = Sketchbook(
        owner_id=1,
        title='DigitalPainter\'s sketchbook'
    )

    post1 = Post(
        body="Here's an example sketchbook.         ![](https: // 66.media.tumblr.com/378aeb06aab219432ac99f5e14322afb/tumblr_o5quc9w6ap1r4ltwho1_1280.png)         ![](https: // 66.media.tumblr.com/1ecf7f27c19feb286388eabc1d7ff4f9/tumblr_o1n645Y8RE1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 1, day: 1)
    )
    post2 = Post(
        body="Vivamus erat ipsum, pulvinar non dolor suscipit, pulvinar porttitor eros. Duis in vehicula turpis. Nam ac dapibus ligula, ut rhoncus dolor. Nulla imperdiet pharetra libero, ac maximus urna. Mauris blandit pretium mi, in venenatis purus posuere ut. In tristique sollicitudin sollicitudin. Morbi nec scelerisque nunc, non molestie nisi. Donec porta consectetur lorem eget consectetur. Cras nec malesuada lectus. Maecenas hendrerit nisl venenatis eros sagittis, sit amet vehicula diam congue. Etiam euismod ornare purus ac tempor. Morbi non mauris nibh. Integer porttitor, dolor quis fringilla placerat, quam urna iaculis purus, eget consectetur justo felis vitae libero. Mauris consectetur, sem nec feugiat maximus, lacus neque facilisis nulla, id varius lacus mauris vel massa.         ![](https: // 66.media.tumblr.com/d3c1d27e2c9a1fdedd482bcfa4c4fa78/tumblr_o1hvrslPPQ1r4ltwho1_540.png)         ![](https: // 66.media.tumblr.com/9e58d04b714baafae9cb19019809911f/tumblr_oaknvxYjni1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 1, day: 15)
    )

    # body = db.Column(db.Text, nullable=False)
    # sketchbook_id = db.Column(db.Integer, db.ForeignKey("sketchbooks.id"),
    #                           nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey("users.id"),
    #                     nullable=False)
    # timestamp = db.Column(db.DateTime, default=datetime.datetime.now(),
    #                       nullable=False)

    db.session.add(user1)
    db.session.add(skb1)
    # db.session.add(f2)
    # db.session.add(f3)
    # db.session.add(f4)
    # db.session.add(f5)
    # db.session.add(post1)
    # db.session.add(post2)
    # db.session.add(post3)
    # db.session.add(post4)
    # db.session.add(post5)
    # db.session.add(post6)
    # db.session.add(post7)
    # db.session.add(post8)
    # db.session.add(post9)
    # db.session.add(like1)
    # db.session.add(like2)
    # db.session.add(like3)
    # db.session.add(like4)
    # db.session.add(comment1)
    # db.session.add(comment2)
    # db.session.add(comment3)
    # db.session.add(comment4)
    # db.session.add(comment5)
    # db.session.add(comment6)
    db.session.commit()
