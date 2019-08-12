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

song4 = Song(4, "Money in the Grave", "Drake", 'https://images.genius.com/a5d3df427e3ff8ebeff7c38a7e3bb329.300x300x1.png')
songs.append(song4)

song5 = Song(5, "I Don't Care", "Ed Sheeran",'https://upload.wikimedia.org/wikipedia/en/6/69/Ed_Sheeran_%26_Justin_Bieber_-_I_Don%27t_Care.png')
songs.append(song5)

song6 = Song(6, "Old Town Road", "Lil Nas X",'https://img.discogs.com/zOLHNMG4CR9fgLs4wfJd7T566LA=/fit-in/300x300/filters:strip_icc():format(jpeg):mode_rgb():quality(40)/discogs-images/R-13475626-1554921221-3492.jpeg.jpg')
songs.append(song6)

song7 = Song(7, "Bad Guy", "Billie Eilish", 'http://d2lubch9d26anb.cloudfront.net/cdn/farfuture/QnhjlVPapAC_e9SVZ242t0OCLM_CCC4Stnx5FQsT2P0/mtime:1548794286/sites/default/files/styles/album_artwork__300x300_/public/BAA434A0-9DBB-4216-B605-0510C18C54CA.jpeg?itok=VT9atKhn')
songs.append(song7)

song8 = Song(8, "God's Country", "Blake Shelton", 'https://upload.wikimedia.org/wikipedia/en/b/b2/Blake_Shelton_-_God%27s_Country.png')
songs.append(song8)

song9 = Song(9, "Natrual", "Imagine Dragons", 'https://upload.wikimedia.org/wikipedia/en/1/10/Imagine_Dragons_Natural.png')
songs.append(song9)

song10 = Song(10, "Happier", "Marshmello", 'https://images.genius.com/4ff9277eed36fb6f90372654b6c9d818.300x300x1.png')
songs.append(song10)

song11 = Song(11, "Under Your Scars", "Godsmack", 'https://images.genius.com/6cd7debb969c7222440a560f287c7152.300x300x1.png')
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
#for i, n in enumerate(note_lst):
#    note = Note(i, n,'https://www.google.com/search?q=citrus&source=lnms&tbm=isch&sa=X&ved=0ahUKEwijufrcvtHjAhVkTt8KHR1UC9MQ_AUIESgB&cshid=1564106619008256&biw=1680&bih=939#imgrc=D6mKxRRc4-Rz1M:' )
#    notes.append(note)
#    notes_dict[i] = n

note1 = Note(1, 'CITRUS', 'https://blog.williams-sonoma.com/wp-content/uploads/2014/01/CitrusEditorial_v9.jpg')
notes.append(note1)
notes_dict[1] = 'CITRUS'

note2 = Note(2, 'FLORAL', 'https://www.elliecashmandesign.com/media/catalog/product/cache/1/image/800x/602f0fa2c1f0d1ba5e241f914e856ff9/d/f/df03100_.jpg')
notes.append(note2)
notes_dict[2] = 'FLORAL'

note3 = Note(3, 'FOUGERE', 'https://www.dapperconfidential.com/wp-content/uploads/2017/06/mike-erskine-98419-750x500.jpg')
notes.append(note3)
notes_dict[3] = 'FOUGERE'

note4 = Note(4, 'GREEN', 'https://mz-static.imgix.net/redactor/pictures/8112/Green-Term-Deposit_original.jpg?w=660&fm=jpg&q=70')
notes.append(note4)
notes_dict[4] = 'GREEN'

note5 = Note(5, 'LEATHER', 'http://www.chalk29.com/wp-content/uploads/2015/12/leather-1080x720.jpg')
notes.append(note5)
notes_dict[5] = 'LEATHER'

note6 = Note(6, 'ORIENTAL', 'https://100degreeperfumes.com/wp-content/uploads/2019/04/orientalfragrance.jpg')
notes.append(note6)
notes_dict[6] = 'ORIENTAL'

note7 = Note(7, 'TOBACCO', 'https://countryclubformen.com/wp-content/uploads/2018/08/tobacco.jpg')
notes.append(note7)
notes_dict[7] = 'TOBACCO'

note8 = Note(8, 'WOODS', 'https://f4.bcbits.com/img/a4170709666_10.jpg')
notes.append(note8)
notes_dict[8] = 'WOODS'

#REPEAT THESE NOTES FOR THE OTHER SONGS
note9 = Note(9, 'FLORAL', 'https://www.elliecashmandesign.com/media/catalog/product/cache/1/image/800x/602f0fa2c1f0d1ba5e241f914e856ff9/d/f/df03100_.jpg')
notes.append(note9)
notes_dict[9] = 'FLORAL'

note10 = Note(10, 'FOUGERE', 'https://www.dapperconfidential.com/wp-content/uploads/2017/06/mike-erskine-98419-750x500.jpg')
notes.append(note10)
notes_dict[10] = 'FOUGERE'

note11 = Note(11, 'GREEN', 'https://mz-static.imgix.net/redactor/pictures/8112/Green-Term-Deposit_original.jpg?w=660&fm=jpg&q=70')
notes.append(note11)
notes_dict[11] = 'GREEN'

note12 = Note(12, 'LEATHER', 'http://www.chalk29.com/wp-content/uploads/2015/12/leather-1080x720.jpg')
notes.append(note12)
notes_dict[12] = 'LEATHER'

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

#Perfume
fragrance[0] = Fragrance(0, 0,'Black Orchid', 'https://www.tomford.com/black-orchid/T0-BLACK-ORCHID.html')

#Cologne
fragrance[1] = Fragrance(1, 1, 'Tom Ford For Men', 'https://www.tomford.com/tom-ford-for-men/T03-TOMFORD-FORMEN.html')

#unisex
fragrance[2] = Fragrance(2, 2, 'Oud Wood', 'https://www.tomford.com/oud-wood/T1-OUD-WOOD.html')
#TODO: Add all the fragrances here

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
        print(result[0])
        print(result[1])
        print(result[2])
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





if __name__ == '__main__':
    with database: database.create_tables([Table])
    app.run(host='0.0.0.0', port=9999, debug = True)
