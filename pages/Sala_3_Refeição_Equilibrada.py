import streamlit as st
from PIL import Image

st.markdown('<p class="main-title">Sala 3: Desafio da Refeição Equilibrada 🍽️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Monte um prato equilibrado!</p>', unsafe_allow_html=True)

# ------------------------------
# Imagem exemplo
# ------------------------------
try:
    prato = Image.open("assets/prato.jpg")
    st.image(prato, caption="Exemplo de prato equilibrado", use_container_width=True)
except FileNotFoundError:
    st.warning("Imagem do prato não encontrada.")

# ------------------------------
# Seleção do prato
# ------------------------------
componentes = st.multiselect("Adicione:", ["Arroz (grão)", "Frango (proteína)", "Salada (vegetal)", "Maçã (fruta)", "Refrigerante (errado)"])

# ------------------------------
# Verificação
# ------------------------------
if st.button("Montar"):
    if len(componentes) == 4 and "Refrigerante (errado)" not in componentes:
        st.success("🌟 Perfeito! Equilibrado. Sala 3 liberada!")
        st.session_state.progresso = 3
        st.balloons()
        if st.button("➡️ Ir para Sala Final"):
            st.experimental_set_query_params(page="4_Sala_Vitoria")
            st.experimental_rerun()
    else:
        st.error("❌ Sem bebidas açucaradas! Tente novamente.")
