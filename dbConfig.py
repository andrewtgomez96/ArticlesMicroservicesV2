from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from app import db
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/student/proj2/articles/usersDB.db'
app.config['SQLALCHEMY_BINDS'] = {'articles' : 'sqlite://///home/student/proj2/articles/articlesDB.db',
                                    'tags' : 'sqlite://///home/student/proj2/articles/tagsDB.db',
                                    'comments' : 'sqlite://///home/student/proj2/articles/commentsDB.db'}

db = SQLAlchemy(app)
class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(25))
    password = db.Column(db.String(25))

class Articles(db.Model):
    __bind_key__ = "articles"
    username = db.Column(db.String(25))
    artId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40))
    body = db.Column(db.String(240))
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

class Tags(db.Model):
    __bind_key__ = "tags"
    tagId = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20))
    artId = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    author = db.Column(db.String(25), default="anonymous coward")

class Comments(db.Model):
    __bind_key__ = "comments"
    commendId = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(180))
    artId = db.Column(db.Integer)
    created = db.Column(db.DateTime)
    author = db.Column(db.String(25), default="anonymous coward")
