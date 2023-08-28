import math


def haversine_distance(lon1, lat1, lon2, lat2):
    r = 6371

    lon1_rad = math.radians(lon1)
    lat1_rad = math.radians(lat1)
    lon2_rad = math.radians(lon2)
    lat2_rad = math.radians(lat2)

    d_lon = lon2_rad - lon1_rad
    d_lat = lat2_rad - lat1_rad

    a = math.sin(d_lat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = r * c

    return distance
