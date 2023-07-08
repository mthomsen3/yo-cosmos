import sys
import random
import os
sys.path.append(os.path.abspath(os.path.join('..')))

from yocosmos import create_app, db
from yocosmos.models import Post, Liker
from datetime import datetime
import random
app = create_app()
app.app_context().push()
db.create_all()

db.session.commit()

avatar_directory = 'yocosmos/static/avatars/'
avatar_filenames = os.listdir(avatar_directory)



temp_ip = '127.0.0.1'

post0 = Post(content='Yo, Cosmos!', user_ip=temp_ip, date_posted = datetime(1995, 1, 16, 7, 10), avatar_image = random.choice(avatar_filenames)) 
db.session.add(post0)

post1 = Post(content='I can\'t tell whether the \'birds aren\'t real\' movement is ironic or serious', user_ip=temp_ip, date_posted = datetime(1995, 1, 21, 17, 52), avatar_image = random.choice(avatar_filenames))
db.session.add(post1)

post2 = Post(content='BIRDS AREN\'T REAL MAN JUST ACCEPT IT', user_ip=temp_ip, date_posted = datetime(1995, 2, 7, 13, 34), avatar_image = random.choice(avatar_filenames))
db.session.add(post2)

post3 = Post(content='Shout out to Mr. Burt and his fantastic Bees', user_ip=temp_ip, date_posted = datetime(1995, 2, 9, 14, 48), avatar_image = random.choice(avatar_filenames))
db.session.add(post3)

