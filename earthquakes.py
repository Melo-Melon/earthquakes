# The Python standard library includes some functionality for communicating
# over the Internet.
# However, we will use a more powerful and simpler library called requests.
# This is external library that you may need to install first.
import requests
import json


def get_data():
    # With requests, we can ask the web service for the data.
    # Can you understand the parameters we are passing here?
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
        params={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2018-10-11",
            "orderby": "time-asc"}
    )

    # The response we get back is an object with several fields.
    # The actual contents we care about are in its text field:


    text = response.text
    dic = json.loads(text)
    #dum = json.dumps(json.loads(text))
    # f2 = open('Earthquake.json', 'w')
    # f2.write(dum)
    # f2.close()


    # To understand the structure of this text, you may want to save it
    # to a file and open it in VS Code or a browser.
    # See the README file for more information.

    # We need to interpret the text to get values that we can work with.
    # What format is the text in? How can we load the values?
    return dic

def count_earthquakes(data):
    """Get the total number of earthquakes in the response."""

    return data["metadata"]["count"]


def get_magnitude(earthquake):
    """Retrive the magnitude of an earthquake item."""
    return earthquake["properties"]["mag"]


def get_location(earthquake):
    """Retrieve the latitude and longitude of an earthquake item."""
    # There are three coordinates, but we don't care about the third (altitude)
    return (earthquake["geometry"]["coordinates"][0],earthquake["geometry"]["coordinates"][1])


def get_maximum(data):
    """Get the magnitude and location of the strongest earthquake in the data."""
    max = 0 
    max_posi = 0
    index = 0
    max_list=[]
    for earth in data["features"] :
        mag = earth["properties"]["mag"]
        if mag>=max:
            max = mag
            max_posi = index
        index = index+1
    return get_magnitude(data["features"][max_posi]), get_location(data["features"][max_posi])


# With all the above functions defined, we can now call them and get the result
data = get_data()
print(f"Loaded {count_earthquakes(data)}")
#print(data)
max_magnitude, max_location = get_maximum(data)
print(f"The strongest earthquake was at {max_location} with magnitude {max_magnitude}")