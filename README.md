## 🛠️ Installation & Configuration

### 1. Installer les dépendances
Installez les librairies requises (FastAPI, LangChain, etc.) via le fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

### 2. Configurer le .env
Créez un fichier .env à la racine du projet (ou copiez un .env.example) et configurez-le selon le modèle que vous souhaitez utiliser.

Voici les variables disponibles :
```
# CHOIX DU MODÈLE : "openai", "google", "mistral", ou "huggingface"
LLM_PROVIDER=openai

# --- CLÉS API (Remplir celles dont on a besoin) ---
OPENAI_API_KEY=sk-proj-xxxxxx
GOOGLE_API_KEY=AIzaSyxxxxxx
MISTRAL_API_KEY=xxxxxxxx
HUGGINGFACEHUB_API_TOKEN=hf_xxxxxx

# Configuration spécifique des modèles (optionnel, prend la défaut sinon)
OPENAI_MODEL=gpt-3.5-turbo
GOOGLE_MODEL=gemini-1.5-pro
MISTRAL_MODEL=mistral-small-latest
HUGGINGFACE_REPO_ID=mistralai/Mistral-7B-Instruct-v0.2
```

--------------------------------------

## Démarrage du Backend

Pour lancer le serveur API avec le rechargement automatique (hot-reload), placez-vous dans le dossier contenant le module app (ex: backend) et exécutez :

```
uvicorn app.main:app --reload
```

L'API sera accessible sur http://127.0.0.1:8000.
