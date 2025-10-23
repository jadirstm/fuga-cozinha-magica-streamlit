import streamlit as st
from PIL import Image

st.title("Sala 1: A Pirâmide Alimentar 🏔️")
st.write("Para escapar, responda: O que fica na base da pirâmide (mais importante)?")

# Imagem interativa
try:
    piramide = Image.open("assets/piramide_alimentar.jpg")
    st.image(piramide, caption="Dica: Olhe a pirâmide!", use_container_width=True)
except FileNotFoundError:
    st.write("Imagem da pirâmide não encontrada.")

opcoes = ["Doces e gorduras", "Grãos e pães", "Carnes e ovos"]
resposta = st.radio("Escolha:", opcoes)

if st.button("Verificar"):
    if resposta == opcoes[1]:
        st.success("Correto! Grãos dão energia. Sala 1 liberada! 🎉")
        st.session_state.progresso = 1
        st.balloons()
        st.write("Vá para Sala 2.")
    else:
        st.error("Errado! Dica: Energia vem de pão, arroz. Tente novamente!")
