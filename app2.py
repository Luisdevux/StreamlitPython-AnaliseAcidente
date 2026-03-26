import pandas as pd
import streamlit as st

# Carregamento dos dados
acidentes = pd.read_csv('./acidentes/acidentes_2022.csv')
localidades = pd.read_csv('./localidades/localidades_2022.csv')
tipo_veiculo = pd.read_csv('./tipo_veiculo/tipo_veiculo_2022.csv', sep=';')
vitimas = pd.read_csv('./vitimas/vitimas_2022.csv')

acidentes_ro = acidentes[acidentes['uf_acidente'] == 'RO']
localidades_ro = localidades[localidades['uf'] == 'RO']
vitimas_ro = vitimas[vitimas['uf_acidente'] == 'RO']

st.markdown("# Análise de Acidentes de Trânsito em Rondônia - 2022")

## 1. Quais cidades de RO apresentaram mais acidentes em 2022 em valores absolutos?
df_cidades_ro = pd.merge(acidentes_ro, localidades_ro, left_on='chv_localidade', right_on='chv_localidade', how='left')[['num_acidente', 'municipio']].groupby('municipio').count().sort_values(by='num_acidente', ascending=False)

st.markdown("### Cidades de RO com mais acidentes em 2022 (valores absolutos)")
st.dataframe(df_cidades_ro)

## 2. Qual a média de acidentes a cada mil habitantes das cidades de RO? 

df_mergeados = pd.merge(acidentes_ro, localidades_ro, on='chv_localidade', how='left')
df_agrupado = df_mergeados.groupby('municipio').agg({
    'num_acidente': 'count', 
    'qtde_habitantes': 'mean'
})


df_mergeado = df_agrupado.assign(
    media_acidentes_mil_habitantes = lambda x: (x['num_acidente'] / x['qtde_habitantes']) * 1000
).sort_values(by='media_acidentes_mil_habitantes', ascending=False)

st.markdown("### Média de Acidentes a cada mil habitantes por cidade em RO")
st.dataframe(df_mergeado)

## 3. Construa um mapa e faça o plot de cada acidente de 2022 considerando a sua latitude e longitude.

latitudes_invalidas = acidentes[(acidentes.latitude_acidente.isna()) | (acidentes.latitude_acidente == 0)].index
longitudes_invalidas = acidentes[(acidentes.longitude_acidente.isna()) | (acidentes.longitude_acidente == 0)].index
acidentes_filtrados = acidentes.drop([*latitudes_invalidas, *longitudes_invalidas])

st.markdown("### Mapa de Acidentes de Acordo com a Latitude e Longitude - 2022")
st.map(acidentes_filtrados, size=20, latitude="latitude_acidente", longitude="longitude_acidente", color="#0D00FF")
