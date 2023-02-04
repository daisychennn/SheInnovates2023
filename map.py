import pandas as pd
import folium
import numpy as np
import imageio
import cv2
import requests
import io

url = "https://raw.githubusercontent.com/daisychennn/SheInnovates2023/main/Pitt-Dining.csv"
r = requests.get(url)
# print(r.text)
df = pd.read_csv(io.StringIO(r.text))


m = folium.Map(location=[40.4426, -79.9564], tiles='Stamen Terrain', zoom_start=16.5, control_scale = True)


#WPU
#group these places together into Schenley Cafe

folium.vector_layers.Marker(location=[40.443257, -79.954832], tooltip='Wicked Pie').add_to(m)
folium.vector_layers.Marker(location=[40.443155, -79.954902], tooltip='PA Taco').add_to(m)
folium.vector_layers.Marker(location=[40.443179, -79.954773], tooltip='True Burger').add_to(m)
folium.vector_layers.Marker(location=[40.443159, -79.954854], tooltip='CrEATe').add_to(m)
folium.vector_layers.Marker(location=[40.443118, -79.954924], tooltip='Ft. Pitt Subs').add_to(m)


#Cathy
folium.vector_layers.Marker(location=[40.444380, -79.953171], tooltip='The Roost').add_to(m)
folium.vector_layers.Marker(location=[40.444458, -79.953204], tooltip='Pam & Honey').add_to(m)
folium.vector_layers.Marker(location=[40.444470, -79.953231], tooltip='Cathedral Sushi').add_to(m)
folium.vector_layers.Marker(location=[40.444348, -79.953171], tooltip='Saxbys').add_to(m)


#Hillman
folium.vector_layers.Marker(location=[40.442320, -79.953906], tooltip='Saxbys').add_to(m)


#Posvar
folium.vector_layers.Marker(location=[40.441470, -79.954512], tooltip='Einstein Bros Bagels').add_to(m)


#Amos's Starbucks (mark it as doesn't accept dining dollars/panther funds/meal swaps, etc)
folium.vector_layers.Marker(location=[40.443526, -79.955749], tooltip='Starbucks').add_to(m)


#Pete
folium.vector_layers.Marker(location=[40.443764, -79.962283], tooltip='BBQ Smokeland').add_to(m)
folium.vector_layers.Marker(location=[40.443817, -79.962337], tooltip='Shake Smart').add_to(m)
folium.vector_layers.Marker(location=[40.443903, -79.962417], tooltip='Chick-fil-a').add_to(m)
folium.vector_layers.Marker(location=[40.443948, -79.962455], tooltip='Burrito Bowl').add_to(m)

popup  = folium.Popup('Wicked Pizza', max_width=600, max_height=600)
folium.vector_layers.Marker(location=[32.07148197,34.7876717], tooltip='Wicked Pizza', popup = popup).add_to(m)

popup  = folium.Popup('Wicked Pizza', max_width=600, max_height=600)
folium.vector_layers.Marker(location=[32.07148197,34.7876717], tooltip='Wicked Pizza', popup = popup).add_to(m)
folium.vector_layers.Marker(location=[32.07148197,34.7876717], tooltip='Wicked Pizza', popup = popup).add_to(m)

m.save('Pitt Map')
