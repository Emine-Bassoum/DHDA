import streamlit as st

st.set_page_config(
    page_title="Des Hommes et Des Arbres",
    page_icon="🌳",
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
        
        h2 {
            color: #1a1a1a !important;
            font-weight: 600 !important;
        }
        
        h3 {
            color: var(--dhda-magenta) !important;
            font-weight: 500 !important;
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
        
        .stat-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            border-left: 4px solid var(--dhda-magenta);
            margin: 10px 0;
        }
        
        .stat-number {
            font-size: 2.5rem;
            font-weight: 700;
            color: var(--dhda-magenta);
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #666;
            margin-top: 5px;
        }
        
        .quote-box {
            background-color: #f8f9fa;
            border-left: 4px solid var(--dhda-magenta);
            padding: 20px;
            margin: 20px 0;
            font-style: italic;
            border-radius: 0 10px 10px 0;
        }
        
        .highlight-box {
            background: linear-gradient(135deg, #d100ff15 0%, #d100ff05 100%);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
        }
        
        .tree-fact {
            background-color: #e8f5e9;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            border-left: 4px solid #4caf50;
        }
    </style>
    """, unsafe_allow_html=True)

apply_dhda_design()

# Sidebar
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    if st.button("💬 Assistant IA"):
        st.switch_page("pages/Assistant_IA.py")
    if st.button("📊 Graphe Miro"):
        st.switch_page("pages/Graphe_Miro.py")
    
    st.divider()
    
    st.markdown("### 📞 Contact")
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/contact/" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block;
                padding: 6px 15px;
                border-radius: 20px;
                border: 1.5px solid #d100ff;
                color: #d100ff;
                font-size: 0.85rem;
                font-weight: 500;
                background-color: transparent;
                ">
                ✉️ Nous contacter
            </div>
        </a>
    """, unsafe_allow_html=True)
    
    st.markdown("")
    
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/nous-rejoindre/" target="_blank" style="text-decoration: none;">
            <div style="
                display: inline-block;
                padding: 6px 15px;
                border-radius: 20px;
                border: 1.5px solid #d100ff;
                color: #d100ff;
                font-size: 0.85rem;
                font-weight: 500;
                background-color: transparent;
                ">
                🤝 Nous rejoindre
            </div>
        </a>
    """, unsafe_allow_html=True)

# Header
st.image("./logo_DHDA.png", width=300)

st.title("🌳 Des Hommes et Des Arbres")
st.markdown("### *Un collectif hybride et audacieux au service des territoires*")

st.markdown("---")

# Section présentation
st.markdown("""
<div class="highlight-box">
<h2>🌿 Qui sommes-nous ?</h2>
<p style="font-size: 1.1rem; line-height: 1.8;">
<strong>Des Hommes et Des Arbres</strong> rassemble plus de <strong>120 membres</strong> : entrepreneurs, forestiers, artistes, 
agriculteurs, chercheurs, élus, industriels, naturalistes, citoyens... Tous unis par une conviction forte : 
<em>l'arbre est un levier puissant pour faire évoluer nos territoires vers plus de résilience, de bien-être et d'innovation.</em>
</p>
<p style="font-size: 1.1rem; line-height: 1.8;">
En croisant les savoirs, les expériences et les regards, le collectif imagine et accompagne des <strong>solutions concrètes</strong> 
pour la transition écologique, la vitalité économique et la qualité de vie.
</p>
</div>
""", unsafe_allow_html=True)

# Stats DHDA
st.markdown("## 📊 Le Collectif en Chiffres")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">124</div>
        <div class="stat-label">Membres du collectif</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">51</div>
        <div class="stat-label">Projets labellisés</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">576h</div>
        <div class="stat-label">Mobilisées pour l'analyse</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">225</div>
        <div class="stat-label">Synergies ouvertes</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Une communauté en action
st.markdown("## 🎯 Une Communauté en Action")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("""
    Le collectif agit pour **faciliter et accélérer le développement de projets à impact**. 
    À travers son label, il se mobilise dès qu'un projet montre un potentiel de transformation pour le territoire.
    
    **Concrètement, les membres du collectif :**
    - 🔍 Analysent les projets candidats et formulent des préconisations
    - 💡 Font émerger de nouvelles idées ou problématiques à partir du terrain
    - 🎓 Partagent leurs expertises, leurs savoirs et leurs retours d'expérience
    - 📢 Font rayonner les projets labellisés et les initiatives inspirantes
    - 🤝 Détectent les besoins de terrain et conjuguent leurs intelligences pour y répondre
    """)

with col_right:
    st.markdown("""
    <div class="quote-box">
    <p>"Être lauréat de l'appel à projet « Territoire d'innovation » avec Des Hommes et Des Arbres témoigne 
    du dynamisme de notre territoire."</p>
    <p style="text-align: right; font-weight: bold; font-style: normal;">— Mathieu Klein</p>
    <p style="text-align: right; font-size: 0.85rem; font-style: normal;">Président de la Métropole du Grand Nancy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Section Arbres - Statistiques mondiales
st.markdown("## 🌍 Les Arbres dans le Monde : Chiffres Clés")

st.markdown("""
<div class="highlight-box">
<p style="font-size: 1.05rem; line-height: 1.7;">
Les arbres sont essentiels à la vie sur Terre. Ils produisent l'oxygène que nous respirons, 
stockent le carbone, régulent le climat, abritent la biodiversité et fournissent des ressources vitales à l'humanité.
</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="tree-fact">
        <h4>🌳 3 000 milliards</h4>
        <p>Nombre d'arbres sur Terre (estimation)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tree-fact">
        <h4>🪓 15 milliards</h4>
        <p>Arbres abattus chaque année</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tree-fact">
        <h4>🌲 31%</h4>
        <p>Surface terrestre couverte par les forêts</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tree-fact">
        <h4>🦎 80%</h4>
        <p>De la biodiversité terrestre vit en forêt</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tree-fact">
        <h4>💨 22 kg</h4>
        <p>CO₂ absorbé par arbre/an en moyenne</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tree-fact">
        <h4>🫁 118 kg</h4>
        <p>O₂ produit par arbre mature/an</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Section France
st.markdown("## 🇫🇷 Les Forêts en France")

col_fr1, col_fr2 = st.columns(2)

with col_fr1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">17 millions</div>
        <div class="stat-label">Hectares de forêt en France métropolitaine</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - 🌲 **31%** du territoire métropolitain est couvert de forêts
    - 📈 La surface forestière a **doublé** depuis 1850
    - 🌳 **190 espèces** d'arbres différentes
    - 🏭 **440 000 emplois** dans la filière forêt-bois
    """)

with col_fr2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2,8 milliards</div>
        <div class="stat-label">Arbres en France métropolitaine</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - 🏔️ **75%** des forêts sont privées
    - 🌡️ Les forêts absorbent **~15%** des émissions de CO₂ françaises
    - 🌿 **136 espèces d'arbres** dans le Grand Est
    - 🪵 **3ème ressource** naturelle de la France après l'eau et le sol
    """)

st.markdown("---")

# Section Grand Est
st.markdown("## 🗺️ Le Grand Est : Un Territoire Forestier d'Exception")

st.markdown("""
<div class="highlight-box">
<p style="font-size: 1.05rem; line-height: 1.7;">
Le <strong>Grand Est</strong> est un territoire où les arbres occupent une place essentielle dans l'économie, la culture et les paysages. 
Cette relation privilégiée avec le végétal a inspiré la création de <strong>Des Hommes et Des Arbres</strong>.
</p>
</div>
""", unsafe_allow_html=True)

col_ge1, col_ge2, col_ge3 = st.columns(3)

with col_ge1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">1,9 M ha</div>
        <div class="stat-label">Surface forestière du Grand Est</div>
    </div>
    """, unsafe_allow_html=True)

