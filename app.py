import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
from datasets import *

df=pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.sidebar.title('India ka Data')
selected_state = st.sidebar.selectbox('Select a state', list_of_states)

primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))
plot = st.sidebar.button('Plot Graph')
if plot:
    st.text('Size represents Primary Parameter')
    st.text('Color represents Secondary Parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat = 'Latitude',
                        lon = 'Longitude',
                        zoom = 4,
                        size = primary,
                        color = secondary,
                        size_max=35,
                        width=1200,
                        height=700,
                        mapbox_style = 'carto-positron',
                        hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        #plot for state
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat = 'Latitude',
                        lon = 'Longitude',
                        zoom = 4,
                        size = primary,
                        color = secondary,
                        size_max=35,
                        width=1200,
                        height=700,
                        mapbox_style = 'carto-positron',
                        hover_name='District')
        st.plotly_chart(fig, use_container_width=True)