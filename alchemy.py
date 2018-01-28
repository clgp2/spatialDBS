from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://spatialuser:spatialuser@localhost/gerrymandering'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

class BerlinWahlkreise(db.Model):
    __tablename__='BerlinWahlkreise'
    id=db.Column('id', db.Integer,primary_key=True )
    geom=db.Column('geom', db.Unicode)
    UWB=db.Column('UWB', db.Unicode)
    BWB=db.Column('BWB', db.Unicode)
    AWK=db.Column('AWK', db.Unicode)
    BEZ=db.Column('BEZ', db.Unicode)

