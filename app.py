import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

# ------------------------------
# Configuração do app
# ------------------------------
st.set_page_config(
    page_title="Escape Room Nutrição para Crianças",
    page_icon="🍎",
    layout="wide"
)

# ------------------------------
# Inicializa progresso
# ------------------------------
if "progresso" not in st.session_state:
    st.session_state.progresso = 0

# ------------------------------
# CSS para personalização
# ------------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    color: #2C6E49;
    font-size: 2.2em;
    font-weight: 700;
}
.subtitle {
    text-align: center;
    color: #FF8C00;
    font-size: 1.3em;
}
.stButton>button {
    background-color: #FF8C00;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}
.stButton>button:hover {
    background-color: #FFA733;
}
[data-testid="stSidebar"] {
    background-color: #F0FFF0;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Cabeçalho
# ------------------------------
st.markdown('<p class="main-title">🏰 Escape Room da Nutrição 🥦🍎</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ajude o herói a escapar das salas resolvendo enigmas sobre comida saudável!</p>', unsafe_allow_html=True)

# ------------------------------
# Imagem de fundo segura
# ------------------------------
bg_path = "assets/background_escape.jpg"
bg_image = None
if os.path.exists(bg_path):
    try:
        img = Image.open(bg_path)
        img.verify()  # Confirma se é uma imagem válida
        bg_image = Image.open(bg_path)  # Reabre para exibição
    except (UnidentifiedImageError, IOError):
        st.warning("⚠️ A imagem de fundo existe, mas não pôde ser aberta. Reexporte como JPG válido.")
else:
    st.warning("⚠️ Imagem de fundo não encontrada em assets/")

if bg_image:
    st.image(bg_image, caption="A aventura começa aqui!", use_container_width=True)

# ------------------------------
# Barra de progresso
# ------------------------------
st.progress(st.session_state.progresso / 3)

# ------------------------------
# Botão iniciar
# ------------------------------
if st.session_state.progresso == 0:
    if st.button("🚪 Começar a aventura"):
        st.session_state.progresso = 0
        st.experimental_rerun()
