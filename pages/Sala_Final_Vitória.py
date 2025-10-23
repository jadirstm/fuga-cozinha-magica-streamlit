import streamlit as st
from PIL import Image

st.title("Parabéns! Você Escapou! 🏆")
st.write("Aprendeu: Coma variado, beba água, evite excessos!")

try:
    vitoria = Image.open("assets/imagem_vitoria.jpg")
    st.image(vitoria, caption="Celebração!", use_column_width=True)
except:
    st.write("Imagem de vitória não encontrada.")

st.balloons()
st.write("Resumo: Pirâmide guia, frutas diárias, refeições equilibradas.")
if st.button("Reiniciar"):
    st.session_state.progresso = 0
    st.experimental_rerun()
