# the new date should be passed as a string in the format 'YYYY-MM-DD HH:MM:SS'

from yocosmos import create_app, db
from yocosmos.models import Post
from datetime import datetime
import sys

app = create_app()
app.app_context().push()

def edit_post_date(post_id, new_date):
    post = Post.query.get(post_id)

    if post:
        post.date_posted = datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S')
        db.session.commit()
        print(f"Post date edited successfully!")
    else:
        print(f"No post found with id {post_id}")

if __name__ == "__main__":
    post_id = int(sys.argv[1])
    new_date = sys.argv[2]
    edit_post_date(post_id, new_date)
