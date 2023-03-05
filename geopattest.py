import json
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.io as pio


zipfile = "zip:///Users/Kate/Desktop/tl_2020_25_tract10.zip"
tracts = gpd.read_file(zipfile).to_crs("EPSG:4326")

df = pd.read_csv("/Users/Kate/Desktop/GeoPatrons.csv", dtype={'geoid':str})
df = df[(df['geoid'] >= '25017352101') & (df['geoid'] <= '25017355000')]


tracts = pd.merge(tracts, df, left_on='GEOID10', right_on='geoid', how="inner")

zipjson = json.loads(tracts.to_json())

fig = px.choropleth_mapbox(df, geojson=tracts, locations='geoid', featureidkey="properties.geoid", color='total_patrons',
                           color_continuous_scale="Viridis",
                           mapbox_style="open-street-map",
                           zoom=13, center = {"lat": 42.3736, "lon": -71.1097},
                           opacity=0.75,
                           labels={'total_patrons':'Number of Patrons','tracts':'Census Tract'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

pio.write_html(fig, file='/Users/Kate/Desktop/geopatTest.html', auto_open=True)