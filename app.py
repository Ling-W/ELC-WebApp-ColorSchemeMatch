# coding: utf-8

import os
from flask import Flask, render_template, request, redirect, url_for
#from flask_mysqldb import MySQL
from peewee import *
from wtforms import Form, StringField , TextAreaField ,PasswordField , validators
import logging
database = MySQLDatabase(os.environ['MYSQL_DATABASE'], 
                            host=os.environ['MYSQL_HOST'], 
                            port=int(os.environ['MYSQL_PORT']),
                            user=os.environ['MYSQL_USER'], 
                            password=os.environ['MYSQL_PASSWORD'])
import sys
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'MyDB'

# mysql = MySQL(app)

class BaseModel(Model):
    class Meta:     
        database = database

class Table(BaseModel):
    column1 = CharField()
    column2 = CharField()    
    created_at = DateTimeField()
    updated_at = DateTimeField(null=True)                              
        
app = Flask(__name__)


database.connect()
#Result form class
class Song:
    def __init__(self, id, name, artist, link, img):
        self.id = id
        self.name  = name
        self.artist = artist
        self.link = link
        self.img = img

class Note:
    def __init__(self, id, name, img):
        self.id = id
        self.name  = name
        self.img = img


#Mock dataset of songs
songs = []
for i in range(9):
    song = Song(i, "song_{}".format(i), "Taylor Swift","https://soundcloud.com/taylorswiftofficial/i-did-something-bad", 'https://i1.sndcdn.com/artworks-NMKb89tCPSQP-0-t500x500.jpg')
    songs.append(song)


note_lst = ['CITRUS',
'FLORAL',
'FOUGERE',
'GREEN',
'LEATHER',
'MUSK',
'ORIENTAL',
'TOBACCO',
'WOODS']
notes = []
notes_dict = {}
for i, n in enumerate(note_lst):
    note = Note(i, n,'https://www.google.com/search?q=citrus&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijufrcvtHjAhVkTt8KHR1UC9MQ_AUIESgB&cshid=1564106619008256&biw=1680&bih=939#imgrc=D6mKxRRc4-Rz1M:' )
    notes.append(note)
    notes_dict[i] = n
    
genre = ['Country','Jazz','Ambient', 'Acoustic', 'Disco','Hip-hop', 'rap','Heavy Metal', 'Classical']
genre = dict(enumerate(genre))

song_notes = dict(zip([song.id for song in songs],notes))

notes_genre = dict(zip(notes, genre))
@app.route("/")
def hello():
    
    
    '''
    #cursor = database.excecute()
    #results = cur.excecute("SELECT * FROM songs")
    #songs = cur.fetchall()
    if result > 0:
        return render_template('index.html',songs = songs)
    else:
        msg = 'no songs found!'
        return render_template('index.html', msg = msg)
    cur.close()
    '''
    return render_template('songs.html', songs = songs)
    #return render_template('category.html')
    
@app.route("/category")
def category():
    if request.method == 'GET':
        return ''

    else:
        return render_template('category.html')


@app.route("/song/<int:id>")
def song(id):
    for song in songs:
        if song.id == id:
            return redirect(song.link)
    return "Song not found!"


@app.route("/songs", methods = ['POST', 'GET'])
def select_song():
    if request.method == 'GET':
        #songs = request.args.getlist('songs[]')
        #url = "/notes/{}/{}/{}".format(songs[0],songs[1],songs[2])
        #return redirect(url)
        result = []
        for song in songs:
            if str(song.id) in request.args:
                result += [str(song.id)]
        url = "/notes/{}/{}/{}".format(result[0],result[1],result[2])
        return redirect(url)

      
       
    else:
        '''
        #get to the fragrance.
        return redirect('fragrance')
        '''
        return render_template("recommendaton.html",fragrance = fragrance)


@app.route("/notes/<int:song1>/<int:song2>/<int:song3>")
def get_notes(song1,song2,song3):
    if request.method =='GET':
        note1 = song_notes[int(song1)]
        note2 = song_notes[int(song2)]
        note3 = song_notes[int(song3)]
        return render_template("album.html", note1 = note1, note2 = note2, note3 = note3)


@app.route("/fragrance/<int:note1>/<int:note2>/<int:note3>")
def direct_fragrance(note1,note2,note3):
    base_url = 'https://www.tomford.com/beauty/fragrance/'
    selection = '#prefn1=fragrancenotes&prefn2=productType&prefv1={}%7C{}%7C{}&prefv2=FRAGRANCE'.format(
        notes_dict[note1], notes_dict[note2], notes_dict[note3])
    return redirect(base_url + selection)

# @app.route('/fragrance/<string:id>')
# def fragrance(id):
#     '''
#     cur = database.connection.cursor()

#     result = cur.excecute()  

#     fragrance = cur.fetchone()
#     return render_template('recommendation.html'), fragrance = fragrance)
#     '''
#     return 'This is the recommendation' + id

#song form class
'''
class SongForm(Form):
    title = StringField('Title',[validators.Length(min=1,max=50)])
    body = TextAreaField('Body',[validators.Length(min=30,max=1000)])
'''



if __name__ == '__main__':
    with database: database.create_tables([Table]) 
    app.run(host='0.0.0.0', port=9999, debug = True)
