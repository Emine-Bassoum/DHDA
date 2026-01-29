import streamlit as st
import requests  # N'oublie pas d'installer requests (pip install requests)
import re
from streamlit_mermaid import st_mermaid

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

# --- FONCTION UTILITAIRE POUR EXTRAIRE LE MERMAID ---
def split_response(text):
    """
    Sépare le texte explicatif du code Mermaid s'il existe.
    Renvoie un tuple (texte_propre, code_mermaid_ou_none)
    """
    # Regex pour capturer le contenu entre ```mermaid et ```
    pattern = r"```mermaid\s+(.*?)\s+```"
    match = re.search(pattern, text, re.DOTALL)
    
    if match:
        mermaid_code = match.group(1)
        # On enlève le bloc de code du texte principal pour ne pas l'afficher en double
        text_without_code = re.sub(pattern, "", text, flags=re.DOTALL).strip()
        return text_without_code, mermaid_code
    return text, None

# Affichage des messages précédents
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
                    raw_response = data.get("response", "Erreur: Réponse vide.")
                    
                    # 1. On sépare le texte du graphique
                    text_content, mermaid_code = split_response(raw_response)
                    
                    # 2. On affiche le texte
                    st.markdown(text_content)
                    
                    # 3. On affiche le diagramme si présent
                    if mermaid_code:
                        st_mermaid(mermaid_code, height=350)
                    
                    # 4. On sauvegarde TOUT le contenu brut dans l'historique
                    # (Comme ça au rechargement de la page, la boucle ci-dessus refera le parsing)
                    st.session_state.messages.append({"role": "assistant", "content": raw_response})
                
                else:
                    st.error(f"Erreur API ({response.status_code})")
            
            except Exception as e:
                st.error(f"Erreur : {str(e)}")