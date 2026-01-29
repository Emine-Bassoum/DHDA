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

--------------------------------------

## 🐳 Déploiement avec Docker

### Build automatique via GitHub Actions
Ce projet dispose d'un workflow GitHub Actions qui compile automatiquement le projet et crée une image Docker. L'image est publiée sur GitHub Container Registry (GHCR).

Le workflow se déclenche :
- À chaque push sur les branches `main` ou `master`
- À chaque pull request vers `main` ou `master`
- Manuellement via l'onglet Actions

### Utiliser l'image Docker

Vous pouvez télécharger et utiliser l'image Docker publiée :

```bash
docker pull ghcr.io/emine-bassoum/dhda:latest
docker run -p 8000:8000 -p 8501:8501 --env-file .env ghcr.io/emine-bassoum/dhda:latest
```

### Build local avec Docker

Pour construire l'image localement :

```bash
docker build -t dhda:latest .
docker run -p 8000:8000 -p 8501:8501 --env-file .env dhda:latest
```

L'application sera accessible sur :
- Backend (API FastAPI) : http://localhost:8000
- Frontend (Streamlit) : http://localhost:8501
