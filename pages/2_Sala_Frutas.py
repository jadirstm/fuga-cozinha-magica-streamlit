import streamlit as st
from PIL import Image

st.markdown('<p class="main-title">Sala 2: Enigma das Frutas e Vegetais 🌽🍇</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Selecione 3 saudáveis ricos em vitaminas!</p>', unsafe_allow_html=True)

# ------------------------------
# Imagens em colunas
# ------------------------------
cols = st.columns(3)
imagens = [
    ("Maçã", "assets/frutas.jpg"),
    ("Cenoura", "assets/vegetais.jpg"),
    ("Chocolate", "assets/doce_chocolate.jpg")
]

for col, (nome, path) in zip(cols, imagens):
    try:
        img = Image.open(path)
        col.image(img, caption=nome)
    except FileNotFoundError:
        col.write(nome)

# ------------------------------
# Seleção do usuário
# ------------------------------
selecoes = st.multiselect("Escolha 3:", ["Maçã", "Cenoura", "Chocolate", "Banana", "Brócolis", "Batata Frita"])

# ------------------------------
# Botão de verificação
# ------------------------------
if st.button("Verificar"):
    acertos = {"Maçã", "Cenoura", "Banana", "Brócolis"}
    if set(selecoes).issubset(acertos) and len(selecoes) == 3:
        st.success("🥳 Ótimo! Frutas e vegetais = vitaminas. Sala 2 liberada!")
        st.session_state.progresso = 2
        st.balloons()
        if st.button("➡️ Ir para Sala 3"):
            st.experimental_set_query_params(page="3_Sala_Prato")
            st.experimental_rerun()
    else:
        st.error("❌ Evite doces/fritos. Tente novamente!")
