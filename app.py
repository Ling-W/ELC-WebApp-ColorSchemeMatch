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
    def __init__(self, id, name, artist, img):
        self.id = id
        self.name  = name
        self.artist = artist
        #self.link = link
        self.img = img

class Note:
    def __init__(self, id, name, img):
        self.id = id
        self.name  = name
        self.img = img





#Mock dataset of songs
songs = []
#for i in range(15):
#    song = Song(i, "song_{}".format(i), "Taylor Swift","https://soundcloud.com/taylorswiftofficial/i-did-something-bad", 'https://i1.sndcdn.com/artworks-NMKb89tCPSQP-0-t500x500.jpg')
#    songs.append(song)


song0 = Song(0, "Ran$om", "Lil Tecca", 'https://upload.wikimedia.org/wikipedia/en/8/86/Lil_Tecca_-_Ransom.png')
songs.append(song0)

song1 = Song(1, "Boyfriend", "Ariana Grande", 'http://cdn02.cdn.justjared.com/wp-content/uploads/headlines/2019/08/ariana-grande-boyfriend-stream.jpg')
songs.append(song1)

song2 = Song(2, "Goodbyes", "Post Malone", 'https://pl.scdn.co/images/pl/default/8ad229b50c9ab13c0c233dc987e8b59a6e1746c5')
songs.append(song2)

song3 = Song(3, "Truth Hurts", "Lizzo", 'https://s3.amazonaws.com/media.thecrimson.com/photos/2019/05/04/135013_1338000.png')
songs.append(song3)

song4 = Song(4, "Monkey in the Grave", "Drake", 'https://i.ytimg.com/vi/gK2JZvtU-xE/hqdefault.jpg')
songs.append(song4)

song5 = Song(5, "I Don't Care", "Ed Sheeran",'https://upload.wikimedia.org/wikipedia/en/6/69/Ed_Sheeran_%26_Justin_Bieber_-_I_Don%27t_Care.png')
songs.append(song5)

song6 = Song(6, "Old Town Road", "Lil Nas X",'https://img.discogs.com/zOLHNMG4CR9fgLs4wfJd7T566LA=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-13475626-1554921221-3492.jpeg.jpg')
songs.append(song6)

song7 = Song(7, "Bad Guy", "Billie Eilish", 'http://d2lubch9d26anb.cloudfront.net/cdn/farfuture/QnhjlVPapAC_e9SVZ242t0OCLM_CCC4Stnx5FQsT2P0/mtime:1548794286/sites/default/files/styles/album_artwork__300x300_/public/BAA434A0-9DBB-4216-B605-0510C18C54CA.jpeg?itok=VT9atKhn')
songs.append(song7)

song8 = Song(8, "God's Country", "Blake Shelton", 'https://upload.wikimedia.org/wikipedia/en/b/b2/Blake_Shelton_-_God%27s_Country.png')
songs.append(song8)

song9 = Song(9, "High Hopes", "Panic! At The Disco", 'https://res.cloudinary.com/dx5kjjpce/image/upload/d_default.svg/2788f359d686032eeebbbb4c908ea9f6.jpg')
songs.append(song9)

song10 = Song(10, "Happier", "Marshmello", 'https://images.genius.com/4ff9277eed36fb6f90372654b6c9d818.300x300x1.png')
songs.append(song10)

song11 = Song(11, "I Did Something Bad", "Taylor Swift", 'https://glhsreflection.org/wp-content/uploads/2017/11/REPUTATIONCOVER-300x300.jpg')
songs.append(song11)


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

#All Fragrance
class Fragrance:
    def __init__(self, id, category, name, link):
        self.id = id
        self.category = category
        self.name = name
        self.link = link



fragrance = {}

#add fragrance
#0 perfume, 1 cologne, 2 unisex
fragrance[0] = Fragrance(0,2,'SOLEIL BLANC ATOMIZER', 'https://www.tomford.com/soleil-blanc-atomizer/T6K7.html?cgid=3-555&dwvar_T6K7_color=OC#prefn1=productType&srule=Price+-+Ascending&prefv1=FRAGRANCE&gclid=Cj0KCQjws7TqBRDgARIsAAHLHP5GIIeAca0JIzG-Y1TQoGaWy8Rpinw8ovD57BOrIX6ncXu_8m3OVm4aAiaYEALw_wcB&gclsrc=aw.ds&start=12')
fragrance[1] = Fragrance(1,1,'Tom Ford for Men','https://www.tomford.com/tom-ford-for-men/T03-TOMFORD-FORMEN.html?cgid=3-555&dwvar_T03-TOMFORD-FORMEN_color=OC#prefn1=productType&srule=Price+-+Ascending&prefv1=FRAGRANCE&gclid=Cj0KCQjws7TqBRDgARIsAAHLHP5GIIeAca0JIzG-Y1TQoGaWy8Rpinw8ovD57BOrIX6ncXu_8m3OVm4aAiaYEALw_wcB&gclsrc=aw.ds&start=17')
fragrance[2] = Fragrance(2,0, 'Orchid Soleil','https://www.tomford.com/orchid-soleil/T47Y-ORCHID-SOLEIL.html?dwvar_T47Y-ORCHID-SOLEIL_color=OC&cgid=3-555#prefn1=productType&srule=Price+-+Ascending&prefv1=FRAGRANCE&gclid=Cj0KCQjws7TqBRDgARIsAAHLHP5GIIeAca0JIzG-Y1TQoGaWy8Rpinw8ovD57BOrIX6ncXu_8m3OVm4aAiaYEALw_wcB&gclsrc=aw.ds&start=1')
fragrance[3] = Fragrance(3,1,'TOM FORD NOIR POUR FEMME','https://www.tomford.com/tom-ford-noir-pour-femme/T2RY.html?cgid=3-555&dwvar_T2RY_color=OC#prefn1=productType&srule=Price+-+Ascending&prefv1=FRAGRANCE&gclid=Cj0KCQjws7TqBRDgARIsAAHLHP5GIIeAca0JIzG-Y1TQoGaWy8Rpinw8ovD57BOrIX6ncXu_8m3OVm4aAiaYEALw_wcB&gclsrc=aw.ds&start=1')

category = 0
@app.route("/")
def hello():
    
    #return render_template('songs.html', songs = songs)
    return render_template('category.html')
    
@app.route("/category")
def category():
    return render_template('category.html')

@app.route("/perfume")
def perfume():
    global category 
    category = 0
    return render_template('songs.html', songs = songs)

@app.route("/cologne")
def cologne():
    global category
    category = 1
    return render_template('songs.html', songs = songs)

@app.route("/unisex")
def unisex():
    global category
    category = 2
    return render_template('songs.html', songs = songs)
    

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
    # base_url = 'https://www.tomford.com/beauty/fragrance/'
    # selection = '#prefn1=fragrancenotes&prefn2=productType&prefv1={}%7C{}%7C{}&prefv2=FRAGRANCE'.format(
    #     notes_dict[note1], notes_dict[note2], notes_dict[note3])
    # #return redirect(base_url + selection)
    res = []
    for f in fragrance.values():
        if f.category == category:
            res.append(f)
    
    return redirect(res[0].link)





if __name__ == '__main__':
    with database: database.create_tables([Table]) 
    app.run(host='0.0.0.0', port=9999, debug = True)
