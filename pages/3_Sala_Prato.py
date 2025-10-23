import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">Sala 3: Desafio da Refeição Equilibrada 🍽️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Monte um prato equilibrado!</p>', unsafe_allow_html=True)

# Imagem do prato
path = "assets/prato.jpg"
if os.path.exists(path):
    try:
        prato = Image.open(path).convert("RGB")
        st.image(prato, caption="Exemplo de prato equilibrado", use_container_width=True)
    except (UnidentifiedImageError, OSError):
        st.warning("⚠️ Imagem do prato inválida.")
else:
    st.warning("⚠️ Imagem do prato não encontrada.")

# Seleção
componentes = st.multiselect(
    "Adicione:", 
    ["Arroz (grão)", "Frango (proteína)", "Salada (vegetal)", "Maçã (fruta)", "Refrigerante (errado)"]
)

if st.button("Montar"):
    if len(componentes) == 4 and "Refrigerante (errado)" not in componentes:
        st.success("🌟 Perfeito! Equilibrado. Sala 3 liberada!")
        st.session_state.progresso = 3
        st.balloons()
    else:
        st.error("❌ Sem bebidas açucaradas! Tente novamente.")
