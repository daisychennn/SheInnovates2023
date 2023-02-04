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
m.save('Pitt Map')


'''
for index, row in df.iterrows():
    html = folim.Html(
        f"""
        <!DOCTYPE html>
        <html>

        <>

        """,
    )
'''