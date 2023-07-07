from flask import render_template, request, Blueprint, jsonify, make_response, flash, redirect, url_for
from yocosmos import db, limiter
from yocosmos.models import Post, Liker
from yocosmos.main.forms import ContactForm
from yocosmos.main.utils import send_contact_email
from flask_limiter.util import get_remote_address
from sqlalchemy import func

import time
import json

main = Blueprint('main', __name__)


# @main.route("/")
# def home():
#posts = Post.query.all()

#    page = request.args.get('page', 1, type=int)
#    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
#    return render_template('home.html', posts=posts)


@main.route("/")
def home():
    #posts = Post.query.all()
    return render_template('home.html')


@main.route("/like/<int:id>", methods=["POST"])
@limiter.limit("1000/hour")
def like(id):
    address = get_remote_address()
    #print("HONK")
    likerquery = db.session.query(Liker).filter(Liker.ip_address == address, Liker.post_id == id).all()
    if(likerquery != []):
        return ""
    else:
        liker = Liker(ip_address=address, post_id=id)
        db.session.add(liker)
        db.session.commit()
        return ""
    

@main.route("/unlike/<int:id>", methods=["POST"])
@limiter.limit("1000/hour")
def unlike(id):
    address = get_remote_address()
    #print("DIMANCHE")
    likerquery = db.session.query(Liker).filter(Liker.ip_address == address, Liker.post_id == id).all()
    if(likerquery == []):
        return ""
    else:
        db.session.delete(likerquery[0])
        db.session.commit()
    return ""


@main.route("/load")
def load():
    """ Route to return the posts """

    time.sleep(0.2)     # Used to simulate delay
    quantity = 10       # Number of posts to return at a time
    postcount = Post.query.order_by(Post.date_posted.desc()).first().id

    if request.args:
        # The 'counter' value sent in the QS
        pagecounter = int(request.args.get("c"))

        if pagecounter == 0:
            print(f"Returning page {pagecounter}")
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=1, per_page=10).items
            data = {'posts': [], 'likes': []}
            for c in posts:
                data['likes'].append(len(c.likers))
                data['posts'].append(json.dumps(c.to_dict()))
            # print(json.dumps(data))
            res = make_response(json.dumps(data), 200)

        elif (pagecounter * 10) >= postcount:
            print("No more posts")
            res = make_response(jsonify({}), 200)

        else:
            print(f"Returning page {pagecounter}")
            posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=(pagecounter+1), per_page=10).items
            # insert here = get like counts for these 10 posts and send in the data
            # make a new data = {'posts': []; 'likes': []} or something like that
            data = {'posts': [], 'likes': []}
            for c in posts:
                data['likes'].append(len(c.likers))
                data['posts'].append(json.dumps(c.to_dict()))
            # print(json.dumps(data))
            res = make_response(json.dumps(data), 200)

        return res
    else:
        return


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/privacy_policy")
def privacy_policy():
    return render_template('privacy-policy.html')


@main.route("/terms_of_service")
def terms_of_service():
    return render_template('terms-of-service.html')

# @main.route("/contact")
# def contact():
#    return render_template('contact.html')


@main.route("/contact", methods=['POST'])
@limiter.limit("5/hour")
@limiter.limit("20/day")
def contact_post():
    form = ContactForm()
    if form.validate_on_submit():
        send_contact_email(form.name.data, form.email.data, form.content.data)
        flash(f'Your message has been sent to the website administrators.', 'success')
        return redirect(url_for('main.home'))
    flash(f'There was an error sending your message. Please check your formatting and try again.', 'danger')
    return render_template('contact.html', title='Contact Form', form=form, legend='Contact Form')


@main.route("/contact", methods=['GET'])
def contact_get():
    form = ContactForm()
    return render_template('contact.html', title='Contact Form', form=form, legend='Contact Form')
