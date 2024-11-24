import math


def calculate_distance(coord1, coord2):
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    R = 6378100

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_meters = R * c

    distance_kilometers = round(distance_meters / 1000)

    return distance_kilometers


if __name__ == "__main__":
    point1 = [55.7558, 37.6173]
    point2 = [48.8566, 2.3522]

    distance = calculate_distance(point1, point2)
    print(f"The distance between the two points is {distance} km.")