with col_ge2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">34%</div>
        <div class="stat-label">Taux de boisement régional</div>
    </div>
    """, unsafe_allow_html=True)

with col_ge3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">1ère</div>
        <div class="stat-label">Région forestière de France</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Section services écosystémiques
st.markdown("## 🌱 Les Services Rendus par les Arbres")

tab1, tab2, tab3, tab4 = st.tabs(["🌡️ Climat", "💧 Eau", "🦋 Biodiversité", "👥 Société"])

with tab1:
    st.markdown("""
    ### Régulation climatique
    - **Absorption du CO₂** : Un hectare de forêt absorbe 2 à 5 tonnes de CO₂/an
    - **Effet de refroidissement** : Un arbre mature équivaut à 10 climatiseurs
    - **Réduction des îlots de chaleur** : Jusqu'à -8°C en zone urbaine arborée
    - **Protection contre le vent** : Réduction de 50% de la vitesse du vent
    """)

with tab2:
    st.markdown("""
    ### Cycle de l'eau
    - **Filtration naturelle** : Les forêts purifient l'eau de pluie
    - **Régulation des crues** : Absorption jusqu'à 400L d'eau/jour/arbre
    - **Prévention de l'érosion** : Les racines stabilisent les sols
    - **Recharge des nappes** : Infiltration favorisée par le couvert forestier
    """)

with tab3:
    st.markdown("""
    ### Habitat et biodiversité
    - **Refuge** : 80% des espèces terrestres vivent en forêt
    - **Corridors écologiques** : Connexion entre les habitats naturels
    - **Pollinisation** : Support essentiel pour les pollinisateurs
    - **Chaîne alimentaire** : Base de nombreux écosystèmes
    """)

with tab4:
    st.markdown("""
    ### Bienfaits pour l'humanité
    - **Santé mentale** : Réduction du stress et de l'anxiété
    - **Économie** : Filière bois, tourisme, agroforesterie
    - **Cadre de vie** : Amélioration du bien-être quotidien
    - **Patrimoine culturel** : Arbres remarquables, forêts historiques
    """)

st.markdown("---")

# Call to action
st.markdown("## 🤝 Rejoignez le Mouvement")

st.markdown("""
<div class="highlight-box" style="text-align: center;">
<h3>Vous êtes convaincu que les meilleures solutions sont collectives ?</h3>
<p style="font-size: 1.1rem;">
Faire partie de Des Hommes et Des Arbres, c'est :
</p>
<ul style="text-align: left; max-width: 600px; margin: 0 auto;">
<li>✅ Intégrer une communauté engagée, pluridisciplinaire et ouverte</li>
<li>✅ Participer à une dynamique collective qui fait émerger des solutions concrètes</li>
<li>✅ Bénéficier d'un environnement fertile pour développer, tester et valoriser ses projets</li>
<li>✅ Partager ses savoir-faire et apprendre des autres</li>
<li>✅ Contribuer à une transition écologique portée par l'arbre</li>
</ul>
</div>
""", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn1:
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/nous-rejoindre/" target="_blank" style="text-decoration: none;">
            <div style="
                text-align: center;
                padding: 12px 25px;
                border-radius: 25px;
                background-color: #d100ff;
                color: white;
                font-size: 1rem;
                font-weight: 600;
                ">
                🌳 Rejoindre le collectif
            </div>
        </a>
    """, unsafe_allow_html=True)

