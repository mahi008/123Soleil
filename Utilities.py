from flask import abort
def process_coordinates(lat, lng):
    '''Convert the param to float and check the coverage range'''
    f_lat, f_lng = float(lat), float(lng)
    latitude = 0.00

    isValidCoordinates = check_coordinates(f_lat, f_lng)
    if isValidCoordinates:
        latitude = f_lat
    else:
        print("Out of coverage area")
        abort(403)
    return latitude


def check_coordinates(lat, lng):
    return 41.00 <= lat <= 51.50 and -5.50 <= lng <= 10.00


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calculate_irradiance(lat):
    '''Calculate the irradience using the given formula'''
    irradiance = 2000.0 - 900.0 * (lat - 41.0) / (51.50 - 41.0)
    return irradiance
