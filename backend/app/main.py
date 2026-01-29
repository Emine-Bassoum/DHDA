from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

from app.utils import load_graph_context
from app.graph import graph_app

# Chargement des variables d'environnement
load_dotenv()

app = FastAPI(title="Hackathon Arbres API")

# -- Chargement des données au démarrage --
# On construit le chemin vers le fichier data/graph_data.txt
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "graph_data.txt")

# Variable globale pour stocker le texte du graphe
GRAPH_CONTENT = ""

@app.on_event("startup")
async def startup_event():
    global GRAPH_CONTENT
    print(f"Chargement des données depuis {DATA_FILE}...")
    GRAPH_CONTENT = load_graph_context(DATA_FILE)
    if not GRAPH_CONTENT or "Erreur" in GRAPH_CONTENT[:20]:
        print("ATTENTION: Le fichier de données semble vide ou introuvable.")
    else:
        print("Données du graphe chargées avec succès !")

# -- Modèles de données pour l'API --
class ChatRequest(BaseModel):
    question: str
    # Optionnel : thread_id pour gérer plusieurs conversations si besoin
    thread_id: str = "default_thread"

class ChatResponse(BaseModel):
    response: str

# -- Endpoint du Chatbot --
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    if not GRAPH_CONTENT:
        raise HTTPException(status_code=500, detail="Les données du graphe ne sont pas chargées.")

    # On prépare l'input pour LangGraph
    # On passe la question de l'utilisateur ET le contexte chargé
    inputs = {
        "messages": [("user", request.question)],
        "context": GRAPH_CONTENT
    }

    # Configuration pour gérer la mémoire (optionnel pour le hackathon mais bonne pratique)
    config = {"configurable": {"thread_id": request.thread_id}}

    try:
        # On lance le graphe
        output = graph_app.invoke(inputs, config=config)
        
        # On récupère le dernier message
        last_message = output["messages"][-1]
        raw_content = last_message.content

        # --- CORRECTION DU BUG ---
        # Si le contenu est une liste (ex: [{'type': 'text', 'text': '...'}]), on extrait le texte.
        if isinstance(raw_content, list):
            bot_response = "".join(
                [block.get("text", "") for block in raw_content if isinstance(block, dict) and "text" in block]
            )
        else:
            # Sinon c'est déjà du texte
            bot_response = str(raw_content)
        # -------------------------

        return ChatResponse(response=bot_response)

    except Exception as e:
        print(f"Erreur backend: {e}")
        # On renvoie l'erreur en string pour débugger plus facilement côté frontend
        raise HTTPException(status_code=500, detail=str(e))


# Pour lancer en local (si on exécute ce fichier directement)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)