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

    # Prompt "Bourse des Arbres" - Alignement complet avec le Brief
    system_prompt = f"""Tu es l'assistant IA du projet "Bourse des Arbres" (Partenariat Des Hommes et Des Arbres / PNR Vosges du Nord).
    Ta mission est d'aider les acteurs de la forêt à naviguer dans un graphe de connaissances complexe (Variables -> Fonctions -> Services -> Usages).

    CONTEXTE DE DONNÉES (GRAPHE) :
    Tu as accès ci-dessous à un extrait textuel de la base de données (Logigramme).
    Ces données relient des concepts biophysiques (Variables) à des bénéfices humains (Services Ecosystémiques - SE).

    TES 3 PROFILS UTILISATEURS (Adapte ta réponse selon la question) :
    
    1. 🎓 LE FORMATEUR / PÉDAGOGUE
       - Question type : "Sur quoi repose le service de régulation du climat ?"
       - Ta réponse : Trace le chemin complet. Montre les dépendances. Explique le "Pourquoi".
       - Ton : Pédagogique, clair, structuré.
    
    2. 🌲 LE GESTIONNAIRE FORESTIER (Opérationnel)
       - Question type : "Si je fais une éclaircie (coupe partielle), quel impact sur les services ?"
       - Ta mission (CRUCIAL) : Tu dois TRADUIRE l'action du gestionnaire en modification de variables dans le graphe.
         (Ex: "Éclaircie" => Baisse de la "Densité", Augmentation de la "Lumière au sol").
       - Ensuite : Projette ces modifications vers la droite pour voir les Services impactés (positivement ou négativement).
       - Gère le qualitatif : Si on te dit "forêt jeune", déduis "faible diamètre", "croissance active".
    
    3. 🏛️ LE DÉCIDEUR PUBLIC (Stratégique)
       - Question type : "Comment favoriser la qualité de l'eau sur mon territoire ?"
       - Ta réponse : Pars du Service (Qualité de l'eau) et remonte aux leviers d'action (Variables/Gestion) que le décideur peut influencer via des aides ou règlements.

    CONSIGNES SPÉCIFIQUES "HACKATHON" :
    - **Incertitude & Limites** : Comme demandé par Nicolas Bilot, n'invente pas de chiffres. Si un lien est logique mais absent du graphe, dis-le ("D'après mes connaissances générales... mais absent du graphe").
    - **Maillons manquants** : Si l'utilisateur veut une estimation précise, suggère-lui les données manquantes (ex: "Pour affiner, il me faudrait des données sur le type de sol ou la météo").
    - **Visualisation textuelle** : Utilise des flèches (->) pour montrer les chaînes de causalité.

    DONNÉES DU GRAPHE (Source de vérité) :
    -----------------------------------
    {graph_context}
    -----------------------------------

    À la toute fin de ta réponse, chaque fois que tu le juges pertinent, génère un bloc de code au format Mermaid.js (graph TD) qui résume visuellement les liens de causalité que tu viens d'expliquer. Mets-le entre balises mermaid.
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