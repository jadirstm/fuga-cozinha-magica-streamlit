import streamlit as st
from PIL import Image

# ------------------------------
# Configuração do app
# ------------------------------
st.set_page_config(
    page_title="Escape Room Nutrição para Crianças",
    page_icon="🍎",
    layout="wide"
)

# Inicializa progresso
if "progresso" not in st.session_state:
    st.session_state.progresso = 0

# ------------------------------
# CSS para personalização global
# ------------------------------
st.markdown("""
<style>
/* Títulos e subtítulos */
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
/* Botões */
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
    color: white;
}
/* Sidebar */
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
# Imagem de introdução
# ------------------------------
try:
    bg_image = Image.open("assets/background_escape.jpg")
    st.image(bg_image, caption="A aventura começa aqui!", use_container_width=True)
except FileNotFoundError:
    st.warning("Imagem de fundo não encontrada. Verifique a pasta assets.")

# ------------------------------
# Barra de progresso
# ------------------------------
st.progress(st.session_state.progresso / 3)

# ------------------------------
# Navegação pelas salas
# ------------------------------
st.sidebar.title("Salas da Aventura")
st.sidebar.write("Clique em uma sala para navegar:")

# Deixa Streamlit criar menu automático via pages (melhor prática)
# O menu lateral mostra as páginas automaticamente

# ------------------------------
# Botão de início
# ------------------------------
if st.session_state.progresso == 0:
    if st.button("🚪 Começar a aventura"):
        st.session_state.progresso = 0
        st.experimental_rerun()
