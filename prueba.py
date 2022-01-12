import streamlit as st 
import pandas as pd 
import numpy as np 
from bokeh.plotting import figure
#import psycopg2
import sys 


st.title("""
GetHired Community dashboard
""")



#Data visualization using bokeh

df_users  = pd.read_csv('USERS_MOCK_DATA_1.csv')
df_users['creado_dia'] = pd.to_datetime(df_users['creado_dia'])

y = df_users.groupby(pd.Grouper(key='creado_dia',freq='M'))['id'].count()
x = y.index

p = figure(
     title='New users per month',
     x_axis_type = "datetime",
     x_axis_label='Month and year',
     y_axis_label='New users')

p.background_fill_color = "#22201F"
p.line(x,y, line_width=2)

st.subheader('New Users per month')
st.bokeh_chart(p)




#Analysis per country 

countries_count = df_users.groupby('pais')['id'].count()
st.subheader('Usuarios por paises')
st.write(countries_count.sort_values( ascending=False))




#Challenges and community analysis 

challenges_df = pd.read_csv('dummy_data.csv')

popular_post = challenges_df.groupby('discussion-post')['likes'].sum()
st.subheader('Post más populares')
st.bar_chart(data = popular_post)

popular_topics = challenges_df.groupby('Tema challenges')['Challenges completados '].sum()
st.subheader('Temas más populares')
st.bar_chart(data=popular_topics)

df_gender = pd.read_csv('gender_mock_data.csv')
gender_analysis = (df_gender.groupby('genero').count() / df_gender.groupby('genero').count().sum()) * 100

st.write('Género')
st.bar_chart(data=gender_analysis)






#xx = pd.read_sql_query()
