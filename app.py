# coding: utf-8

import os
from flask import Flask, render_template, request, redirect, url_for
#from flask_mysqldb import MySQL
from peewee import *
from wtforms import Form, StringField , TextAreaField ,PasswordField , validators

database = MySQLDatabase(os.environ['MYSQL_DATABASE'], 
                            host=os.environ['MYSQL_HOST'], 
                            port=int(os.environ['MYSQL_PORT']),
                            user=os.environ['MYSQL_USER'], 
                            password=os.environ['MYSQL_PASSWORD'])

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
    def __init__(self, id, name, link):
        self.id = id
        self.name  = name
        self.link = link

#Mock dataset of songs
songs = []
for i in range(15):
    song = Song(i, "song_{}".format(i),"https://soundcloud.com/bluewednesday/sink-or-swim-feat-dj-quads")
    songs.append(song)

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
    

@app.route("/song/<int:id>")
def song(id):
    for song in songs:
        if song.id == id:
            return redirect(song.link)
    return 



@app.route("/select", methods = ['GET','POST'])
def select():
    if request.method == 'POST':
        first_song = request.args.get('songs')
        # first_song = request.form['first']
        # second_song = request.form['second']
        # third_song = request.form['third']
      
        
    return redirect('/result/'+first_song + '/' + second_song + '/' + third_song)

@app.route("/result", methods = ['POST', 'GET'])
def select_song():
    if request.method == 'GET':
        result = request.args.getlist('songs[]')
      
        # first_song = result[0]
        # second_song = request.args.get('songs')[1]
        # third_song = request.args.get('songs')[2]
        return 'This the selected song' + result[0] + result[1] + result[2]
        #else:
            #return "You must select 3 songs!"
    else:
        '''
        #get to the fragrance.
        return redirect('fragrance')
        '''
        return 'The result is.'


@app.route('/fragrance/<string:id>')
def fragrance(id):
    '''
    cur = database.connection.cursor()

    result = cur.excecute()  

    fragrance = cur.fetchone()
    return render_template('recommendation.html'), fragrance = fragrance)
    '''
    return 'This is the recommendation' + id

#song form class
'''
class SongForm(Form):
    title = StringField('Title',[validators.Length(min=1,max=50)])
    body = TextAreaField('Body',[validators.Length(min=30,max=1000)])
'''



if __name__ == '__main__':
    with database: database.create_tables([Table]) 
    app.run(host='0.0.0.0', port=9999, debug = True)
