import sys
import os
sys.path.append(os.path.abspath(os.path.join('..')))

from yocosmos import create_app, db
from yocosmos.models import Post
from datetime import datetime
app = create_app()
app.app_context().push()
db.drop_all()