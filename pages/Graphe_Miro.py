import streamlit as st

st.set_page_config(
    page_title="Graphe Miro - DHDA",
    page_icon="📊",
    layout="wide"
)

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

# Sidebar avec le même contenu que la page principale
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
    
    st.success("🌱 51 projets labellisés")
    
    st.divider()
    st.subheader("🗺️ Navigation")
    if st.button("⬅️ Retour à l'accueil"):
        st.switch_page("ui.py")

st.image("./logo_DHDA.png", width=250)

st.title("📊 Graphe des Relations")
st.write("### Visualisation interactive des liens entre thématiques, impacts et grandes variables")

st.markdown("---")

# Embed Miro
miro_embed = """
<iframe 
    width="100%" 
    height="600" 
    src="https://miro.com/app/live-embed/uXjVGIhZBpg=/?embedMode=view_only_without_ui&moveToViewport=-19570,-24996,11152,5170&embedId=979634646839" 
    frameborder="0" 
    scrolling="no" 
    allow="fullscreen; clipboard-read; clipboard-write" 
    allowfullscreen>
</iframe>
"""

st.components.v1.html(miro_embed, height=620)

st.markdown("---")
st.caption("🌳 Des Hommes et Des Arbres - Graphe de connaissances interactif")
