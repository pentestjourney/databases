"""Forms for playlist app."""

from wtforms import SelectField, StringField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, NumberRange, Optional


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Playlist Name', validators=[Length(min=1, max=30), InputRequired()], )
    description = TextAreaField('Playlist Description', validators=[Length(min=1, max=55), Optional()])



class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField("Song Title", validators=[Length(min=1, max=100), InputRequired()])
    artist = StringField("Artist", validators=[Length(min=1, max=100), InputRequired()])



class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
