import json
from flask import Flask, render_template, request
from alchemy import *
from sqlalchemy import create_engine

app = Flask(__name__)

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/json/<year>', methods=['GET']) 
def get_json(year):
    year = int(year)
    if year==1:
        #the engine.execute method returns a resultproxy object, which is a pointer to a db, a tuple-like object
        getGEOJsonQuery=db.engine.execute(
        #query gibt ein geojson Objekt, gleich wie BerlinWahlkreise.geojson
        """
        select json_build_object(
        'type', 'FeatureCollection',
        'features', jsonb_agg(feature))
        from(
            select json_build_object(
                'type',       'Feature',
                'geometry',   ST_AsGeoJSON(geom)::json,
                'properties', json_build_object(
                    'UWB', "UWB",
                    'BWB', "BWB",
                    'AWK', "AWK",
                    'BEZ', "BEZ")) as feature
            from (select * from public."BerlinWahlkreise") row) features;"""
            )        

    elif year==2 or year==3:
        #the engine.execute method returns a resultproxy object, which is a pointer to a db, a tuple-like object
        getGEOJsonQuery=db.engine.execute(
        #query gibt ein geojson Objekt, gleich wie BerlinWahlkreise.geojson
        """
        select json_build_object(
        'type', 'FeatureCollection',
        'features', jsonb_agg(feature))
        from(
            select json_build_object(
                'type',       'Feature',
                'geometry',   ST_AsGeoJSON(geom)::json,
                'properties', json_build_object(
                    'wkr_nr', "wkr_nr",
                    'land_nr', "land_nr",
                    'land_name', "land_name",
                    'wkr_name', "wkr_name")) as feature
            from (select * from public."Wahlkreis_Geometrie") row) features;"""
            )        

    #fetchall returnes an array of an array of one object
    rows= getGEOJsonQuery.fetchall()

    firstlist=rows[0]
    theobject=firstlist[0]
    return json.dumps(theobject)

if __name__ == '__main__':
    app.run(debug=True)


