import json
from flask import Blueprint, jsonify, request, redirect, Response
from json2html import *
from geocens_api.utils import *
#=== Platform ===#
platform_api = Blueprint('platform_api', __name__)

@platform_api.route('/info/')
def info():
    response = {
        "name": "Smart Air (GeoCENS)",
        "synopsis": "Smart Air extends the existing GeoCENS platform to collect and analyze hyper-local and real-time air quality data across Canada. Smart Air will provide street-level air quality data with an unprecedented spatio-temporal resolution, leading to transformative new innovations with direct impacts to the health of Canadians.",
        "version": "v1.0",
        "institution": "University of Calgary",
        "releaseTime": "2019-08-08T18:00:00Z",
        "researchSubject": "Geographic Information Systems",
        "supportEmail": "smart.cities@sensorup.com",
        "tags": ["GeoCENS", "Air Quality", "Smart Cities"]
    }

    if request_wants_json():
        return Response(response=json.dumps(response),status=200,mimetype='application/json')
    return Response(response=json2html.convert(json=json.dumps(response)),status=200,mimetype='text/html')

@platform_api.route('/stats/')
def stats():
    utc_datetime = datetime.utcnow()
    last_reset = utc_datetime.strftime("%Y-%m-%dT%H:%M:%SZ")

    thing_count = getSTA("Things")["@iot.count"]

    response = {
        "sensor counts": thing_count,
        "lastReset": last_reset
    }

    if request_wants_json():
        return Response(response=json.dumps(response),status=200,mimetype='application/json')
    return Response(response=json2html.convert(json=json.dumps(response)),status=200,mimetype='text/html')

@platform_api.route('/doc/')
def docs():
    return redirect('https://canarie-geocens.github.io/')

@platform_api.route('/releasenotes/')
def releasenotes():
    return redirect('https://canarie-geocens.github.io/#releasenotes')

@platform_api.route('/support/')
def support():
    return redirect('https://canarie-geocens.github.io/#support')

@platform_api.route('/source/')
def source():
    return redirect('https://github.com/canarie-geocens/')

@platform_api.route('/tryme/')
def tryme():
    return redirect('https://geocens.sensorup.com/')

@platform_api.route('/licence/')
def licence():
    return redirect('https://canarie-geocens.github.io/#licence')

@platform_api.route('/provenance/')
def provenance():
    return redirect('https://canarie-geocens.github.io/#provenance')

@platform_api.route('/factsheet/')
def factsheet():
    return redirect('https://canarie-geocens.github.io/#factsheet')
