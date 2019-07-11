# coding: utf-8

import os
from flask import Flask, render_template
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
    return "Hello"
    
if __name__ == '__main__':
    with database: database.create_tables([Table]) 
    app.run(host='0.0.0.0', port=9999, debug = True)
