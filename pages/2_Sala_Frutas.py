import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.markdown('<p class="main-title">Sala 2: Frutas e Vegetais 🌽🍇</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Selecione 3 saudáveis ricos em vitaminas!</p>', unsafe_allow_html=True)

cols = st.columns(3)
imagens = [("Maçã", "assets/fruta_maca.jpg"), 
           ("Cenoura", "assets/vegetal_cenoura.jpg"), 
           ("Chocolate", "assets/doce_chocolate.jpg")]

for col, (nome, path) in zip(cols, imagens):
    if os.path.exists(path):
        try:
            col.image(Image.open(path).convert("RGB"), caption=nome)
        except:
            col.write(f"⚠️ Imagem {nome} inválida")
    else:
        col.write(f"⚠️ Imagem {nome} não encontrada")

selecoes = st.multiselect("Escolha 3:", ["Maçã", "Cenoura", "Chocolate", "Banana", "Brócolis", "Batata Frita"])
if st.button("Verificar"):
    acertos = {"Maçã", "Cenoura", "Banana", "Brócolis"}
    if set(selecoes).issubset(acertos) and len(selecoes) == 3:
        st.success("🥳 Sala 2 liberada!")
        st.session_state.progresso = 2
        st.balloons()
    else:
        st.error("❌ Evite doces/fritos.")
