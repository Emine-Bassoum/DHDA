import streamlit as st
import requests  # N'oublie pas d'installer requests (pip install requests)

# Configuration de l'URL du backend
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Des Hommes et Des Arbres",
    page_icon="https://deshommesetdesarbres.org/wp-content/uploads/2021/03/cropped-favicon-dhda-32x32.png", # Teste avec cet emoji d'abord
    layout="wide"
)

def apply_dhda_design():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        /* 1. Cache le bouton Deploy et le footer Streamlit sans bloquer le menu */
        .stAppDeployButton { display: none !important; }
        footer { visibility: hidden; }
        
        /* 2. Rendre le header discret mais laisser le menu accessible */
        header {
            background-color: rgba(0,0,0,0) !important;
            border-bottom: none !important;
        }

        /* Le reste de ton design DHDA */
        html, body, [class*="css"] { font-family: 'Roboto', sans-serif; color: #333333; }
        :root { --dhda-magenta: #d100ff; }
        .stApp { background-color: #FFFFFF; }
        
        h1 {
            color: #1a1a1a !important;
            font-weight: 700 !important;
            border-bottom: 2px solid var(--dhda-magenta);
            padding-bottom: 10px;
        }

        .stButton>button {
            border-radius: 50px !important;
            border: 2px solid var(--dhda-magenta) !important;
            color: var(--dhda-magenta) !important;
            background-color: transparent;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: var(--dhda-magenta) !important;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

apply_dhda_design()
st.image("./logo_DHDA.png", width=250)

st.title("Un collectif engagé pour l’avenir")
st.caption("Explorez les liens entre thématiques, impacts et grandes variables")

with st.sidebar:
    st.markdown("### Le Collectif")
    st.write("""
    En Grand Est, Des Hommes et Des Arbres identifie, encourage et fait émerger des projets innovants avec et pour les arbres, au service des territoires.
    """)
    st.divider()
    st.success("🌱 51 projets labellisés dans le Grand Est")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages précédents
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Gestion de la saisie utilisateur
if prompt := st.chat_input("De quoi dépend la production de bois par les forêts ?"):
    
    # 1. Afficher le message de l'utilisateur tout de suite
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Appeler le backend pour avoir la réponse
    with st.chat_message("assistant"):
        with st.spinner("L'IA analyse le graphe..."):
            try:
                # Préparation des données comme attendu par ta classe ChatRequest dans main.py
                payload = {"question": prompt, "thread_id": "streamlit_session"}
                
                # Envoi de la requête POST
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    ai_response = data.get("response", "Erreur: Réponse vide.")
                    st.markdown(ai_response)
                    
                    # Sauvegarder la réponse dans l'historique
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                else:
                    st.error(f"Erreur API ({response.status_code}) : {response.text}")
            
            except requests.exceptions.ConnectionError:
                st.error("Impossible de se connecter au backend. Vérifie qu'il est bien lancé sur le port 8000.")
            except Exception as e:
                st.error(f"Une erreur est survenue : {str(e)}")