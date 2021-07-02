import folium
from numpy import string_
import pandas

data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
popupinfo_name= list(data["NAME"])
popupinfo_location= list(data["LOCATION"])
popupinfo_elevation = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start = 6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")


for lt, lg, name, location, elevation in zip(lat, lon, popupinfo_name, popupinfo_location, popupinfo_elevation):
    iframe = folium.IFrame(html=html % (name, name, str(elevation) ) + name + " " + location,  width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, lg], popup=folium.Popup(iframe), icon=folium.Icon(color='red')))



map.add_child(fg)
map.save("Map.html")
