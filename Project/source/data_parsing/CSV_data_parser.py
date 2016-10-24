from data_parsing.Planet import Planet

eu = {"mass": "mass", "radius":"radius", "orbital_period": "period", "semi_major_axis":"semimajoraxis",
    "eccentricity":"eccentricity", "detection_type":"discoverymethod"}
nasa = {}

discoveryCorrection = {"Radial Velocity": "RV", "Primary Transit": "transit", "Imaging":"imaging",
    "Pulsar":"timing", "Microlensing":"microlensing", "TTV":"transit", "Astrometry":"RV"}

correction = {"discoverymethod":discoveryCorrection}

def buildPlanet(line, heads, wanted, source):
    _data_field = dict()
    _name = 0
    _wanted = wanted

    if(source == "eu"):
        _actual = eu
    else: #(source == "nasa")
        _actual = nasa

    for i in _wanted:
        temp = _actual[i]
        tempval = _fixVal(temp, heads.index(i))
        #if(heads.index(i) == "Other"):
        _data_field[temp] = tempval

    planet = Planet(line[_name])

    for i in _data_field:
        # here
        try:
            planet.addVal(i, line[_data_field[i]])
        except:
            planet.addVal(i, "")

    return planet

def _fixVal(field, value):
    if(field in correction and value in correction[field]):
        return correction[field[value]]
    else:
        return value

def buildDictionaryPlanets(filename, wanted, source):
    file = open(filename, "r")
    heads = file.readline().split(',')
    line = file.readline()
    planets = dict()

    while(line):
        line = line.split(',')
        planet = buildPlanet(line, heads, wanted, source)
        planets[planet.data["namePlanet"]] = planet
        line = file.readline()
    return planets

def buildListPlanets(filename, wanted, source):
    tdict = buildDictionaryPlanets(filename, wanted, source)
    rlist = []

    for name in tdict:
        rlist += [tdict[name]]
    return rlist

if __name__ == "__main__":
    try:
        planets = buildListPlanets("exoplanet.eu_catalog-2.csv",
            ["mass", "radius", "orbital_period", "semi_major_axis"], "eu")
        for i in planets:
            print(str(i))
    except:
        pass