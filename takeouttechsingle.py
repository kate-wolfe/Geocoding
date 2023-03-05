import json
import pandas as pd
import geopandas as gpd
import plotly.io as pio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

zipfile = "zip:///Users/Kate/Desktop/tl_2020_25_tract10.zip"
tracts = gpd.read_file(zipfile).to_crs("EPSG:4326")

df = pd.read_csv("/Users/Kate/Desktop/CObySCATbyTract8-4-21ToT.csv", dtype={'Tract':str})


tracts = pd.merge(tracts, df, left_on='TRACTCE10', right_on='Tract', how="inner")

zipjson = json.loads(tracts.to_json())


fig1 = go.Choroplethmapbox(geojson=zipjson, locations=df.Tract, featureidkey="properties.Tract", z=df.April,
                                    colorscale="viridis", zmin=0, zmax=35,
                                    marker_opacity=0.7, marker_line_width=1, showlegend=False, showscale=False)

fig2 = go.Choroplethmapbox(geojson=zipjson, locations=df.Tract, featureidkey="properties.Tract", z=df.May,
                                    colorscale="viridis", zmin=0, zmax=35,
                                    marker_opacity=0.7, marker_line_width=1, showlegend=False, showscale=False)

fig3 = go.Choroplethmapbox(geojson=zipjson, locations=df.Tract, featureidkey="properties.Tract", z=df.June,
                                    colorscale="viridis", zmin=0, zmax=35,
                                    marker_opacity=0.7, marker_line_width=1, showlegend=False, showscale=False)

fig4 = go.Choroplethmapbox(geojson=zipjson, locations=df.Tract, featureidkey="properties.Tract", z=df.July,
                                    colorscale="viridis", zmin=0, zmax=35,
                                    marker_opacity=0.7, marker_line_width=1, showlegend=False, showscale=False)




# Initialize figure with subplots
fig = make_subplots(
    rows=2, cols=2, subplot_titles=("April", "May", "June", "July"),
    specs=[[{"type": "choroplethmapbox"}, {"type": "choroplethmapbox"}], [{"type": "choroplethmapbox"}, {"type": "choroplethmapbox"}]],
    vertical_spacing=0.1)

# Add first map
fig.add_trace(
    fig1,
    row=1, col=1
)

# Add second map
fig.add_trace(
    fig2,
    row=1, col=2
)

# Add third map
fig.add_trace(
    fig3,
    row=2, col=1
)

# Add fourth map
fig.add_trace(
    fig4,
    row=2, col=2
)


fig.update_layout(mapbox_style="open-street-map", mapbox2_style="open-street-map", mapbox3_style="open-street-map", mapbox4_style="open-street-map",
mapbox_zoom=11.5, mapbox2_zoom=11.5, mapbox3_zoom=11.5, mapbox4_zoom=11.5, 
mapbox_center = {"lat": 42.378418, "lon": -71.109544}, mapbox2_center = {"lat": 42.378418, "lon": -71.109544}, mapbox3_center = {"lat": 42.378418, "lon": -71.109544}, mapbox4_center = {"lat": 42.378418, "lon": -71.109544})


pio.write_html(fig, file='/Users/Kate/Desktop/TakeoutTechMonths.html', auto_open=True)