# coding: utf-8

import os
from flask import Flask, render_template, request
from peewee import *

database = MySQLDatabase(os.environ['MYSQL_DATABASE'], 
                            host=os.environ['MYSQL_HOST'], 
                            port=int(os.environ['MYSQL_PORT']),
                            user=os.environ['MYSQL_USER'], 
                            password=os.environ['MYSQL_PASSWORD'])

class BaseModel(Model):
    class Meta:     
        database = database

class Table(BaseModel):
    column1 = CharField()
    column2 = CharField()    
    created_at = DateTimeField()
    updated_at = DateTimeField(null=True)                              
        
app = Flask(__name__)

@app.route("/")
def hello():
    cur = database.connection.cursor()
    #results = cur.excecute("SELECT * FROM songs")
    #songs = cur.fetchall()
    '''
    if result > 0:
        return render_template('index.html',songs = songs)
    else:
        msg = 'no songs found!'
        return render_template('index.html', msg = msg)
    '''
    return render_template('index.html')
    cur.close()


@app.route("/select", method = ['GET','POST'])
def select(request):
    if request.method == 'POST':
        first_song = request.form['first']
        second_song = request.form['second']
        third_song = request.form['third']
        
    return redirect('/select/'+first_song + '/' + second_song + '/' + third_song)

@app.route("/select/<first_song>/<second_song>/<third_song>", methods = ['POST', 'GET'])
def select_song():
    if request.method == 'POST':
        return 'This the selected song'
    else:
        '''
        #get to the fragrance.
        return redirect('fragrance')
        '''
        return 'The result is."


@app.route('/fragrance/<string:id>')
def fragrance(id):
    cur = database.connection.cursor()

    result = cur.excecute()  

    fragrance = cur.fetchone()

    return render_template('recommendation.html'), fragrance = fragrance)
    
if __name__ == '__main__':
    with database: database.create_tables([Table]) 
    app.run(host='0.0.0.0', port=9999, debug = True)
