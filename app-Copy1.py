import streamlit as st
import leafmap.maplibregl as leafmap
import ibis
from ibis import _
con = ibis.duckdb.connect()
'''
# Zoning/Redlining Map

### Enter a city to view the  specific zoning
'''
# fixme could create drop-down selection of the 300 cities
city_name = st.text_input("Select a city", "New Haven")

# Extract the specified city 
city = (con
    .read_geo("/vsicurl/https://dsl.richmond.edu/panorama/redlining/static/mappinginequality.gpkg")
    .filter(_.city == city_name, _.residential)
    .execute()
)

# Render the map
m = leafmap.Map(style="positron")
m.add_gdf(city, "fill", paint = {"fill-color": ["get", "fill"], "fill-opacity": 0.8})
m.to_streamlit()

