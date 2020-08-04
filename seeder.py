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
    post3 = Post(
        body="Nam pulvinar magna et viverra ultrices. Curabitur a mauris quis tortor euismod tincidunt sed a neque. Aliquam vestibulum congue velit eu placerat. Ut lacinia augue ut placerat tristique. Pellentesque sed auctor augue. Fusce sit amet ligula malesuada, tempus velit eget, bibendum ligula. Suspendisse ut sapien molestie, finibus massa et, luctus risus. Cras vel risus commodo turpis luctus facilisis. In ultrices lacus vel posuere rhoncus. Nam at odio quis purus ultrices molestie. Cras efficitur porta velit ac malesuada. Proin sit amet feugiat nulla.         ![](https: // 66.media.tumblr.com/c88a2430f1cd069c2c2150a912fa7188/tumblr_oan0kndgxU1r4ltwho1_1280.png)         ![](https: // 66.media.tumblr.com/61aed172599c3aeec5418088d279245f/tumblr_ofqinzMCO11r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 1, day: 20)
    )
    post4 = Post(
        body="Curabitur id turpis at quam vulputate fringilla vitae in lectus. Nulla mi nisl, pellentesque ac semper sed, iaculis et tortor. Nam iaculis sem placerat dolor tristique ornare sed eget nulla. Nulla facilisi. Vestibulum mollis justo felis, ac fringilla odio tincidunt at. Etiam vestibulum ante felis. Integer ac aliquam ante, nec lobortis risus. Fusce dictum nisl a diam tincidunt iaculis. Praesent accumsan turpis quis pretium varius. Pellentesque dignissim, nunc et tempus dictum, velit ligula sodales nisi, a lacinia arcu quam ut massa. Nulla eu laoreet erat, quis pretium nibh.         ![](https: // 68.media.tumblr.com/adfcfc9ac947ee9616391e32612650a2/tumblr_oj56b9FCcM1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 2, day: 11)
    )
    post5 = Post(
        body="Donec iaculis metus sit amet tellus feugiat, ac commodo dui tristique. Nunc nulla felis, mollis fermentum dapibus ultricies, molestie ut lorem. Ut congue pretium felis commodo volutpat. Sed in finibus purus. Etiam dictum urna lacus, vel pretium nunc porttitor vel. In laoreet blandit dui, feugiat faucibus enim condimentum et. Integer egestas fringilla justo, eget lobortis orci lobortis nec. Proin a tellus in nibh tempor porta vel sed mauris. In hac habitasse platea dictumst. Morbi luctus turpis porttitor, mollis odio sit amet, vestibulum nibh. Vestibulum eget fringilla libero, et consequat turpis. Curabitur convallis turpis nec massa malesuada, imperdiet cursus enim lacinia. Quisque sollicitudin, dui vel eleifend ultrices, ex neque elementum dolor, ac tempor leo nulla non orci.         ![](https: // 68.media.tumblr.com/ae44b24f3aba9bbcf1a0686bda94796c/tumblr_ok30mbsMRz1r4ltwho1_500.png)         ![](https: // 78.media.tumblr.com/8431461077bccf604fb798ee6704622f/tumblr_oxulrcjVHW1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 2, day: 24)
    )
    post6 = Post(
        body="Etiam interdum arcu ac turpis gravida lacinia. Curabitur ornare volutpat libero sed iaculis. Mauris nec leo non dolor suscipit vestibulum. Donec consectetur malesuada egestas. Vivamus vestibulum bibendum cursus. Praesent placerat tellus sed urna efficitur, sed pharetra urna vestibulum. Suspendisse potenti.         ![](https: // 78.media.tumblr.com/62a1a9781012144a92df3d357d1029e7/tumblr_p2qtagLXWG1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 3, day: 9)
    )
    post7 = Post(
        body="Praesent condimentum, eros vitae viverra fermentum, quam eros pulvinar urna, ac ornare nunc lorem ut ipsum. Sed eu interdum sem. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae        Nullam accumsan leo nec accumsan accumsan. Nullam placerat massa commodo est cursus, nec euismod enim facilisis. Vivamus a neque varius, ultricies enim volutpat, tincidunt odio. Curabitur purus dolor, varius vitae dignissim vitae, venenatis vel turpis. Praesent ac dui in urna vulputate sollicitudin. ![](https: // 78.media.tumblr.com/91f71502727c3a0afd03ac891117ab9c/tumblr_p3iknq8hMN1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 3, day: 19)
    )
    post8 = Post(
        body="Suspendisse et eros ut augue fringilla volutpat sit amet id sapien. Nunc imperdiet sodales mauris, a hendrerit lorem vehicula eget. Nam fringilla, tortor et sagittis porta, lacus purus porttitor dui, id molestie velit arcu in sapien. Suspendisse mi dui, scelerisque fringilla feugiat sed, sagittis ac elit. Ut ante dui, tristique at tincidunt eget, iaculis ut quam. Cras hendrerit leo a elit aliquam consectetur a vehicula justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae        Curabitur sodales nibh et ipsum maximus cursus. Donec nec elit et ex lobortis placerat. ![](https: // 78.media.tumblr.com/b7f3cc6599b1b37fcb2262630ef3c1a3/tumblr_pc8xkwTa2E1r4ltwho1_540.png) ![](https: // 78.media.tumblr.com/c564c8939fc855a3d9a20e25fa847d32/tumblr_pcb6jfmopg1r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 4, day: 10)
    )
    post9 = Post(
        body="Vestibulum dignissim rutrum sagittis. Nunc interdum volutpat turpis, non accumsan metus dignissim id. Duis est massa, efficitur interdum condimentum ut, tempus nec lacus. Vestibulum gravida hendrerit nulla sit amet venenatis. Aenean a metus laoreet, sollicitudin nulla vel, molestie metus. Proin ligula lorem, pellentesque eu ullamcorper vel, varius et lacus. Nunc vel viverra sapien. Ut aliquam volutpat velit vitae posuere. Suspendisse non tempor enim. Etiam efficitur arcu non lacus egestas, sit amet eleifend arcu auctor. In porttitor, odio vel molestie fringilla, libero orci egestas nisl, nec lacinia lorem nunc et dui. Suspendisse potenti.         ![](https: // 66.media.tumblr.com/e895da808fbbfd1ee07218cf0c65cbce/tumblr_pn5wqrz6S71r4ltwho1_1280.png)         ![](https: // 66.media.tumblr.com/f05c260b95bead649f6487f58a26b326/tumblr_ppblco8Sv71r4ltwho2_1280.png)         ![](https: // 66.media.tumblr.com/ba2c5d5beb07f9ebfcda2cf1af005ea5/tumblr_ppblco8Sv71r4ltwho1_1280.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 5, day: 13)
    )
    post10 = Post(
        body="Cras elit felis, ultrices vel arcu ut, gravida hendrerit quam. Aliquam laoreet vestibulum mauris eget feugiat. Suspendisse congue quis sapien posuere hendrerit. Mauris sit amet blandit augue. Proin porta libero nulla, eu commodo metus gravida a. Quisque vehicula, massa quis feugiat malesuada, nisi ante ultricies turpis, a sollicitudin neque odio nec dolor. Vestibulum at imperdiet dui. Aliquam et congue lorem. Sed tincidunt imperdiet tellus eu posuere. Donec placerat elementum urna id iaculis. Nulla facilisi. Vestibulum ipsum neque, sollicitudin eu risus ac, efficitur laoreet lectus. ![](https: // 66.media.tumblr.com/8a9f141952b77e3fee953c71628ce1c8/tumblr_opbgjv1dOF1r4ltwho1_640.png)",
        sketchbook_id=1,
        user_id=1,
        timestamp=datetime(year: 2020, month: 6, day: 16)
    )

    db.session.add(user1)
    db.session.add(skb1)
    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.commit()
