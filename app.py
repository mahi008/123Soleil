from flask import Flask, request, render_template, jsonify, abort
from Utilities import *

app = Flask(__name__, static_url_path='/static')


''' Homepage'''
@app.route("/")
def index_route():
    title = "123Soleil"
    return render_template("index.html", title=title)


@app.route("/data")
def data_route():

    '''Get parmas from url'''
    lat_coor = request.args.get("lat") if request.args.get("lat") else None
    lng_coor = request.args.get("lng") if request.args.get("lng") else None

    irradiance = {}

    '''Check if the value is number and validate the coordinates'''
    if is_number(lat_coor) and is_number(lng_coor):
        processed_lat = process_coordinates(lat_coor, lng_coor)
        irradiance = {"result": calculate_irradiance(processed_lat)}
    else:
        print("Missing url parameters or the params given is not the correct type")
        abort(403)

    return jsonify(irradiance)