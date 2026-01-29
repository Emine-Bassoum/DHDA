import os

def load_graph_context(file_path: str) -> str:
    """
    Lit le fichier .txt contenant les données du graphe.
    """
    if not os.path.exists(file_path):
        return "Erreur : Le fichier de données du graphe est introuvable."
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except Exception as e:
        return f"Erreur lors de la lecture du fichier : {e}"