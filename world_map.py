import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'lightgreen'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58,-99.89], zoom_start=5, tiles= "Stamen Terrain")

fgt = folium.FeatureGroup(name="U.S.A Volcanos")

for lt, ln, el in zip(lat, lon, elev):
    fgt.add_child(folium.CircleMarker(location=[lt, ln], radius = 8, popup=str(el)+" m",
    fill_color = color_producer(el), color = 'grey', fill_opacity=0.7))

fga = folium.FeatureGroup(name="World Population")

fga.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function= lambda x: {'fillColor':'green' if x ['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgt)
map.add_child(fga)
map.add_child(folium.LayerControl())
map.save("world_map.html")
