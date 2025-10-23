import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">🏆 Parabéns! Você Escapou!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aprendeu: Coma variado, beba água e evite excessos!</p>', unsafe_allow_html=True)

path = "assets/vitoria.jpg"
if os.path.exists(path):
    try:
        vitoria = Image.open(path).convert("RGB")
        st.image(vitoria, caption="Celebração!", use_container_width=True)
    except (UnidentifiedImageError, OSError):
        st.warning("⚠️ Imagem de vitória inválida.")
else:
    st.warning("⚠️ Imagem de vitória não encontrada.")

st.balloons()
st.info("Resumo: Pirâmide guia, frutas diárias, refeições equilibradas.")

if st.button("🔄 Reiniciar aventura"):
    st.session_state.progresso = 0
    st.experimental_rerun()
