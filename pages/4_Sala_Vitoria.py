import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">🏆 Parabéns! Você Escapou!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aprendeu: Coma variado, beba água e evite excessos!</p>', unsafe_allow_html=True)

path = "assets/vitoria.jpg"
if os.path.exists(path):
    try:
        st.image(Image.open(path).convert("RGB"), caption="Celebração!", use_container_width=True)
    except:
        st.warning("⚠️ Imagem inválida")
else:
    st.warning("⚠️ Imagem não encontrada")

if st.button("Reiniciar"):
    st.session_state.progresso = 0
    st.experimental_rerun()
