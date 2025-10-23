import streamlit as st
from PIL import Image, UnidentifiedImageError
import os

st.set_page_config(
    page_title="Escape Room Nutrição",
    page_icon="🍎",
    layout="wide"
)

# Inicializa progresso
if "progresso" not in st.session_state:
    st.session_state.progresso = 0

# CSS básico
st.markdown("""
<style>
.main-title {text-align:center;color:#2C6E49;font-size:2.2em;font-weight:700;}
.subtitle {text-align:center;color:#FF8C00;font-size:1.3em;}
.stButton>button {background-color:#FF8C00;color:white;font-weight:bold;border-radius:10px;height:3em;width:100%;}
.stButton>button:hover {background-color:#FFA733;}
[data-testid="stSidebar"] {background-color:#F0FFF0;color:#333;}
</style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown('<p class="main-title">🏰 Escape Room da Nutrição 🥦🍎</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ajude o herói a escapar das salas resolvendo enigmas sobre comida saudável!</p>', unsafe_allow_html=True)

# Carrega imagem de fundo com segurança
bg_path = "assets/background.jpg"
bg_image = None
if os.path.exists(bg_path):
    try:
        bg_image = Image.open(bg_path).convert("RGB")
        # Redimensiona para largura máxima 1200px
        max_width = 1200
        w_percent = max_width / float(bg_image.size[0])
        h_size = int(float(bg_image.size[1]) * w_percent)
        bg_image = bg_image.resize((max_width, h_size))
    except (UnidentifiedImageError, OSError):
        st.warning("⚠️ A imagem de fundo existe, mas não pôde ser aberta.")
else:
    st.warning("⚠️ Imagem de fundo não encontrada.")

if bg_image:
    st.image(bg_image, caption="A aventura começa aqui!", use_container_width=True)

# Barra de progresso
st.progress(st.session_state.progresso / 3)

# Sidebar
st.sidebar.title("Salas da Aventura")
if st.session_state.progresso >= 0:
    st.sidebar.markdown("1️⃣ Sala 1: Pirâmide Alimentar")
if st.session_state.progresso >= 1:
    st.sidebar.markdown("2️⃣ Sala 2: Frutas e Vegetais")
if st.session_state.progresso >= 2:
    st.sidebar.markdown("3️⃣ Sala 3: Refeição Equilibrada")
if st.session_state.progresso >= 3:
    st.sidebar.markdown("🏆 Sala Final: Vitória!")

# Botão inicial
if st.session_state.progresso == 0:
    if st.button("🚪 Começar a aventura"):
        st.experimental_rerun()
