from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField 
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    content = TextAreaField('', validators=[DataRequired(), Length(min=1, max=5000)])
    submit = SubmitField('Submit Post')


