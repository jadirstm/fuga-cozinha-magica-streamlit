import streamlit as st
from PIL import Image

st.title("Sala 2: Enigma das Frutas e Vegetais 🌽🍇")
st.write("Selecione 3 saudáveis ricos em vitaminas!")

# Imagens em colunas
cols = st.columns(3)
with cols[0]:
    try:
        img1 = Image.open("assets/fruta_maca.jpg")
        st.image(img1, caption="Maçã")
    except:
        st.write("Maçã")
with cols[1]:
    try:
        img2 = Image.open("assets/vegetal_cenoura.jpg")
        st.image(img2, caption="Cenoura")
    except:
        st.write("Cenoura")
with cols[2]:
    try:
        img3 = Image.open("assets/doce_chocolate.jpg")
        st.image(img3, caption="Chocolate")
    except:
        st.write("Chocolate")

selecoes = st.multiselect("Escolha 3:", ["Maçã", "Cenoura", "Chocolate", "Banana", "Brócolis", "Batata Frita"])
if st.button("Verificar"):
    if set(selecoes) in [{"Maçã", "Cenoura", "Banana"}, {"Maçã", "Cenoura", "Brócolis"}]:
        st.success("Ótimo! Frutas/vegetais = vitaminas. Sala 2 liberada! 🥳")
        st.session_state.progresso = 2
        st.balloons()
    else:
        st.error("Evite doces/fritos. Tente novamente!")
