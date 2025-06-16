import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')
st.title("Gráficos de Veículos")
st.header("Histogramas")
hist_button = st.checkbox('Criar histograma')
valid_cols = car_data.select_dtypes(include=['int64','float64']).columns
columns_list = valid_cols.tolist()

if hist_button:
    st.subheader('Selecione a coluna para o histograma:')
    for col in valid_cols:
        if st.button(f'Histograma de {col}'):
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')     
            fig = px.histogram(car_data, x=col)
            st.plotly_chart(fig, use_container_width=True)
    
st.header("Gráfico de Dispersão")
scatter_button = st.checkbox('Criar Gráfico de Dispersão')

if scatter_button:
    st.session_state.show_scatter = True
 
if st.session_state.get('show_scatter', False):
    col1, col2 = st.columns(2)
    with col1:
        x_axis = st.selectbox(
            'Selecione a coluna para o eixo X:',
            columns_list,
            index=columns_list.index('odometer') if 'odometer' in columns_list else 0
		)
    with col2:
        y_axis = st.selectbox(
            'Selecione a coluna para o eixo Y:',
            columns_list,
            index=columns_list.index('price') if 'price' in columns_list else 1
		)
    if st.button('Gerar Gráfico'):
        st.write('Criando um gráfico de dispersão para o conjunto de dados de anùncios de vendas de carros')
        fig = px.scatter(car_data, x=x_axis, y=y_axis)
        st.plotly_chart(fig, use_container_width=True)