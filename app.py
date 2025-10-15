# app.py (bloque opcional con casillas)
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header('Panel de vehículos')

car_data = pd.read_csv('vehicles_us.csv')

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odometer')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un diagrama de dispersión')
if build_scatter:
    st.write('Construir un diagrama de dispersión odometer vs price')
    fig2 = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig2.update_layout(title='Odometer vs Price', xaxis_title='odometer', yaxis_title='price')
    st.plotly_chart(fig2, use_container_width=True)
