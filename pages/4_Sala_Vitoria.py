import streamlit as st
from PIL import Image

st.markdown('<p class="main-title">🏆 Parabéns! Você Escapou!</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Aprendeu: Coma variado, beba água e evite excessos!</p>', unsafe_allow_html=True)

# ------------------------------
# Imagem de vitória
# ------------------------------
try:
    vitoria = Image.open("assets/vitoria.jpg")
    st.image(vitoria, caption="Celebração!", use_container_width=True)
except FileNotFoundError:
    st.warning("Imagem de vitória não encontrada.")

# ------------------------------
# Feedback final
# ------------------------------
st.balloons()
st.info("Resumo: Pirâmide guia, frutas diárias, refeições equilibradas.")

# ------------------------------
# Botão reiniciar
# ------------------------------
if st.button("🔄 Reiniciar aventura"):
    st.session_state.progresso = 0
    st.experimental_rerun()
