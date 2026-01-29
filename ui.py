import streamlit as st
import requests
import re
from streamlit_mermaid import st_mermaid

# Configuration de l'URL du backend
API_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="Des Hommes et Des Arbres",
    page_icon="https://deshommesetdesarbres.org/wp-content/uploads/2021/03/cropped-favicon-dhda-32x32.png", # Teste avec cet emoji d'abord
    layout="wide"
)

# --- FONCTION UTILITAIRE POUR EXTRAIRE LE MERMAID ---
def split_response(text):
    """
    Sépare le texte explicatif du code Mermaid s'il existe.
    Renvoie un tuple (texte_propre, code_mermaid_ou_none)
    """
    pattern = r"```mermaid\s+(.*?)\s+```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        mermaid_code = match.group(1)
        text_without_code = re.sub(pattern, "", text, flags=re.DOTALL).strip()
        return text_without_code, mermaid_code
    return text, None

def apply_dhda_design():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        .stAppDeployButton { display: none !important; }
        footer { visibility: hidden; }
        
        /* Masquer la navigation des pages */
        [data-testid="stSidebarNav"] { display: none !important; }
        
        header {
            background-color: rgba(0,0,0,0) !important;
            border-bottom: none !important;
        }

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

st.title("Posez-moi une question...")
st.write("### Explorez les liens entre thématiques, impacts et grandes variables")

# --- SIDEBAR AVEC LE SÉLECTEUR DE PROFIL ---
with st.sidebar:
    st.markdown("### Le Collectif")
    st.write("""
    En Grand Est, Des Hommes et Des Arbres identifie, encourage et fait émerger des projets innovants avec et pour les arbres, au service des territoires.
    """)
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/projets/" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block;
                padding: 6px 15px;
                border-radius: 20px;
                border: 1.5px solid #d100ff;
                color: #d100ff;
                font-size: 0.85rem;
                font-weight: 500;
                background-color: transparent;
                transition: 0.3s;
                ">
                🔍 Découvrir nos projets
            </div>
        </a>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.subheader("👤 Votre Profil")
    # Le sélecteur de persona
    selected_role = st.selectbox(
        "Qui êtes vous ?",
        ("Pédagogue / Grand Public", "Gestionnaire Forestier", "Décideur Public"),
        index=0
    )
    
    # Mapping vers les clés du backend
    role_mapping = {
        "Pédagogue / Grand Public": "formateur",
        "Gestionnaire Forestier": "gestionnaire",
        "Décideur Public": "decideur"
    }
    current_profile = role_mapping[selected_role]
    
    st.info(f"Mode activé : **{current_profile.upper()}**")
    st.divider()
    st.success("🌱 51 projets labellisés")
    
    st.divider()
    st.subheader("📊 Visualisation")
    if st.button("🗺️ Voir le Graphe Miro"):
        st.switch_page("pages/Graphe_Miro.py")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Si c'est un message assistant, on vérifie s'il y a du mermaid
        if message["role"] == "assistant":
            text, mermaid = split_response(message["content"])
            st.markdown(text)
            if mermaid:
                st_mermaid(mermaid, height=300) # Tu peux ajuster la hauteur
        else:
            st.markdown(message["content"])

if prompt := st.chat_input("De quoi dépend la production de bois par les forêts ?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner(f"L'IA analyse ({current_profile})..."):
            try:
                # Ajout du profil dans la requête
                payload = {
                    "question": prompt, 
                    "thread_id": "streamlit_session",
                    "profile": current_profile
                }
                
                response = requests.post(API_URL, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    raw_response = data.get("response", "Erreur: Réponse vide.")
                    
                    # 1. On sépare le texte du graphique
                    text_content, mermaid_code = split_response(raw_response)
                    
                    # 2. On affiche le texte
                    st.markdown(text_content)
                    
                    # 3. On affiche le diagramme si présent
                    if mermaid_code:
                        st_mermaid(mermaid_code, height=350)
                    
                    st.session_state.messages.append({"role": "assistant", "content": raw_response})
                else:
                    st.error(f"Erreur API ({response.status_code}) : {response.text}")
            
            except requests.exceptions.ConnectionError:
                st.error("Impossible de se connecter au backend sur le port 8000.")
            except Exception as e:
                st.error(f"Erreur : {str(e)}")