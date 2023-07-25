import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')
df=pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'overall india')
st.sidebar.title('India Census Visualization')
selected_state = st.sidebar.selectbox('select a state',list_of_states)
primary_parameter=st.sidebar.selectbox('select a primary parameter',sorted(df.columns[5:]))
secondary_parameter=st.sidebar.selectbox('select a secondary parameter',sorted(df.columns[5:]))
plot=st.sidebar.button('plot graph')

if plot:
    st.text('size represent primary parameter')
    st.text('color represent secondary parameter')
    if selected_state=='overall india':
        #plot for india
        fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',zoom=4,mapbox_style="carto-positron",width=1200,height=700,hover_name='District',
                              size=primary_parameter,size_max=35,color=secondary_parameter)
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot for state
        state_df=df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=4, mapbox_style="carto-positron", width=1200,
                                height=700, hover_name='District',
                                size=primary_parameter, size_max=35, color=secondary_parameter)
        st.plotly_chart(fig, use_container_width=True)
