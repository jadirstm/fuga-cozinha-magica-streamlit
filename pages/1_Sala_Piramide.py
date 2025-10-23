import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">Sala 1: A Pirâmide Alimentar 🏔️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Descubra o que é essencial para a sua energia!</p>', unsafe_allow_html=True)

# Imagem da pirâmide
path = "assets/piramide.jpg"
if os.path.exists(path):
    try:
        piramide = Image.open(path).convert("RGB")
        st.image(piramide, caption="Dica: Olhe a pirâmide!", use_container_width=True)
    except (UnidentifiedImageError, OSError):
        st.warning("⚠️ Imagem da pirâmide inválida. Reexporte como JPG.")
else:
    st.warning("⚠️ Imagem da pirâmide não encontrada.")

# Pergunta
opcoes = ["Doces e gorduras", "Grãos e pães", "Carnes e ovos"]
resposta = st.radio("Escolha:", opcoes)

if st.button("Verificar"):
    if resposta == "Grãos e pães":
        st.success("🎉 Você acertou! Grãos dão energia para correr e brincar!")
        st.session_state.progresso = 1
        st.balloons()
    else:
        st.error("❌ Quase! Pense no que dá energia logo de manhã...")
