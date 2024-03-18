import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image


st.set_page_config(page_title='Capybird - Série histórica de preços de combustíveos do Brasil - 2013 - 2023.',
                        layout = 'wide',
                        initial_sidebar_state = 'auto')
@st.cache_data
def gerar_df():
    df = pd.read_excel(
        io = "data/data_fuel_brazil.xlsx",
        engine="openpyxl",
        sheet_name="fuel",
        usecols="A:Q",
        nrows=21224
    )
    return df
df = gerar_df()

colunas_uteis = ['MÊS','PRODUTO','REGIÃO','ESTADO','PREÇO MÉDIO REVENDA']

df = df[colunas_uteis]
#Mês e produto
with ((st.sidebar)):
    logo = Image.open("assets/logo.png")
    st.image(logo,use_column_width=False)
    st.subheader('Selecione um mês e um Combustível: ')

    filter_products = st.selectbox(
        "Combustível",
        options= df['PRODUTO'].unique(),
        placeholder = "Escolha uma opção",
    )
    filter_states = st.selectbox(
        "Estado",
        options=df['ESTADO'].unique()
    )
    data_user = df.loc[(df['PRODUTO'] == (filter_products)) & (df['ESTADO'] == (filter_states))]
    st.write("Selecionados: "+ filter_products + ", " + filter_states)




update_dates = data_user['MÊS'].dt.strftime('%Y/%b')
data_user['MÊS'] = update_dates[0:]




st.header("Preço de Combustíveis no Brasil")
st.subheader('2013 - 2023')
st.markdown('**Combustíveis:** ' + filter_products)
st.markdown('**Estados:** ' + filter_states)

chart_combine_state = alt.Chart(data_user).mark_line(
    point=alt.OverlayMarkDef(color='aqua', size=20)
).encode(
    x = 'MÊS:T',
    y = 'PREÇO MÉDIO REVENDA',
    strokeWidth = alt.value(3)
).properties(
    height = 400,
    width = 800
)


st.altair_chart(chart_combine_state)
data_user
