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
    lat_coor = request.args.get("lat")
    lon_coor = request.args.get("lon")

    irradiance = {}

    if lat_coor and lon_coor:
        data = check_var_type(lat_coor, lon_coor)
    else:
        abort(403)

    if not data["error"]:
        irradiance = {"result" : calculate_irradiance(data["lt"])}
    else:
        abort(403)

    return jsonify(irradiance)