def get_locationll(location):
    locationr = open('locationsll.txt', 'r')
    if line.startswith("[" + str(location)):
        locationsll = line
    return locationsll