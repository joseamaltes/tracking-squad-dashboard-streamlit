import streamlit as st 
import pandas as pd 
import numpy as np 
from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
import datetime

st.write("""
#HELLO WORLD!! 
This is the first app using streamlit 
""")

serie_prueba = pd.read_csv('gender_mock_data.csv')
dataP = (serie_prueba.groupby('genero').count() / serie_prueba.groupby('genero').count().sum()) * 100

st.write(serie_prueba)
st.bar_chart(data=dataP)

mock_data_df = pd.read_csv('USERS_MOCK_DATA_1.csv')
mock_data_df['creado_dia'] = pd.to_datetime(mock_data_df['creado_dia'])

y = mock_data_df.groupby(pd.Grouper(key='creado_dia',freq='M'))['id'].count()
x = y.index

st.write(y)

p = figure(
     title='New users per month',
     x_axis_type = "datetime",
     x_axis_label='Month and year',
     y_axis_label='New users')

p.background_fill_color = "#22201F"
p.line(x,y, line_width=2)

st.bokeh_chart(p)
