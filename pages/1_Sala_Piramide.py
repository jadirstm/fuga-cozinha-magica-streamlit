import streamlit as st
from PIL import Image

# ------------------------------
# Cabeçalho
# ------------------------------
st.markdown('<p class="main-title">Sala 1: A Pirâmide Alimentar 🏔️</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Descubra o que é essencial para a sua energia!</p>', unsafe_allow_html=True)

# ------------------------------
# Imagem interativa
# ------------------------------
try:
    piramide = Image.open("assets/piramide.jpg")
    st.image(piramide, caption="Dica: Olhe a pirâmide!", use_container_width=True)
except FileNotFoundError:
    st.warning("Imagem da pirâmide não encontrada.")

# ------------------------------
# Pergunta e opções
# ------------------------------
opcoes = ["Doces e gorduras", "Grãos e pães", "Carnes e ovos"]
resposta = st.radio("Escolha:", opcoes)

# ------------------------------
# Botão de verificação
# ------------------------------
if st.button("Verificar"):
    if resposta == "Grãos e pães":
        st.success("🎉 Você acertou! Grãos dão energia para correr e brincar!")
        st.session_state.progresso = 1
        st.balloons()
        if st.button("➡️ Ir para a Sala 2"):
            st.experimental_set_query_params(page="2_Sala_Frutas")
            st.experimental_rerun()
    else:
        st.error("❌ Quase! Pense no que dá energia logo de manhã...")
