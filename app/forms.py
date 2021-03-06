from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchPlaylist(FlaskForm):
    playlist_url = StringField('Playlist URL', validators=[DataRequired()])
    submit = SubmitField('SEARCH')