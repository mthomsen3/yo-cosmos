from yocosmos import create_app, db
from yocosmos.models import Post
import sys

app = create_app()
app.app_context().push()

def replace_post_content(post_id, new_content):
    post = Post.query.get(post_id)

    if post:
        post.content = new_content
        db.session.commit()
        print(f"Post content replaced successfully!")
    else:
        print(f"No post found with id {post_id}")

if __name__ == "__main__":
    post_id = int(sys.argv[1])
    new_content = sys.argv[2]
    replace_post_content(post_id, new_content)
