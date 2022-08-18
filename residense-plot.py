import pandas as pd
df = pd.read_csv(r"C:\Users\jrm\Desktop\opendata_project\opendata_project.csv",encoding= 'unicode_escape')
df.head()

import folium
import webbrowser
loc_center = [df['latitude'].mean(), df['longitude'].mean()]

map1 = folium.Map(location = loc_center, tiles='Openstreetmap', zoom_start = 5, control_scale=True)
for index, loc in df.iterrows():
    folium.CircleMarker([loc['latitude'], loc['longitude']],     radius=2, weight=5, popup=loc['price_min']).add_to(map1)
folium.LayerControl().add_to(map1)
map1.save("mymap.html")
webbrowser.open("mymap.html")
