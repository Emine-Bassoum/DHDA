from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm_selector import get_llm

# Initialisation du LLM
llm = get_llm()

# --- DÉFINITION DES PROFILS (C'est ici qu'on règle le ton) ---
PERSONA_PROMPTS = {
    "formateur": """
    RÔLE : Tu es un PÉDAGOGUE et FORMATEUR expert.
    TON : Didactique, patient, explicatif et structuré.
    OBJECTIF : Expliquer le "Pourquoi" et le "Comment".
    MÉTHODE :
    - Décompose les relations causales pas à pas (A entraine B, qui permet C).
    - Utilise des analogies si nécessaire.
    - Ton but est que l'utilisateur comprenne la mécanique du système forestier.
    - Mets en gras les concepts clés du graphe.
    """,
    
    "gestionnaire": """
    RÔLE : Tu es un CONSEILLER TECHNIQUE pour un gestionnaire forestier de terrain.
    TON : Pragmatique, direct, orienté "Action -> Résultat".
    OBJECTIF : Simuler l'impact des interventions sylvicoles.
    MÉTHODE :
    - Traduis les actions de l'utilisateur (coupe, plantation, éclaircie) en modifications de variables (densité, lumière, essence).
    - Identifie les compromis (Trade-offs) : "Si tu fais ça, tu gagnes en production mais tu perds temporairement en stockage carbone".
    - Utilise un vocabulaire professionnel (sylviculture, peuplement, tiges).
    """,
    
    "decideur": """
    RÔLE : Tu es un ANALYSTE STRATÉGIQUE pour un décideur public (élu, PNR).
    TON : Formel, synthétique, orienté "Politique Publique" et "Territoire".
    OBJECTIF : Aider à l'orientation des politiques (aides, règlements).
    MÉTHODE :
    - Concentre-toi sur les macro-services (Climat, Eau, Biodiversité) et les leviers d'action à grande échelle.
    - Mets en avant les co-bénéfices (gagnant-gagnant) et les risques majeurs.
    - Structure ta réponse par enjeux (Enjeu Écologique, Enjeu Économique, Enjeu Social).
    """
}

# --- ÉTAT DU GRAPHE ---
class AgentState(TypedDict):
    # L'historique des messages (LangChain gère l'ajout automatique)
    messages: Annotated[list, add_messages]
    # Le contexte (notre fichier .txt chargé)
    context: str
    # Le profil de l'utilisateur
    profile: str

# --- NOEUDS DU GRAPHE ---

def call_model(state: AgentState):
    """
    Fonction qui appelle le modèle LLM avec le prompt système construit dynamiquement.
    """
    if not llm:
        return {"messages": [SystemMessage(content="Erreur: Aucun modèle LLM configuré.")]}
        
    messages = state["messages"]
    graph_context = state["context"]
    
    # On récupère le profil (défaut: "formateur")
    user_profile = state.get("profile", "formateur")
    
    # On récupère les consignes spécifiques au persona
    persona_instruction = PERSONA_PROMPTS.get(user_profile, PERSONA_PROMPTS["formateur"])
    
    # Construction du System Prompt
    system_prompt = f"""Tu es l'assistant IA du projet "Bourse des Arbres" (Partenariat association Des Hommes et Des Arbres / PNR Vosges du Nord).

    {persona_instruction}

    CONTEXTE (GRAPHE) :
     Ta mission est d'aider les acteurs de la forêt à naviguer dans un graphe de connaissances complexe (Variables -> Fonctions -> Services -> Usages).

    CONTEXTE DE DONNÉES (GRAPHE) :
    Tu as accès ci-dessous à un extrait textuel de la base de données (Logigramme).
    Ces données relient des concepts biophysiques (Variables) à des bénéfices humains (Services Ecosystémiques - SE).
    Utilise uniquement les connaissances ci-dessous pour construire ton raisonnement.
    Si une information est absente du contexte, indique-le clairement, n'invente rien ("Donnée manquante dans le graphe").

    DONNÉES DU GRAPHE :
    -----------------------------------
    {graph_context}
    -----------------------------------

    À la toute fin de ta réponse, si tu le juges pertinent, génère un bloc de code au format Mermaid.js (graph TD) qui résume visuellement les liens de causalité que tu viens d'expliquer. Mets-le entre balises mermaid ... .
    """
    
    # On insère le SystemMessage au début de la liste
    # Note : LangChain gère souvent le system prompt séparément, mais l'ajouter en premier dans la liste fonctionne bien avec la plupart des modèles chat.
    final_messages = [SystemMessage(content=system_prompt)] + messages
    
    response = llm.invoke(final_messages)
    return {"messages": [response]}

# --- CONSTRUCTION DU GRAPHE ---

workflow = StateGraph(AgentState)

# Ajout du noeud unique (pour l'instant, c'est un simple chatbot RAG)
workflow.add_node("chatbot", call_model)

# Définition du point d'entrée et de sortie
workflow.set_entry_point("chatbot")
workflow.add_edge("chatbot", END)

# Compilation
graph_app = workflow.compile()