post4 = Post(content='Why is it harder to fall asleep when you need to fall asleep? Or is that just me?', user_ip=temp_ip, date_posted = datetime(1995, 2, 18, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post4)

post5 = Post(content='Is my cold resistance weakening with age? I hope not.', user_ip=temp_ip, date_posted = datetime(1995, 2, 19, 8, 30), avatar_image = random.choice(avatar_filenames))
db.session.add(post5)

post6 = Post(content='I would gladly pay you Tuesday for a 🍔 today', user_ip=temp_ip, date_posted = datetime(1995, 3, 1, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post6)

post7 = Post(content='I\'m not wearing matching socks', user_ip=temp_ip, date_posted = datetime(1995, 3, 2, 20, 20), avatar_image = random.choice(avatar_filenames))
db.session.add(post7)

post8 = Post(content='I am Captain Gloob. One day the world shall know my name. Captain Gloob!', user_ip=temp_ip, date_posted = datetime(1995, 3, 4, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post8)

post9 = Post(content='https://www.youtube.com/watch?v=9qoXa5_w3Gw', user_ip=temp_ip, date_posted = datetime(1995, 3, 6, 15, 12), avatar_image = random.choice(avatar_filenames))
db.session.add(post9)

post10 = Post(content='Are we alone in the universe? 🤔 Crap, my toaster is on...', user_ip=temp_ip, date_posted = datetime(1995, 3, 15, 20, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post10)

post11 = Post(content='I was Joan of Arc in a former life', user_ip=temp_ip, date_posted = datetime(1995, 3, 22, 11, 11), avatar_image = random.choice(avatar_filenames))
db.session.add(post11)

post12 = Post(content='Snatch is an excellent film. Go see it if you haven\'t', user_ip=temp_ip, date_posted = datetime(1995, 4, 4, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post12)

post13 = Post(content='NSFW post \n \n \n \n jk', user_ip=temp_ip, date_posted = datetime(1995, 4, 5, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post13)

post14 = Post(content='Don\'t👏 pretend👏 to 👏be 👏entitled👏 to👏 financial👏 compensation👏 if 👏you 👏or👏 a👏 loved 👏one 👏hasn\'t👏 even 👏been 👏diagnosed👏 with 👏mesothelioma', user_ip=temp_ip, date_posted = datetime(1995, 5, 1, 22, 56), avatar_image = random.choice(avatar_filenames))
db.session.add(post14)

post15 = Post(content='Post 15', user_ip=temp_ip, date_posted = datetime(1995, 5, 5, 15, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post15)

post16 = Post(content='\'I didn\'t really say everything I said.\' -Yogi Berra', user_ip=temp_ip, date_posted = datetime(1995, 5, 19, 17, 20), avatar_image = random.choice(avatar_filenames))
db.session.add(post16)

post17 = Post(content='yocosmos.com', user_ip=temp_ip, date_posted = datetime(1995, 6, 11, 23, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post17)

post18 = Post(content='Do you even lift?', user_ip=temp_ip, date_posted = datetime(1995, 6, 27, 17, 55), avatar_image = random.choice(avatar_filenames))
db.session.add(post18)

post19 = Post(content='Gotta Catch \'em All', user_ip=temp_ip, date_posted = datetime(1995, 7, 1, 11, 22), avatar_image = random.choice(avatar_filenames))
db.session.add(post19)

post20 = Post(content='If my girl👧😍 and my beyblades💯🔥 are both drowning🌊😦 and I could only save one😄☝️you can catch me letting it rip😤 at my girl’s funeral😅👻💀 cause it’s bey blade or catch a fade🙏👊😠💯😭', user_ip=temp_ip, date_posted = datetime(1995, 7, 3, 12, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post20)

post21 = Post(content='Try to take away my chicken wings? Cluck around and find out.', user_ip=temp_ip, date_posted = datetime(1995, 7, 5, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post21)

post22 = Post(content='The Office is an American mockumentary sitcom television series that depicts the everyday work lives of office employees at the Scranton, Pennsylvania, branch of the fictional Dunder Mifflin Paper Company. It aired on NBC from March 24, 2005, to May 16, 2013, spanning a total of nine seasons.[1] Based on the 2001–2003 BBC series of the same name created by Ricky Gervais and Stephen Merchant, it was adapted for American television by Greg Daniels, a veteran writer for Saturday Night Live, King of the Hill, and The Simpsons. It was co-produced by Daniels\'s Deedle-Dee Productions and Reveille Productions (later Shine America), in association with Universal Television. The original executive producers were Daniels, Gervais, Merchant, Howard Klein, and Ben Silverman, with numerous others being promoted in later seasons.', user_ip=temp_ip, date_posted = datetime(1995, 7, 9, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post22)

post23 = Post(content='Jim Halpert is a bully.', user_ip=temp_ip, date_posted = datetime(1995, 9, 1, 13, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post23)

post24 = Post(content='Has Anyone Really Been Far Even as Decided to Use Even Go Want to do Look More Like?', user_ip=temp_ip, date_posted = datetime(1995, 9, 3, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post24)

post25 = Post(content='https://www.youtube.com/watch?v=nwP3TeK-fPs', user_ip=temp_ip, date_posted = datetime(1995, 10, 5, 10, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post25)

post26 = Post(content='Am I a cat person, or just a lazy dog person?', user_ip=temp_ip, date_posted = datetime(1995, 10, 13, 9, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post26)

post27 = Post(content='This isn\'t my dad, it\'s a website. Time to throw this thing on the ground.', user_ip=temp_ip, date_posted = datetime(1995, 10, 23, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post27)

post28 = Post(content='Jeff Bezos has 121 BILLION dollars. The population of earth is 7 billion people. He could give every person 1 BILLION dollars and end poverty, and he would still have 114 billion dollars left over but he would do it. This is what capitalist greed looks like!', user_ip=temp_ip, date_posted = datetime(1995, 10, 30, 2, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post28)

post29 = Post(content='Test Post. Do not move during the duration of the Test Post.', user_ip=temp_ip, date_posted = datetime(1995, 11, 2, 17, 40), avatar_image = random.choice(avatar_filenames))
db.session.add(post29)

post30 = Post(content='I wonder how much light pollution is caused by Christmas lights', user_ip=temp_ip, date_posted = datetime(1995, 11, 30, 19, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post30)

post31 = Post(content='Young Gun Silver Fox is a really good band. Very underrated.', user_ip=temp_ip, date_posted = datetime(1995, 12, 24, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post31)

post32 = Post(content='Happy Birthday!', user_ip=temp_ip, date_posted = datetime(1995, 12, 25, 11, 37), avatar_image = random.choice(avatar_filenames))
db.session.add(post32)

post33 = Post(content='In Japan 🇯🇵 , heart surgeon ❤️👨‍⚕️ . Number one 😭☝️ . Steady hand😳✋️. One day, Yakuza boss 🙇🏻need 🆕 heart💘. I do operation🔪⚔️. But, mistake😱! Yakuza boss die😵😪! Yakuza very mad👿. I hide🙈 in fishing boat🐟🚣🏻‍♀️, come to America🎇🎊🇺🇸. No english🤐, no food😩, no money📉🚫💲. Darryl 👨🏿give me job🙌👨🏻‍💼. Now I have house🏡, American car 🚗 , and new woman 🆕👱🏻‍♀️. Darryl 👨🏿save life⛑. My big secret🙊: I kill ☠️yakuza boss on purpose😈. I good 👍surgeon. The best👌💯!', user_ip=temp_ip, date_posted = datetime(1995, 12, 27, 12, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post33)

post34 = Post(content='Yo Cosmos is live!', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 0, 51, 11), avatar_image = random.choice(avatar_filenames))
db.session.add(post34)

post35 = Post(content='Why do British people pronounce the word "clerk" like "Clark"? And why does it bug me so much?', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 0, 51, 59), avatar_image = random.choice(avatar_filenames))
db.session.add(post35)

post36 = Post(content='I finally have access to a family cookie recipe that was kept secret for decades! Now attempting to make the recipe ‘my own’ with a few changes…', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 1, 13, 59), avatar_image = random.choice(avatar_filenames))
db.session.add(post36)

post37 = Post(content="We're nearly out of Hanukkah candles here, and it's not even half way through. Sort of appropriate though, wouldn't you say?", user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 1, 17, 18), avatar_image = random.choice(avatar_filenames))
db.session.add(post37)

post38 = Post(content='I can put my whole fist in my mouth.', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 1, 50, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post38)

post39 = Post(content='YO cosmos', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 1, 53, 40), avatar_image = random.choice(avatar_filenames))
db.session.add(post39)

post40 = Post(content="When it's 1 AM and you tell someone you're going to bed and they respond “why so early?”… it may be a sign you have a problem", user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 6, 49, 32), avatar_image = random.choice(avatar_filenames))
db.session.add(post40)

post41 = Post(content='I never really pondered the name “dry ice” before today. It doesn’t melt, so it’s not wet. Dry ice. Only took me a couple decades to make that connection.', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 8, 33, 15), avatar_image = random.choice(avatar_filenames))
db.session.add(post41)

post42 = Post(content='I wonder how many of my “first time revelations” are really just “things I definitely once knew but completely forgot about”', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 17, 23, 17), avatar_image = random.choice(avatar_filenames))
db.session.add(post42)

post43 = Post(content='TIL of the term “first amendment auditors”', user_ip=temp_ip, date_posted = datetime(2022, 12, 22, 18, 49, 6), avatar_image = random.choice(avatar_filenames))
db.session.add(post43)

post44 = Post(content="There's no such thing as a non sexual banana", user_ip=temp_ip, date_posted = datetime(2022, 12, 23, 4, 59, 4), avatar_image = random.choice(avatar_filenames))
db.session.add(post44)

post45 = Post(content='If you took a vacuum sealed dry aged steak and stored it in a laboratory-grade freezer at -80C, would it still taste good in 30 years? We could have results as soon as 2052…', user_ip=temp_ip, date_posted = datetime(2022, 12, 25, 20, 24, 20), avatar_image = random.choice(avatar_filenames))
db.session.add(post45)

post46 = Post(content='There was a time in my life when I could identify types of cloud by name. That time is gone, the information lost. It was a short time.', user_ip=temp_ip, date_posted = datetime(2022, 12, 26, 0, 54, 34), avatar_image = random.choice(avatar_filenames))
db.session.add(post46)

post47 = Post(content='In a sufficiently advanced structure that is capable of rapid molecular rearrangement, one could imagine a ‘turbolift’-style system wherein the building creates a human-sized open cavity facing into the departure room, which closes around the occupant once entered and shifts them in 3D space to whatever destination room is ready to accept them. This would obfuscate the need for elevator banks. Claustrophobics would be advised to take the stairs…', user_ip=temp_ip, date_posted = datetime(2022, 12, 26, 3, 56, 32), avatar_image = random.choice(avatar_filenames))
db.session.add(post47)

post48 = Post(content='Today I came to a mental truce with the number 6. Finally! Merry Christmas!', user_ip=temp_ip, date_posted = datetime(2022, 12, 26, 4, 1, 27), avatar_image = random.choice(avatar_filenames))
db.session.add(post48)

post49 = Post(content='Made a breakfast sandwich with an English muffin, homemade sausage patty, homemade Big Mac sauce, shrettuce, and American cheese. 10/10.', user_ip=temp_ip, date_posted = datetime(2022, 12, 27, 13, 25, 17), avatar_image = random.choice(avatar_filenames))
db.session.add(post49)

post50 = Post(content="I think I'm slowly replacing all the knowledge I stored in graduate school with The Office trivia. Send help.", user_ip=temp_ip, date_posted = datetime(2022, 12, 30, 2, 42, 59), avatar_image = random.choice(avatar_filenames))
db.session.add(post50)

post51 = Post(content='Useless superpower idea: when you pour soda, it never fizzes over the rim of the glass you’re pouring into (but it still retains optimal carbonation levels)', user_ip=temp_ip, date_posted = datetime(2023, 1, 24, 19, 6, 51), avatar_image = random.choice(avatar_filenames))
db.session.add(post51)


db.session.commit()





post1 = Post.query.get(1)
liker1 = Liker(ip_address='1.1.1.1', post_id=post1.id)
db.session.add(liker1)


from itertools import cycle

# Define IP address generator
def ip_generator(start, end):
    for i in range(start, end + 1):
        yield f'{i}.{i}.{i}.{i}'

# Prepare a list of posts to have likes
posts_to_have_likes = [1, 2, 5, 7, 10, 13, 15, 18, 21, 23, 26, 29, 31, 34, 37, 39, 42, 45, 47, 50, 51]

# Cycle through the list of likes (0 to 3)
like_counts = cycle([1, 2, 1, 3, 1, 1, 2, 3, 1, 2, 1, 3, 1, 1, 2])

# Generate IP addresses
ip_gen = ip_generator(34, 83)

for post_id in posts_to_have_likes:
    # Get the post
    post = Post.query.get(post_id)

    # Determine the number of likes for this post
    like_count = next(like_counts)

    # Add likes
    for _ in range(like_count):
        liker = Liker(ip_address=next(ip_gen), post_id=post.id)
        db.session.add(liker)




db.session.commit()





