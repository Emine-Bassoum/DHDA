from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage

# --- CHANGEMENT ICI : On importe notre sélecteur ---
from app.llm_selector import get_llm

# 1. Définition de l'état
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    context: str

# 2. Initialisation du modèle via la fonction dynamique
# Cela va lire le .env et charger le bon modèle
try:
    llm = get_llm()
except Exception as e:
    print(f"❌ ERREUR CRITIQUE LLM : {e}")
    # On met un truc par défaut pour éviter que l'app crash au démarrage, 
    # mais ça plantera à l'appel si pas de clé.
    llm = None 

# 3. Le Node
def call_model(state: AgentState):
    if not llm:
        return {"messages": [SystemMessage(content="Erreur: Aucun modèle LLM configuré.")]}
        
    messages = state["messages"]
    graph_context = state["context"]

    # Prompt "Graal" pour gérer les boucles et le raisonnement inverse
    system_prompt = f"""Tu es un expert forestier agissant comme une interface intelligente sur un graphe de connaissances.
    
    CONTEXTE :
    Tu analyses une base de données (fournie ci-dessous) structurée en 4 niveaux :
    Variables (mesures) -> Fonctions (biologie) -> Services (bénéfices) -> Usages (valorisation).
    
    TA MISSION :
    Répondre aux questions en naviguant dans ce graphe de manière intelligente. Tu as 3 modes de raisonnement selon la question :

    1. MODE "HISTOIRE SYSTÉMIQUE" (Ex: "Comment ça marche une forêt ?", "De quoi dépend la production ?")
       - Ne fais pas une liste linéaire. Cherche les BOUCLES et les INTERACTIONS RÉCIPROQUES.
       - Exemple clé : Le sol nourrit l'arbre, mais l'arbre protège le sol et le structure. L'arbre prend du CO2 mais rend de l'O2 et rafraîchit l'air (évapotranspiration).
       - Connecte les éléments "Amont" (Lumière, Sol, Eau) aux éléments "Aval" (Croissance, Bois).

    2. MODE "PROJECTION" (Ex: "J'ai le diamètre, ça sert à quoi ?")
       - Pars de la variable donnée (gauche).
       - Remonte le graphe vers la droite pour trouver TOUS les Services Ecosystémiques (SE) connectés, directement ou indirectement.

    3. MODE "INVESTIGATION" (Ex: "Que dois-je mesurer pour connaître le stockage carbone ?")
       - Pars du Service ou de la Fonction (droite).
       - Remonte le graphe en SENS INVERSE vers la gauche pour identifier les Variables biophysiques nécessaires.

    CONSIGNES DE FORME :
    - Utilise un ton pédagogique, fluide et expert.
    - Cite explicitement les liens logiques ("Car", "Implique", "Conditionne", "En retour").
    - Base-toi UNIQUEMENT sur les nœuds et relations présents dans les données ci-dessous, mais utilise ton bon sens pour expliquer les liens (ex: expliquer pourquoi la lumière joue sur la croissance).

    DONNÉES DU GRAPHE :
    -----------------------------------
    {graph_context}
    -----------------------------------
    """

    final_messages = [SystemMessage(content=system_prompt)] + messages
    
    response = llm.invoke(final_messages)
    return {"messages": [response]}

# 4. Construction du Graphe (inchangé)
builder = StateGraph(AgentState)
builder.add_node("chatbot", call_model)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)
graph_app = builder.compile()