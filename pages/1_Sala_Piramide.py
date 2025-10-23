import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">Sala 1: A Pirâmide Alimentar 🏔️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Descubra o que é essencial para a sua energia!</p>', unsafe_allow_html=True)

path = "assets/piramide.jpg"
if os.path.exists(path):
    try:
        piramide = Image.open(path).convert("RGB")
        st.image(piramide, caption="Dica: Olhe a pirâmide!", use_container_width=True)
    except:
        st.warning("⚠️ Imagem inválida.")
else:
    st.warning("⚠️ Imagem não encontrada.")

opcoes = ["Doces e gorduras", "Grãos e pães", "Carnes e ovos"]
resposta = st.radio("Escolha:", opcoes)
if st.button("Verificar"):
    if resposta == "Grãos e pães":
        st.success("🎉 Correto! Sala 1 liberada!")
        st.session_state.progresso = 1
        st.balloons()
    else:
        st.error("❌ Quase! Pense no que dá energia.")
