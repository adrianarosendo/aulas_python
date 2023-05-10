import streamlit as st
import pandas as pd
import numpy as np

st.header("Minha dashboard")
df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])

st.bar_chart(df)

title = st.text_input('Nome', 'Caio')

options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Vermelho', 'Verde'])