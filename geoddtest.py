# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:56:17 2020

@author: Kate
"""

import geopandas as gpd
import plotly.express as px
import plotly.io as pio
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import json


zipfile = "zip:///Users/Kate/Desktop/zipcodes_ma.zip"
zipcodes = gpd.read_file(zipfile).to_crs("EPSG:4326")

df = pd.read_csv("/Users/Kate/Desktop/zipdata.csv", dtype={'POSTCODE':str})

zipcodes = pd.merge(zipcodes, df, on='POSTCODE', how="inner")

zipjson = json.loads(zipcodes.to_json())

cols_dd = ['Arabic', 'Armenian', 'Bengali']

visible = np.array(cols_dd)

traces = []
buttons = []

for value in cols_dd:
    traces.append(go.Choropleth(
        locations = zipcodes.index,
        geojson = zipjson,
        z=zipcodes[value],
        colorbar_title=value,
        colorscale='deep_r',
        hovertemplate="<b>" + zipcodes['Town'] + "</b><br>" +
                      "Number of checkouts: " + zipcodes[value].astype(str),
        visible = True if value==cols_dd[0] else False
    ))

    buttons.append(dict(label=value, method='update', args=[{'visible':list(visible==value)},{'title':f'<b>{value}</b>'}]))

updatemenus = [{'active':0, 'buttons':buttons}]

fig = go.Figure(data=traces, layout=dict(updatemenus=updatemenus))

first_title = cols_dd[0]
fig.update_layout(title=f'<b>{first_title}</b>', title_x=0.5, geo = dict(scope='usa'))

fig.update_geos(fitbounds="locations", visible=True)

pio.write_html(fig, file='/Users/Kate/Desktop/Language_Maps/dropdowntest.html', auto_open=True)