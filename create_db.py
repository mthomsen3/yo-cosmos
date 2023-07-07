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

post27 = Post(content='This isn\'t my dad, it\'s a website. Time to throw this bitch on the ground.', user_ip=temp_ip, date_posted = datetime(1995, 10, 23, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post27)

post28 = Post(content='Jeff Bezos has 121 BILLION dollars. The population of earth is 7 billion people. He could give every person 1 BILLION dollars and end poverty, and he would still have 114 billion dollars left over but he would do it. This is what capitalist greed looks like!', user_ip=temp_ip, date_posted = datetime(1995, 10, 30, 2, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post28)

post29 = Post(content='Rolled my first joint today. So that\'s cool.', user_ip=temp_ip, date_posted = datetime(1995, 11, 2, 17, 40), avatar_image = random.choice(avatar_filenames))
db.session.add(post29)

post30 = Post(content='I wonder how much light pollution is caused by Christmas lights', user_ip=temp_ip, date_posted = datetime(1995, 11, 30, 19, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post30)

post31 = Post(content='Young Gun Silver Fox is a really good band. Very underrated.', user_ip=temp_ip, date_posted = datetime(1995, 12, 24, 17, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post31)

post32 = Post(content='Happy Birthday!', user_ip=temp_ip, date_posted = datetime(1995, 12, 25, 11, 37), avatar_image = random.choice(avatar_filenames))
db.session.add(post32)

post33 = Post(content='In Japan 🇯🇵 , heart surgeon ❤️👨‍⚕️ . Number one 😭☝️ . Steady hand😳✋️. One day, Yakuza boss 🙇🏻need 🆕 heart💘. I do operation🔪⚔️. But, mistake😱! Yakuza boss die😵😪! Yakuza very mad👿. I hide🙈 in fishing boat🐟🚣🏻‍♀️, come to America🎇🎊🇺🇸. No english🤐, no food😩, no money📉🚫💲. Darryl 👨🏿give me job🙌👨🏻‍💼. Now I have house🏡, American car 🚗 , and new woman 🆕👱🏻‍♀️. Darryl 👨🏿save life⛑. My big secret🙊: I kill ☠️yakuza boss on purpose😈. I good 👍surgeon. The best👌💯!', user_ip=temp_ip, date_posted = datetime(1995, 12, 27, 12, 10), avatar_image = random.choice(avatar_filenames))
db.session.add(post33)

db.session.commit()





post1 = Post.query.get(1)
liker1 = Liker(ip_address='1.1.1.1', post_id=post1.id)
db.session.add(liker1)

db.session.commit()





