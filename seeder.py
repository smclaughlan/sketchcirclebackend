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

    allposts = []

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
        body="""Here's an example sketchbook.

![](https://66.media.tumblr.com/378aeb06aab219432ac99f5e14322afb/tumblr_o5quc9w6ap1r4ltwho1_1280.png)
![](https://66.media.tumblr.com/1ecf7f27c19feb286388eabc1d7ff4f9/tumblr_o1n645Y8RE1r4ltwho1_1280.png)
        """,
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 1, 1)
    )
    allposts.append(post1)

    post2 = Post(
        body="""Vivamus erat ipsum, pulvinar non dolor suscipit, pulvinar porttitor eros. Duis in vehicula turpis. Nam ac dapibus ligula, ut rhoncus dolor. Nulla imperdiet pharetra libero, ac maximus urna. Mauris blandit pretium mi, in venenatis purus posuere ut. In tristique sollicitudin sollicitudin. Morbi nec scelerisque nunc, non molestie nisi. Donec porta consectetur lorem eget consectetur. Cras nec malesuada lectus. Maecenas hendrerit nisl venenatis eros sagittis, sit amet vehicula diam congue. Etiam euismod ornare purus ac tempor. Morbi non mauris nibh. Integer porttitor, dolor quis fringilla placerat, quam urna iaculis purus, eget consectetur justo felis vitae libero. Mauris consectetur, sem nec feugiat maximus, lacus neque facilisis nulla, id varius lacus mauris vel massa.

![](https://66.media.tumblr.com/d3c1d27e2c9a1fdedd482bcfa4c4fa78/tumblr_o1hvrslPPQ1r4ltwho1_540.png)
![](https://66.media.tumblr.com/9e58d04b714baafae9cb19019809911f/tumblr_oaknvxYjni1r4ltwho1_1280.png)
        """,
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 1, 15)
    )
    allposts.append(post2)

    post3 = Post(
        body="""Nam pulvinar magna et viverra ultrices. Curabitur a mauris quis tortor euismod tincidunt sed a neque. Aliquam vestibulum congue velit eu placerat. Ut lacinia augue ut placerat tristique. Pellentesque sed auctor augue. Fusce sit amet ligula malesuada, tempus velit eget, bibendum ligula. Suspendisse ut sapien molestie, finibus massa et, luctus risus. Cras vel risus commodo turpis luctus facilisis. In ultrices lacus vel posuere rhoncus. Nam at odio quis purus ultrices molestie. Cras efficitur porta velit ac malesuada. Proin sit amet feugiat nulla.

![](https://66.media.tumblr.com/c88a2430f1cd069c2c2150a912fa7188/tumblr_oan0kndgxU1r4ltwho1_1280.png)
![](https://66.media.tumblr.com/61aed172599c3aeec5418088d279245f/tumblr_ofqinzMCO11r4ltwho1_1280.png)
        """,
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 1, 20)
    )
    allposts.append(post3)

    post4 = Post(
        body="""Curabitur id turpis at quam vulputate fringilla vitae in lectus. Nulla mi nisl, pellentesque ac semper sed, iaculis et tortor. Nam iaculis sem placerat dolor tristique ornare sed eget nulla. Nulla facilisi. Vestibulum mollis justo felis, ac fringilla odio tincidunt at. Etiam vestibulum ante felis. Integer ac aliquam ante, nec lobortis risus. Fusce dictum nisl a diam tincidunt iaculis. Praesent accumsan turpis quis pretium varius. Pellentesque dignissim, nunc et tempus dictum, velit ligula sodales nisi, a lacinia arcu quam ut massa. Nulla eu laoreet erat, quis pretium nibh.

![](https://68.media.tumblr.com/adfcfc9ac947ee9616391e32612650a2/tumblr_oj56b9FCcM1r4ltwho1_1280.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 2, 11)
    )
    allposts.append(post4)

    post5 = Post(
        body="""Donec iaculis metus sit amet tellus feugiat, ac commodo dui tristique. Nunc nulla felis, mollis fermentum dapibus ultricies, molestie ut lorem. Ut congue pretium felis commodo volutpat. Sed in finibus purus. Etiam dictum urna lacus, vel pretium nunc porttitor vel. In laoreet blandit dui, feugiat faucibus enim condimentum et. Integer egestas fringilla justo, eget lobortis orci lobortis nec. Proin a tellus in nibh tempor porta vel sed mauris. In hac habitasse platea dictumst. Morbi luctus turpis porttitor, mollis odio sit amet, vestibulum nibh. Vestibulum eget fringilla libero, et consequat turpis. Curabitur convallis turpis nec massa malesuada, imperdiet cursus enim lacinia. Quisque sollicitudin, dui vel eleifend ultrices, ex neque elementum dolor, ac tempor leo nulla non orci.

![](https://68.media.tumblr.com/ae44b24f3aba9bbcf1a0686bda94796c/tumblr_ok30mbsMRz1r4ltwho1_500.png)
![](https://78.media.tumblr.com/8431461077bccf604fb798ee6704622f/tumblr_oxulrcjVHW1r4ltwho1_1280.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 2, 24)
    )
    allposts.append(post5)

    post6 = Post(
        body="""Etiam interdum arcu ac turpis gravida lacinia. Curabitur ornare volutpat libero sed iaculis. Mauris nec leo non dolor suscipit vestibulum. Donec consectetur malesuada egestas. Vivamus vestibulum bibendum cursus. Praesent placerat tellus sed urna efficitur, sed pharetra urna vestibulum. Suspendisse potenti.

![](https://78.media.tumblr.com/62a1a9781012144a92df3d357d1029e7/tumblr_p2qtagLXWG1r4ltwho1_1280.png)
        """,
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 3, 9)
    )
    allposts.append(post6)

    post7 = Post(
        body="""Nullam accumsan leo nec accumsan accumsan. Nullam placerat massa commodo est cursus, nec euismod enim facilisis. Vivamus a neque varius, ultricies enim volutpat, tincidunt odio. Curabitur purus dolor, varius vitae dignissim vitae, venenatis vel turpis. Praesent ac dui in urna vulputate sollicitudin.

![](https://78.media.tumblr.com/91f71502727c3a0afd03ac891117ab9c/tumblr_p3iknq8hMN1r4ltwho1_1280.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 3, 19)
    )
    allposts.append(post7)

    post8 = Post(
        body="""Suspendisse et eros ut augue fringilla volutpat sit amet id sapien. Nunc imperdiet sodales mauris, a hendrerit lorem vehicula eget. Nam fringilla, tortor et sagittis porta, lacus purus porttitor dui, id molestie velit arcu in sapien. Suspendisse mi dui, scelerisque fringilla feugiat sed, sagittis ac elit. Ut ante dui, tristique at tincidunt eget, iaculis ut quam. Cras hendrerit leo a elit aliquam consectetur a vehicula justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae        Curabitur sodales nibh et ipsum maximus cursus. Donec nec elit et ex lobortis placerat.

![](https://78.media.tumblr.com/b7f3cc6599b1b37fcb2262630ef3c1a3/tumblr_pc8xkwTa2E1r4ltwho1_540.png)

![](https://78.media.tumblr.com/c564c8939fc855a3d9a20e25fa847d32/tumblr_pcb6jfmopg1r4ltwho1_1280.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 4, 10)
    )
    allposts.append(post8)

    post9 = Post(
        body="""Vestibulum dignissim rutrum sagittis. Nunc interdum volutpat turpis, non accumsan metus dignissim id. Duis est massa, efficitur interdum condimentum ut, tempus nec lacus. Vestibulum gravida hendrerit nulla sit amet venenatis. Aenean a metus laoreet, sollicitudin nulla vel, molestie metus. Proin ligula lorem, pellentesque eu ullamcorper vel, varius et lacus. Nunc vel viverra sapien. Ut aliquam volutpat velit vitae posuere. Suspendisse non tempor enim. Etiam efficitur arcu non lacus egestas, sit amet eleifend arcu auctor. In porttitor, odio vel molestie fringilla, libero orci egestas nisl, nec lacinia lorem nunc et dui. Suspendisse potenti.

![](https://66.media.tumblr.com/e895da808fbbfd1ee07218cf0c65cbce/tumblr_pn5wqrz6S71r4ltwho1_1280.png)
![](https://66.media.tumblr.com/f05c260b95bead649f6487f58a26b326/tumblr_ppblco8Sv71r4ltwho2_1280.png)
![](https://66.media.tumblr.com/ba2c5d5beb07f9ebfcda2cf1af005ea5/tumblr_ppblco8Sv71r4ltwho1_1280.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 5, 13)
    )
    allposts.append(post9)

    post10 = Post(
        body="""Cras elit felis, ultrices vel arcu ut, gravida hendrerit quam. Aliquam laoreet vestibulum mauris eget feugiat. Suspendisse congue quis sapien posuere hendrerit. Mauris sit amet blandit augue. Proin porta libero nulla, eu commodo metus gravida a. Quisque vehicula, massa quis feugiat malesuada, nisi ante ultricies turpis, a sollicitudin neque odio nec dolor. Vestibulum at imperdiet dui. Aliquam et congue lorem. Sed tincidunt imperdiet tellus eu posuere. Donec placerat elementum urna id iaculis. Nulla facilisi. Vestibulum ipsum neque, sollicitudin eu risus ac, efficitur laoreet lectus.

![](https://66.media.tumblr.com/8a9f141952b77e3fee953c71628ce1c8/tumblr_opbgjv1dOF1r4ltwho1_640.png)""",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(2020, 6, 16)
    )
    allposts.append(post10)

    # guest seed data
    user2 = User(
        username='Guest',
        hashed_password='pbkdf2:sha256:150000$5cEZurmB$db355487fa715a469c081f7a99c29bd77c1b4303d5418b8bde0118e52795b1ef',
        email='Guest@email.com',
    )
    skb2 = Sketchbook(
        owner_id=2,
        title='Guest\'s sketchbook'
    )

    # hak seed data
    user3 = User(
        username='H_AK',
        hashed_password='pbkdf2:sha256:150000$5cEZurmB$db355487fa715a469c081f7a99c29bd77c1b4303d5418b8bde0118e52795b1ef',
        email='H_AK@email.com',
        avatarurl='https://i.imgur.com/7AOgDAz.png'
    )

    skb3 = Sketchbook(
        owner_id=3,
        title='H_AK\'s sketchbook'
    )

    post11 = Post(
        body="""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem sed risus ultricies tristique nulla aliquet. Faucibus et molestie ac feugiat sed. Congue quisque egestas diam in arcu. Volutpat est velit egestas dui. Sit amet consectetur adipiscing elit pellentesque habitant.

![](https://i.imgur.com/R1glhk6.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 6, 15)
    )
    allposts.append(post11)

    post12 = Post(
        body="""Id velit ut tortor pretium viverra suspendisse. Adipiscing diam donec adipiscing tristique risus nec feugiat. Diam vulputate ut pharetra sit amet aliquam id.

![](https://i.imgur.com/ygAV1Vr.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 6, 20)
    )
    allposts.append(post12)

    post13 = Post(
        body="""A condimentum vitae sapien pellentesque habitant morbi tristique. Malesuada fames ac turpis egestas sed tempus urna et. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare.

![](https://i.imgur.com/zl6XoFV.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 6, 22)
    )
    allposts.append(post13)

    post14 = Post(
        body="""Tortor at auctor urna nunc id cursus metus aliquam. Turpis egestas maecenas pharetra convallis posuere. Egestas sed sed risus pretium quam vulputate. Luctus venenatis lectus magna fringilla. Elit pellentesque habitant morbi tristique senectus et.

![](https://i.imgur.com/4bEM5Fu.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 6, 25)
    )
    allposts.append(post14)

    post15 = Post(
        body="""Enim lobortis scelerisque fermentum dui faucibus in ornare quam. Ultricies tristique nulla aliquet enim tortor at auctor urna nunc.

![](https://i.imgur.com/kqtjMbR.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 7, 10)
    )
    allposts.append(post15)

    post16 = Post(
        body="""Non curabitur gravida arcu ac tortor dignissim convallis aenean. Et netus et malesuada fames ac turpis. Etiam sit amet nisl purus in mollis nunc. Amet nisl purus in mollis nunc. Eleifend donec pretium vulputate sapien.

![](https://i.imgur.com/o88RBFG.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 7, 20)
    )
    allposts.append(post16)

    post17 = Post(
        body="""Dui nunc mattis enim ut tellus elementum sagittis vitae. Nunc sed id semper risus in hendrerit gravida. Aliquam ultrices sagittis orci a scelerisque purus semper eget. Non blandit massa enim nec dui.

![](https://i.imgur.com/zXQjgFq.png)
![](https://i.imgur.com/0Zd8DN3.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 8, 15)
    )
    allposts.append(post17)

    post18 = Post(
        body="""Risus nullam eget felis eget. Blandit volutpat maecenas volutpat blandit aliquam etiam. Quam quisque id diam vel quam elementum pulvinar. Bibendum neque egestas congue quisque. Leo duis ut diam quam nulla porttitor.

![](https://i.imgur.com/Y4s1rIE.png)
![](https://i.imgur.com/XFh1om6.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 8, 25)
    )
    allposts.append(post18)

    post19 = Post(
        body="""Rhoncus urna neque viverra justo nec. Et odio pellentesque diam volutpat commodo. Ligula ullamcorper malesuada proin libero. Nunc scelerisque viverra mauris in aliquam sem.

![](https://i.imgur.com/6vLz2ce.png)
![](https://i.imgur.com/dxuRhtn.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 9, 10)
    )
    allposts.append(post19)

    post20 = Post(
        body="""Sed faucibus turpis in eu mi bibendum. Tortor consequat id porta nibh. Accumsan lacus vel facilisis volutpat est velit egestas dui. Pulvinar neque laoreet suspendisse interdum consectetur libero.

![](https://i.imgur.com/yJsgytf.png)
![](https://i.imgur.com/6iZ5dDS.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 9, 20)
    )
    allposts.append(post20)

    post21 = Post(
        body="""Tortor at auctor urna nunc id cursus metus aliquam. Facilisi etiam dignissim diam quis enim lobortis scelerisque fermentum dui.

![](https://i.imgur.com/YStrd0G.png)
![](https://i.imgur.com/Hx82Dmb.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 10, 14)
    )
    allposts.append(post21)

    post22 = Post(
        body="""Vel turpis nunc eget lorem dolor sed viverra ipsum. Quisque id diam vel quam elementum pulvinar etiam non. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim. Placerat in egestas erat imperdiet. Mauris in aliquam sem fringilla ut morbi tincidunt augue.

![](https://i.imgur.com/mSf8Kwb.png)
![](https://i.imgur.com/WX0GQWe.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 11, 6)
    )
    allposts.append(post22)

    post23 = Post(
        body="""Dapibus ultrices in iaculis nunc sed augue lacus viverra vitae. Scelerisque eleifend donec pretium vulputate sapien nec sagittis. Mi proin sed libero enim sed. Augue mauris augue neque gravida in fermentum et sollicitudin. Nulla pharetra diam sit amet nisl suscipit adipiscing. Lectus quam id leo in. Diam sit amet nisl suscipit adipiscing bibendum est ultricies integer. Euismod in pellentesque massa placerat duis ultricies lacus.

![](https://i.imgur.com/jAt3KUa.png)
![](https://i.imgur.com/mGRIVHs.png)
![](https://i.imgur.com/7AOgDAz.png)
![](https://i.imgur.com/t11XyUB.png)
        """,
        sketchbook_id=3,
        user_id=3,
        timestamp=datetime(2020, 12, 10)
    )
    allposts.append(post23)

    # end hak seed data

    db.session.add(user1)
    db.session.add(skb1)
    db.session.add(user2)
    db.session.add(skb2)
    db.session.add(user3)
    db.session.add(skb3)

    for p in allposts:
        db.session.add(p)

    # db.session.add(post1)
    # db.session.add(post2)
    # db.session.add(post3)
    # db.session.add(post4)
    # db.session.add(post5)
    # db.session.add(post6)
    # db.session.add(post7)
    # db.session.add(post8)
    # db.session.add(post9)
    # db.session.add(post10)
    # db.session.add(post11)
    # db.session.add(post12)
    # db.session.add(post13)
    # db.session.add(post14)
    # db.session.add(post15)
    # db.session.add(post16)
    # db.session.add(post17)
    # db.session.add(post18)
    # db.session.add(post19)
    db.session.commit()
