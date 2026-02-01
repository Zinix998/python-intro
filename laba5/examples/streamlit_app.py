import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Moja Aplikacja", layout="wide")
st.title("Prosty Generator Danych")

# Interakcja z użytkownikiem
count = st.slider("Wybierz liczbę losowych punktów", 10, 1000, 100)

# Generowanie danych
chart_data = pd.DataFrame(
    np.random.randn(count, 3),
    columns=['A', 'B', 'C']
)

# Wyświetlenie wykresu liniowego
st.line_chart(chart_data)

st.success(f"Wygenerowano {count} punktów danych!")