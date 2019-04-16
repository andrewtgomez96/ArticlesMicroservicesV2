from flask import Flask, request, jsonify
#import sqlite3
import datetime
from rfeed import *
import requests

#Create the flask app
app = Flask(__name__)

#Max Number of articles the RSS feed will return
COUNT = 10

#RSS MicroService to fetch the 10 most recent articles
@app.route("/articles/rss")
def rss():
    #List that will hold articles
    items = []
    #The format of an Item object given by rfeed
    item = Item(
            title = "NEW Sample Articles 54",
            link = "example.com/articles/2",
            description = "Sample Article",
            author = "EM",
            pubDate = datetime.datetime.now())

    #access the articles microservice
    link = "http://localhost/articles/" + str(COUNT)
    rArticles = requests.get(link)

    #Check if got an 'OK' status to conntinue
    if rArticles.status_code == 200:
        print("Connection Establish")
    else:
        print("FAILED Connection ",rArticles.status_code) 

    items.append(item)

    #Retrive atricles metadata from articles microserice
    link = "http://localhost/articles/" + str(COUNT)
    rInfoArticles = requests.get(link)

    #Check if established connection
    if rInfoArticles.status_code == 200:
        print('Establish Connection')
    else:
        print("Failed connection ", rInfoArticles.status_code)

    #Start creating RSS articles
    #data = rArticles.json()
    #for articles in data:
    #    print(articles)

    #Title of the RSS feed given by rfeee
    feed = Feed(
            title = "Articles RSS Feed",
            link = "http://localhost/Article",
            description = "A summary feed for the 10 most recent articles",
            language = "en-US",
            lastBuildDate = datetime.datetime.now(),
            items = items)

    return feed.rss()
