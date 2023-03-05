import json
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.io as pio

zipfile = "zip:///Users/Kate/Desktop/tl_2020_25_tract10.zip"
tracts = gpd.read_file(zipfile).to_crs("EPSG:4326")

df = pd.read_csv("/Users/Kate/Desktop/5weekTech.csv", dtype={'TRACT':str})


tracts = pd.merge(tracts, df, left_on='TRACTCE10', right_on='TRACT', how="inner")

zipjson = json.loads(tracts.to_json())

fig = px.choropleth_mapbox(df, geojson=zipjson, locations='TRACT', featureidkey="properties.TRACT", color='All',
                           color_continuous_scale="Viridis",
                           mapbox_style="open-street-map",
                           zoom=12, center = {"lat": 42.3736, "lon": -71.1097},
                           opacity=0.75
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

pio.write_html(fig, file='/Users/Kate/Desktop/TakeoutTechAll.html', auto_open=True)