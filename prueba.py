
from matplotlib.pyplot import title
import streamlit as st 
import pandas as pd 
import numpy as np 
#import psycopg2
import datetime 
import altair as alt 


st.set_page_config(layout="wide")

st.title("""
GetHired Community dashboard
""")

#Sidebar configuration

date_min = st.sidebar.date_input(
     "Select initial date",
     datetime.date(2019, 7, 6))
date_max = st.sidebar.date_input(
     "Select End date",
     datetime.date(2019, 7, 6))

st.write('Range from: ' + str(date_min) + ' to ' + str(date_max) )


#Get the data
df_users  = pd.read_csv('USERS_MOCK_DATA_1.csv')
df_users['creado_dia'] = pd.to_datetime(df_users['creado_dia'])

challenges_df = pd.read_csv('dummy_data.csv')


#Column adjustment
col1, col2 = st.columns([3, 1])
col3, col4  = st.columns(2)



#Users per month analys

created_by = df_users.groupby(pd.Grouper(key='creado_dia',freq='M'))['id'].count()
created_by_indexes = created_by.index

col1.subheader('New Users per month')
col1.line_chart(data=created_by)




#Analysis per country 

countries_count = df_users.groupby('pais')['id'].count()
countries_count_sorted = countries_count.sort_values( ascending=False)
countries_count_countries_name = countries_count_sorted.index


col2.subheader('Countries with most users')
col2.write(countries_count_sorted.head(6))



#Challenges and community analysis 

popular_post_count = challenges_df.groupby('discussion-post')['likes'].sum()
col3.subheader('Popular posts')
col3.write(popular_post_count)


second_chart = alt.Chart(challenges_df).mark_bar().encode(
    x='Challenges completados ', 
    y='Tema challenges'
)

col4.subheader('Popular topics')
col4.altair_chart(second_chart, use_container_width=True)


#Gender analysis 

df_gender = pd.read_csv('gender_mock_data.csv')
gender_analysis = (df_gender.groupby('genero').count() / df_gender.groupby('genero').count().sum()) * 100
st.write('Gender')
st.bar_chart(data=gender_analysis)