with col_btn2:
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/projets/" target="_blank" style="text-decoration: none;">
            <div style="
                text-align: center;
                padding: 12px 25px;
                border-radius: 25px;
                border: 2px solid #d100ff;
                color: #d100ff;
                font-size: 1rem;
                font-weight: 600;
                ">
                🔍 Découvrir les projets
            </div>
        </a>
    """, unsafe_allow_html=True)

with col_btn3:
    st.markdown("""
        <a href="https://www.deshommesetdesarbres.org/le-label/" target="_blank" style="text-decoration: none;">
            <div style="
                text-align: center;
                padding: 12px 25px;
                border-radius: 25px;
                border: 2px solid #d100ff;
                color: #d100ff;
                font-size: 1rem;
                font-weight: 600;
                ">
                🏷️ En savoir plus sur le label
            </div>
        </a>
    """, unsafe_allow_html=True)

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <p>© Des Hommes et Des Arbres - Grand Est, France</p>
    <p style="font-size: 0.85rem;">
        <a href="https://www.deshommesetdesarbres.org/mentions-legales/" target="_blank" style="color: #888;">Mentions légales</a> | 
        <a href="https://www.deshommesetdesarbres.org/" target="_blank" style="color: #888;">Site officiel</a>
    </p>
</div>
""", unsafe_allow_html=True)
