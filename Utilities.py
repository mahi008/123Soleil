def check_var_type(lat, lon):

    lat = float(lat)
    lon = float(lon)

    data = {}

    isOfTypeNum = is_number(lat) and is_number(lon)
    isValidCoordinates = check_coordinates(lat, lon)

    if isOfTypeNum and isValidCoordinates:
        data = {"lt":lat, "ln": lon, "error": None}
    else:
        data = {"lt":None, "ln": None, "error": "Unknown error occurred"}

    return data


def check_coordinates(lat, lon):
    return 41.00 <= lat <= 51.50 and -5.50 <= lon <= 10.00

def calculate_irradiance(lat):
    irradiance = 2000.0 - 900.0 * (lat - 41.0) / (51.50 - 41.0)
    return irradiance


def is_number(n):
    try:
        float(n)

    except ValueError:
        return False
    return True