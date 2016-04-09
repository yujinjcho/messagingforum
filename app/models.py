from datetime import datetime

from app import db


class User(db.Model):
  #__tablename__ = 'users'

  id = db.Column(db.String, nullable=False, primary_key=True)
  created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
                      onupdate=datetime.utcnow)
  name = db.Column(db.String, nullable=False)
  profile_url = db.Column(db.String, nullable=False)
  access_token = db.Column(db.String, nullable=False)
  posts = db.relationship('Post', backref='user', lazy='dynamic')


class Post(db.Model):
	#__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	author_id = db.Column(db.String, db.ForeignKey('user.id'))
	text = db.Column(db.String(140), nullable=False)
	author = db.Column(db.String, nullable=False)