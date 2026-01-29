import streamlit as st

def local_css():
    st.markdown("""
    <style>
        /* Changer la couleur de fond principale */
        .stApp {
            background-color: #f1f8e9; /* Un vert très pâle */
        }
        
        /* Personnaliser les bulles de chat */
        [data-testid="stChatMessage"] {
            background-color: #ffffff;
            border-radius: 15px;
            border: 1px solid #c5e1a5;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }

        /* Titres en vert forêt */
        h1, h2, h3 {
            color: #2e7d32 !important;
            font-family: 'Helvetica Neue', sans-serif;
        }

        /* Modifier la barre de saisie */
        .stChatInputContainer {
            padding-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

st.title("🌳 Des Hommes et des Arbres")
st.caption("Explorez les liens entre thématiques, impacts et grandes variables")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("De quoi dépend la production de bois par les forêts ?   "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = "Message du backend" 
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("À propos")
    st.write("""
    **Des Hommes et des Arbres**
    
    Un collectif engagé pour l’avenir, avec et pour les arbres
    """)
    st.divider()
    st.success("🌱 51 projets labellisés dans le Grand Est")
    
    # Petit curseur pour ajuster le "ton" de l'IA (Créativité)
    temperature = st.slider("Niveau d'inspiration de l'IA", 0.0, 1.0, 0.7)