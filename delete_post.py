from yocosmos import create_app, db
from yocosmos.models import Post
import sys

app = create_app()
app.app_context().push()

def delete_post(post_id):
    post = Post.query.get(post_id)

    if post:
        db.session.delete(post)
        db.session.commit()
        print(f"Post with id {post_id} deleted successfully!")
    else:
        print(f"No post found with id {post_id}")

if __name__ == "__main__":
    post_id = int(sys.argv[1])
    delete_post(post_id)
