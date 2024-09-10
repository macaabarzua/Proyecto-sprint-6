import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\macaa\OneDrive\Escritorio\TripleTen\Sprint 6\Proyecto\Proyecto-sprint-6\vehicles_us.csv')

st.header('Proyecto 6: desarrollo de una aplicación web')

# Crear un boton
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Construir un gráfico de dispersión para los anuncios de venta de vehiculos')
    fig_2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)