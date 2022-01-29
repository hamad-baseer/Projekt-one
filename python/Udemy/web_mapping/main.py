import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def marker_colour_key(el):
    if el < 1000:
        return "green"
    elif el >= 1000 and el < 3000:
        return "orange"
    else:
        return "red"


derived_map = folium.Map(location=[13.02, 77.62], zoom_start=10.5, tiles="Stamen Terrain", )
fgv = folium.FeatureGroup(name="Volcanoes")


for latitude, longitude, elevation in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=(latitude, longitude), radius=7.5, popup=folium.Popup(str(elevation)+" m", parse_html=True),
                                      fill_color=marker_colour_key(elevation), fill_opacity=0.7, color="black"))


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open("world.json", "r", encoding='utf-8-sig').read()),
                             style_function=lambda colour_legend: {"fillColor": "green" if colour_legend["properties"]["POP2005"] < 10000000
                             else "orange" if 10000000 <= colour_legend["properties"]["POP2005"] < 20000000 else "red"}))


derived_map.add_child(fgv)
derived_map.add_child(fgp)
derived_map.add_child(folium.LayerControl())
derived_map.save("Map2.html")
