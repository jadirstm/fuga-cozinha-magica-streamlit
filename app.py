import streamlit as st
from PIL import Image

st.set_page_config(page_title="Escape Room Nutrição para Crianças", page_icon="🍎", layout="wide")

st.title("Bem-vindo à Escape Room da Nutrição! 🥦🍎")
st.write("Ajude o herói a escapar das salas resolvendo enigmas sobre comida saudável. Para crianças de 6-12 anos. Complete uma sala para desbloquear a próxima!")

# Imagem de introdução
try:
    bg_image = Image.open("assets/background_escape.jpg")
    st.image(bg_image, caption="Aventura começa aqui!", use_column_width=True)
except FileNotFoundError:
    st.write("Imagem de fundo não encontrada.")

# Controle de progresso
if 'progresso' not in st.session_state:
    st.session_state.progresso = 0

# Sidebar para navegação
st.sidebar.title("Salas da Aventura")
if st.session_state.progresso >= 0:
    st.sidebar.markdown("[Sala 1: Pirâmide Alimentar](./Sala_1_Pirâmide_Alimentar)")
if st.session_state.progresso >= 1:
    st.sidebar.markdown("[Sala 2: Frutas e Vegetais](./Sala_2_Frutas_e_Vegetais)")
if st.session_state.progresso >= 2:
    st.sidebar.markdown("[Sala 3: Refeição Equilibrada](./Sala_3_Refeição_Equilibrada)")
if st.session_state.progresso >= 3:
    st.sidebar.markdown("[Sala Final: Vitória!](./Sala_Final_Vitória)")

st.write("Comece pela Sala 1 no menu lateral.")
