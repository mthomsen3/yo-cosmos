from datetime import datetime
from yocosmos import db
from sqlalchemy_serializer import SerializerMixin


class Post(db.Model, SerializerMixin):
    __tablename__ = 'post'

    serialize_only = ('id', 'date_posted', 'content')

    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_ip = db.Column(db.Text, nullable=False)
    likers = db.relationship("Liker", backref='post')

    def __repr__(self):
        return f"Post('{self.id}')"


class Liker(db.Model):
    __tablename__ = "likers"
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    #liker = db.relationship("Post", back_populates="likers")
