from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


class AddImage(FlaskForm):
    picture = FileField('Update Profile Picture',
                        validators=[FileAllowed(['jpeg', 'jpg', 'png'])])


class AddParagraph(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])
