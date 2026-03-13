import pandas as pd
import streamlit as st

# Carregamento dos dados
acidentes = pd.read_csv('./acidentes/acidentes_2022.csv')
localidades = pd.read_csv('./localidades/localidades_2022.csv')
tipo_veiculo = pd.read_csv('./tipo_veiculo/tipo_veiculo_2022.csv', sep=';')
vitimas = pd.read_csv('./vitimas/vitimas_2022.csv')

acidentes_ro = acidentes[acidentes['uf_acidente'] == 'RO'].head(100)
localidades_ro = localidades[localidades['uf'] == 'RO'].head(100)
vitimas_ro = vitimas[vitimas['uf_acidente'] == 'RO'].head(100)

# Visualização dos dados
st.title('Análise de Acidentes de Trânsito - 2022')
st.dataframe(acidentes_ro)

st.title('Localidades dos Acidentes')
st.dataframe(localidades_ro)

st.title('Tipos de Veículos Envolvidos')
st.dataframe(tipo_veiculo.head(100))

st.title('Vítimas dos Acidentes')
st.dataframe(vitimas_ro)