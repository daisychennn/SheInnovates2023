import pandas as pd
import folium
from folium.plugins import Search
from folium.plugins import BeautifyIcon
import numpy as np
import imageio
import cv2
import requests
import io
import webbrowser
from branca.element import Template, MacroElement



url = "https://raw.githubusercontent.com/daisychennn/SheInnovates2023/main/Pitt-Dining.csv"
r = requests.get(url)
# print(r.text)
df = pd.read_csv(io.StringIO(r.text))

m = folium.Map(location=[40.4426, -79.9564], tiles='Stamen Terrain', zoom_start=16.5, control_scale = True)

# square marker
icon_square = BeautifyIcon(
    icon_shape='rectangle-dot', 
    border_color='red', 
    border_width=10,
)

# circle marker
icon_circle = BeautifyIcon(
    icon_shape='circle-dot', 
    border_color='green', 
    border_width=10,
)

# star marker
icon_star = BeautifyIcon(
    icon_shape='star',
    inner_icon_style='color:blue',
    background_color='transparent',
    border_color='transparent',
)


#WPU
#group these places together into Schenley Cafe

folium.vector_layers.Marker(location=[40.443257, -79.954832], tooltip='Wicked Pie (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.443155, -79.954902], tooltip='PA Taco (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.443179, -79.954773], tooltip='True Burger (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.443159, -79.954854], tooltip='CrEATe (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.443118, -79.954924], tooltip='Ft. Pitt Subs (*V)').add_to(m)


#Cathy
folium.vector_layers.Marker(location=[40.444380, -79.953171], tooltip='The Roost').add_to(m)
folium.vector_layers.Marker(location=[40.444458, -79.953204], tooltip='Pam & Honey (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.444470, -79.953231], tooltip='Cathedral Sushi').add_to(m)
folium.vector_layers.Marker(location=[40.444348, -79.953171], tooltip='Saxbys (*V)').add_to(m)


#Hillman
folium.vector_layers.Marker(location=[40.442320, -79.953906], tooltip='Saxbys (*V)').add_to(m)


#Posvar
folium.vector_layers.Marker(location=[40.441470, -79.954512], tooltip='Einstein Bros Bagels (*V)').add_to(m)


#Amos's Starbucks (mark it as doesn't accept dining dollars/panther funds/meal swaps, etc)
folium.vector_layers.Marker(location=[40.443526, -79.955749], tooltip='Starbucks (*V)').add_to(m)


#Pete
folium.vector_layers.Marker(location=[40.443764, -79.962283], tooltip='BBQ Smokeland').add_to(m)
folium.vector_layers.Marker(location=[40.443817, -79.962337], tooltip='Shake Smart (*V)').add_to(m)
folium.vector_layers.Marker(location=[40.443903, -79.962417], tooltip='Chick-fil-a').add_to(m)
folium.vector_layers.Marker(location=[40.443948, -79.962455], tooltip='Burrito Bowl (*V)').add_to(m)

#Benedum
popup  = folium.Popup('Einstein Bros Bagels', max_width=600, max_height=600)
folium.vector_layers.Marker(location=[40.4441782,-79.9582627], tooltip='Einstein Bros Bagels (*V)').add_to(m)

#Study Areas
folium.vector_layers.Marker(location=[40.443922, -79.958131], tooltip='Bevier Engineering Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.442923, -79.961480], tooltip='Falk Library of Health Sciences', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.442444, -79.954031], tooltip='Hillman Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.442427, -79.954991], tooltip='Barco Law Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.442787, -79.950495], tooltip='Carnegie Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.441474, -79.951187], tooltip='Frick Fine Arts Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.445950, -79.957585], tooltip='Chemistry Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.446685, -79.953716], tooltip='Langley Library', icon=folium.Icon(color='red')).add_to(m)
folium.vector_layers.Marker(location=[40.446731, -79.952257], tooltip='Theodore M. Finney Music Library', icon=folium.Icon(color='red')).add_to(m)


#Add legend
template = """
{% macro html(this, kwargs) %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pitt Campus Map</title>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  
  <script>
  $( function() {
    $( "#maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
});

  </script>
</head>
<body>

 
<div id='maplegend' class='maplegend' 
    style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
     border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
     
<div class='legend-title'>Legend</div>
<div class='legend-scale'>
  <ul class='legend-labels'>
    <li><span style='background:red;opacity:0.7;'></span>Library</li>
    <li><span style='background:blue;opacity:0.7;'></span>Dining Options</li>
    <li><span style='background:white;opacity:0.7;'></span>(*V) = Vegetarian/Vegan Options</li>

  </ul>
</div>
</div>
 
</body>
</html>

<style type='text/css'>
  .maplegend .legend-title {
    text-align: left;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 90%;
    }
  .maplegend .legend-scale ul {
    margin: 0;
    margin-bottom: 5px;
    padding: 0;
    float: left;
    list-style: none;
    }
  .maplegend .legend-scale ul li {
    font-size: 80%;
    list-style: none;
    margin-left: 0;
    line-height: 18px;
    margin-bottom: 2px;
    }
  .maplegend ul.legend-labels li span {
    display: block;
    float: left;
    height: 16px;
    width: 30px;
    margin-right: 5px;
    margin-left: 0;
    border: 1px solid #999;
    }
  .maplegend .legend-source {
    font-size: 80%;
    color: #777;
    clear: both;
    }
  .maplegend a {
    color: #777;
    }
</style>
{% endmacro %}"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)


m.save('Pitt Map')
u = 'file:///Users/daisychen/Desktop/SheInnovates2023/Pitt Map'
webbrowser.open(u, new=0)
