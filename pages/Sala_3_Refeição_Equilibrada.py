import streamlit as st
from PIL import Image

st.title("Sala 3: Desafio da Refeição Equilibrada 🍽️")
st.write("Monte um prato: 1/2 vegetais/frutas, 1/4 grãos, 1/4 proteínas.")

# Imagem exemplo
try:
    prato = Image.open("assets/prato_equilibrado.jpg")
    st.image(prato, caption="Exemplo de prato equilibrado", use_container_width=True)
except:
    st.write("Imagem do prato não encontrada.")

componentes = st.multiselect("Adicione:", ["Arroz (grão)", "Frango (proteína)", "Salada (vegetal)", "Maçã (fruta)", "Refrigerante (errado)"])
if st.button("Montar"):
    if len(componentes) == 4 and "Refrigerante (errado)" not in componentes:
        st.success("Perfeito! Equilibrado. Sala 3 liberada! 🌟")
        st.session_state.progresso = 3
        st.balloons()
    else:
        st.error("Sem bebidas açucaradas! Tente novamente.")
