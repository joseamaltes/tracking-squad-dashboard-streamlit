import streamlit as st 
import pandas as pd 
import numpy as np 
from bokeh.plotting import figure
import psycopg2
import sys 

#Parameters that we need to connect to the POSTGRESQL DB

param_dict = {
    "host"      : "",
    "database"  : "",
    "user"      : "",
    "password"  : "",
    "port":5432
}

#Methods to establish connection 

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1
    
    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()
    
    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df


#Connection to the DB 

#conexion1 = connect(param_dict)
column_names = ['id', 'genero']
postgresql_query = 'SELECT * FROM community.gender_table'

#df_sql = postgresql_to_dataframe(conexion1, postgresql_query, column_names)
#show_gender = (df_sql.groupby('genero').count() / df_sql.groupby('genero').count().sum()) * 100
#st.write('THIS CHART IS OBTAINED FROM A REMOTE POSTGRESQL DB!!')
#st.bar_chart(data=show_gender)


st.write("""
#HELLO WORLD!! 
This is the first app in the community trackins squad using Streamlit
""")

#Using the same dataset but loaded manually 

serie_prueba = pd.read_csv('gender_mock_data.csv')
dataP = (serie_prueba.groupby('genero').count() / serie_prueba.groupby('genero').count().sum()) * 100

st.write('show a dataset')
st.write(serie_prueba)
st.write('Using streamlit charts')
st.bar_chart(data=dataP)

mock_data_df = pd.read_csv('USERS_MOCK_DATA_1.csv')
mock_data_df['creado_dia'] = pd.to_datetime(mock_data_df['creado_dia'])

y = mock_data_df.groupby(pd.Grouper(key='creado_dia',freq='M'))['id'].count()
x = y.index

st.write('Data we are going to plot')
st.write(y)

#Example data visualization using bokeh

p = figure(
     title='New users per month',
     x_axis_type = "datetime",
     x_axis_label='Month and year',
     y_axis_label='New users')

p.background_fill_color = "#22201F"
p.line(x,y, line_width=2)

st.write('Chart using bokeh')
st.bokeh_chart(p)


#xx = pd.read_sql_query()
