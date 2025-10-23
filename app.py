# app.py
import streamlit as st
import random
import time

# === CONFIGURAÇÃO DA PÁGINA ===
st.set_page_config(
    page_title="Fuga da Cozinha Mágica",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# === ESTILOS PERSONALIZADOS (CSS INJETADO) ===
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #a8e6cf, #ffd93d); }
    .titulo { font-family: 'Comic Neue', cursive; color: #e74c3c; text-shadow: 2px 2px #fff; }
    .sala { background: white; padding: 20px; border-radius: 20px; box-shadow: 0 8px 20px rgba(0,0,0,0.2); margin: 20px 0; }
    .alimento { text-align: center; cursor: pointer; transition: 0.3s; padding: 10px; border-radius: 15px; }
    .alimento:hover { background: #fff3cd; transform: scale(1.05); }
    .certo { color: #27ae60; font-weight: bold; }
    .erro { color: #e74c3c; font-weight: bold; }
    .trofeu { width: 200px; border-radius: 50%; border: 6px solid #ffd700; }
</style>
""", unsafe_allow_html=True)

# === INICIALIZAR ESTADO DO JOGO ===
if 'progresso' not in st.session_state:
    st.session_state.progresso = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}
if 'prato_final' not in st.session_state:
    st.session_state.prato_final = {}

# === FUNÇÃO PARA TOCAR SOM (usando HTML5) ===
def tocar_som(tipo):
    sons = {
        'certo': '/assets/sounds/certo.mp3',
        'erro': '/assets/sounds/erro.mp3',
        'vitoria': '/assets/sounds/vitoria.mp3'
    }
    st.components.v1.html(f"""
    <audio autoplay>
        <source src="{sons[tipo]}" type="audio/mpeg">
    </audio>
    """, height=0)

# === FUNÇÃO PARA SALA GENÉRICA ===
def sala(num, titulo, pergunta, opcoes, corretas, imagens, aprendizado):
    st.markdown(f"<div class='sala'><h2 class='titulo'>SALA {num}: {titulo}</h2>", unsafe_allow_html=True)
    st.write(pergunta)

    cols = st.columns(len(opcoes))
    escolha = None

    for i, (texto, img) in enumerate(zip(opcoes, imagens)):
        with cols[i]:
            if st.button(f"{texto}", key=f"btn_{num}_{i}"):
                escolha = texto
                st.session_state.respostas[num] = texto
                if texto in corretas:
                    st.success("CORRETO!")
                    tocar_som('certo')
                    st.balloons()
                    time.sleep(1)
                    st.session_state.progresso = num
                    st.rerun()
                else:
                    st.error("OPS! Tente novamente.")
                    tocar_som('erro')
            st.image(img, width=120, caption=texto)

    if st.session_state.get(f'resposta_{num}') == 'errada':
        st.markdown("<p class='erro'>Tente de novo! Dica: escolha o mais saudável!</p>", unsafe_allow_html=True)

    st.markdown(f"<p><em>{aprendizado}</em></p></div>", unsafe_allow_html=True)

# === REGRAS DE PROGRESSÃO ===
def pode_avancar(sala):
    return st.session_state.progresso >= sala

# === JOGO PRINCIPAL ===
st.markdown("<h1 class='titulo'>FUGA DA COZINHA MÁGICA</h1>", unsafe_allow_html=True)
st.markdown("**Monte um prato saudável e escape da cozinha encantada!**")

# === SALA 1: CARBOIDRATOS ===
if st.session_state.progresso == 0:
    sala(
        1, "ENERGIA PARA BRINCAR!",
        "Qual alimento te dá energia **duradoura** para brincar o dia todo?",
        ["Arroz", "Pão integral", "Bolo", "Refrigerante"],
        ["Arroz", "Pão integral"],
        [
            "assets/img/arroz.png",
            "assets/img/pao.png",
            "assets/img/bolo.png",
            "assets/img/refrigerante.png"
        ],
        "Carboidratos complexos liberam energia aos poucos. Evite açúcar!"
    )

# === SALA 2: PROTEÍNAS ===
elif st.session_state.progresso == 1:
    sala(
        2, "CRESCER FORTE!",
        "Qual alimento ajuda seus músculos a crescerem?",
        ["Frango", "Feijão", "Sorvete", "Pizza"],
        ["Frango", "Feijão"],
        [
            "assets/img/frango.png",
            "assets/img/feijao.png",
            "assets/img/sorvete.png",
            "assets/img/pizza.png"
        ],
        "Proteínas são os 'tijolos' do corpo. Coma todos os dias!"
    )

# === SALA 3: VITAMINAS ===
elif st.session_state.progresso == 2:
    sala(
        3, "VITAMINAS COLORIDAS!",
        "Qual alimento tem **muitas vitaminas** para te proteger?",
        ["Laranja", "Morango", "Bala", "Batata frita"],
        ["Laranja", "Morango"],
        [
            "assets/img/laranja.png",
            "assets/img/morango.png",
            "assets/img/bala.png",
            "assets/img/batata.png"
        ],
        "Frutas coloridas = vitaminas A, C, E. Quanto mais cor, melhor!"
    )

# === SALA 4: HIDRATAÇÃO ===
elif st.session_state.progresso == 3:
    sala(
        4, "ÁGUA É VIDA!",
        "Qual bebida hidrata **de verdade**?",
        ["Água", "Suco natural", "Refrigerante", "Suco de caixinha"],
        ["Água", "Suco natural"],
        [
            "assets/img/agua.png",
            "assets/img/suco.png",
            "assets/img/refrigerante.png",
            "assets/img/caixinha.png"
        ],
        "Água é essencial! Beba 6-8 copos por dia."
    )

# === SALA 5: PRATO FINAL (COMBINAÇÃO OBRIGATÓRIA) ===
elif st.session_state.progresso == 4:
    st.markdown("<div class='sala'>", unsafe_allow_html=True)
    st.subheader("SALA 5: MONTE SEU PRATO MÁGICO!")
    st.write("Arraste os alimentos para formar um **prato equilibrado**!")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        carb = st.selectbox("Carboidrato", ["Arroz", "Pão integral", "Macarrão", "Bolo"], key="carb")
        st.image(f"assets/img/{carb.lower().replace(' ', '')}.png", width=100)

    with col2:
        prot = st.selectbox("Proteína", ["Frango", "Feijão", "Ovo", "Hambúrguer"], key="prot")
        st.image(f"assets/img/{prot.lower().replace(' ', '')}.png", width=100)

    with col3:
        vit = st.selectbox("Vitamina", ["Laranja", "Morango", "Salada", "Bala"], key="vit")
        st.image(f"assets/img/{vit.lower().replace(' ', '')}.png", width=100)

    with col4:
        bebida = st.selectbox("Bebida", ["Água", "Suco natural", "Refrigerante"], key="bebida")
        st.image(f"assets/img/{bebida.lower().replace(' ', '')}.png", width=100)

    # === COMBINAÇÃO CORRETA OBRIGATÓRIA ===
    combinacao_correta = {
        "carb": ["Arroz", "Pão integral"],
        "prot": ["Frango", "Feijão", "Ovo"],
        "vit": ["Laranja", "Morango", "Salada"],
        "bebida": ["Água", "Suco natural"]
    }

    if st.button("MONTAR PRATO!"):
        correto = (
            carb in combinacao_correta["carb"] and
            prot in combinacao_correta["prot"] and
            vit in combinacao_correta["vit"] and
            bebida in combinacao_correta["bebida"]
        )

        if correto:
            st.session_state.prato_final = {"carb": carb, "prot": prot, "vit": vit, "bebida": bebida}
            st.success("PRATO PERFEITO! Você escapou!")
            tocar_som('vitoria')
            st.balloons()
            st.session_state.progresso = 5
            st.rerun()
        else:
            st.error("Faltou equilíbrio! Tente novamente.")
            tocar_som('erro')

    st.markdown("</div>", unsafe_allow_html=True)

# === TELA DE VITÓRIA COM BENEFÍCIOS ===
else:
    st.markdown("<div class='sala'>", unsafe_allow_html=True)
    st.header("VOCÊ ESCAPOU DA COZINHA MÁGICA!")
    st.image("assets/img/trofeu.gif", width=200, caption="Campeão da Nutrição!")

    prato = st.session_state.prato_final
    st.markdown(f"""
    ### Seu Prato Vencedor:
    - **{prato['carb']}** → Energia duradoura  
    - **{prato['prot']}** → Músculos fortes  
    - **{prato['vit']}** → Imunidade alta  
    - **{prato['bebida']}** → Hidratação perfeita  
    """)

    st.markdown("### Benefícios da Sua Conquista:")
    st.info("""
    - Energia para brincar o dia todo  
    - Cresce forte e saudável  
    - Fica doente com menos frequência  
    - Se concentra melhor na escola  
    - Tem mais disposição e alegria!  
    """)

    if st.button("Jogar Novamente!"):
        st.session_state.clear()
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# === RODAPÉ ===
st.markdown("---")
st.markdown("<p style='text-align:center; color:#555;'>Criado com ❤️ para crianças curiosas | Nutrição é diversão!</p>", unsafe_allow_html=True)
