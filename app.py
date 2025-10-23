import streamlit as st
import base64
from io import BytesIO

# Configuração da página (linda para crianças!)
st.set_page_config(
    page_title="Fuga da Cozinha Mágica",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Função para imagens base64 (embutidas, sem precisar de pastas)
@st.cache_data
def get_img_as_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Mas como estamos online, usaremos links de imagens grátis do Unsplash/Pixabay (ou cole URLs aqui)
# Exemplo: st.image("https://example.com/arroz.png")

# Estado do jogo (progresso das salas)
if 'progresso' not in st.session_state:
    st.session_state.progresso = 0

# Título principal
st.title("🧙‍♀️ FUGA DA COZINHA MÁGICA! 🧙‍♂️")
st.markdown("***Monte um prato saudável e escape da cozinha encantada!***")

# Função para cada sala (modular e fácil de editar)
def mostrar_sala(num_sala, titulo, pergunta, opcoes_corretas, opcoes_erradas, imagem_correta, imagem_errada, aprendizado):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"**Sala {num_sala}: {titulo}**")
        st.write(pergunta)
        st.image(imagem_correta, width=150, caption="Alimento Saudável")
    
    with col2:
        st.image(imagem_errada, width=150, caption="Alimento Não Saudável")
    
    # Quiz interativo (botões para crianças)
    opcoes = opcoes_corretas + opcoes_erradas
    import random
    random.shuffle(opcoes)  # Embaralha para desafio
    
    resposta = st.radio("Escolha o alimento certo!", opcoes, key=f"sala_{num_sala}")
    
    if st.button("Enviar Resposta! 🚀", key=f"btn_{num_sala}"):
        if resposta in opcoes_corretas:
            st.success("🎉 CERTO! Você aprendeu: " + aprendizado)
            st.balloons()  # Animação fofa!
            st.session_state.progresso = num_sala
            st.rerun()
        else:
            st.error("😅 Ops! Tente de novo. Lembre: escolha o saudável!")
            st.markdown("### Dica: Alimentos coloridos e naturais são os melhores! 🌈")

# Lógica do jogo
if st.session_state.progresso == 0:
    # Sala 1: Carboidratos (Energia)
    mostrar_sala(
        1, "Energia para Brincar!", 
        "Qual alimento te dá energia para correr e pular o dia todo?",
        ["Arroz 🍚", "Pão integral 🥖"], 
        ["Chocolate 🍫", "Refrigerante 🥤"],
        "https://images.unsplash.com/photo-1542838138-cf3f4f0b73a0?w=200",  # Arroz
        "https://images.unsplash.com/photo-1577968897966-7d436ca249dc?w=200",  # Chocolate
        "Carboidratos como arroz dão energia duradoura!"
    )
    
elif st.session_state.progresso == 1:
    # Sala 2: Proteínas (Crescer Forte)
    mostrar_sala(
        2, "Crescer Forte!", 
        "Qual ajuda seus músculos a crescerem fortes?",
        ["Frango 🍗", "Ovo 🥚"], 
        ["Sorvete 🍦", "Bolo 🍰"],
        "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=200",  # Frango
        "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=200",  # Sorvete
        "Proteínas constroem músculos e te deixam forte como um super-herói!"
    )
    
elif st.session_state.progresso == 2:
    # Sala 3: Vitaminas (Cores Saudáveis)
    mostrar_sala(
        3, "Vitaminas Coloridas!", 
        "Qual fruta colorida te dá vitaminas para ficar bem?",
        ["Laranja 🍊", "Morango 🍓"], 
        ["Bala 🍬", "Chipps 🥨"],
        "https://images.unsplash.com/photo-1540206395-68808572332f?w=200",  # Laranja
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=200",  # Bala
        "Frutas coloridas protegem sua saúde e te deixam feliz!"
    )
    
elif st.session_state.progresso == 3:
    # Sala 4: Hidratação (Água é Vida)
    mostrar_sala(
        4, "Beba Água!", 
        "O que hidrata melhor no calor?",
        ["Água 💧"], 
        ["Refrigerante 🥤", "Suco de caixinha 🧃"],
        "https://images.unsplash.com/photo-1579586145622-7a4e5b8ca758?w=200",  # Água
        "https://images.unsplash.com/photo-1577968897966-7d436ca249dc?w=200",  # Refrigerante
        "Água é o melhor amigo do corpo – beba 8 copos por dia!"
    )
    
elif st.session_state.progresso == 4:
    # Sala 5: Prato Equilibrado (Final)
    st.subheader("**Sala 5: Monte Seu Prato Mágico!**")
    st.write("Arraste alimentos para o prato e crie uma refeição colorida!")
    
    # Simulação de drag-and-drop simples com selects (fácil para mobile)
    carb = st.selectbox("Escolha um carboidrato:", ["Arroz 🍚", "Pão 🥖"])
    prot = st.selectbox("Escolha uma proteína:", ["Frango 🍗", "Feijão 🌱"])
    fru = st.selectbox("Escolha uma fruta:", ["Laranja 🍊", "Banana 🍌"])
    bebida = st.selectbox("Escolha uma bebida:", ["Água 💧"])
    
    if st.button("Montar Prato! ✨"):
        st.success("🏆 PRATO PERFEITO! Equilíbrio é a chave da saúde!")
        st.markdown("### Seu Prato: " + carb + " + " + prot + " + " + fru + " + " + bebida)
        st.balloons()
        st.session_state.progresso = 5
        st.rerun()
    
else:
    # Tela de Vitória
    st.header("🎊 VOCÊ ESCAPOU DA COZINHA MÁGICA! 🎊")
    st.balloons()
    st.markdown("**Parabéns, Nutricionista Mirim!** Você aprendeu a montar pratos saudáveis e coloridos. Compartilhe com amigos! 🌟")
    if st.button("Jogar Novamente! 🔄"):
        st.session_state.progresso = 0
        st.rerun()

# Rodapé educativo
st.sidebar.title("💡 Dicas de Nutrição")
st.sidebar.markdown("""
- **Coma colorido:** Mais cores = mais vitaminas!  
- **Beba água:** Seu corpo agradece!  
- **Equilíbrio:** Um pouco de tudo faz bem.  
[Criado com ❤️ para crianças curiosas]
""")
