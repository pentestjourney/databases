from app import app
from models import db, connect_db, Playlist, Song, PlaylistSong


db.drop_all()
db.create_all()