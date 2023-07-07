from yocosmos import create_app, db
from yocosmos.models import Post, Liker
import json

app = create_app()
app.app_context().push()

def backup_database():
    posts = Post.query.all()
    likers = Liker.query.all()

    posts_data = [post.to_dict() for post in posts]
    likers_data = [liker.to_dict() for liker in likers]

    with open('backup_posts.json', 'w') as f:
        json.dump(posts_data, f)

    with open('backup_likers.json', 'w') as f:
        json.dump(likers_data, f)

    print("Database backed up successfully!")

if __name__ == "__main__":
    backup_database()
