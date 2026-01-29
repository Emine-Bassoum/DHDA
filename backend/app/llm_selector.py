import os
from dotenv import load_dotenv

# Import des différentes classes de modèles
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

def get_llm():
    """
    Renvoie l'objet LLM configuré en fonction de la variable d'env LLM_PROVIDER.
    Permet de configurer le nom du modèle via les variables d'env spécifiques.
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()
    print(f"🔄 Initialisation du provider : {provider.upper()}")

    if provider == "openai":
        # Par défaut gpt-4o si OPENAI_MODEL n'est pas défini
        model_name = os.getenv("OPENAI_MODEL", "gpt-4o")
        print(f"   ➔ Modèle : {model_name}")
        return ChatOpenAI(
            model=model_name,
            temperature=0
        )
    
    elif provider == "google":
        # Par défaut gemini-1.5-flash
        model_name = os.getenv("GOOGLE_MODEL", "gemini-1.5-flash")
        print(f"   ➔ Modèle : {model_name}")
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0
        )
    
    elif provider == "mistral":
        # Par défaut mistral-large-latest
        model_name = os.getenv("MISTRAL_MODEL", "mistral-large-latest")
        print(f"   ➔ Modèle : {model_name}")
        return ChatMistralAI(
            model=model_name,
            temperature=0
        )

    elif provider == "huggingface":
        # Par défaut Meta-Llama-3-8B-Instruct
        repo_id = os.getenv("HUGGINGFACE_REPO_ID", "meta-llama/Meta-Llama-3-8B-Instruct")
        print(f"   ➔ Repo ID : {repo_id}")
        llm_base = HuggingFaceEndpoint(
            repo_id=repo_id,
            task="text-generation",
            temperature=0.1
        )
        return ChatHuggingFace(llm=llm_base)

    else:
        raise ValueError(f"Le provider '{provider}' n'est pas reconnu. Vérifie ton fichier .env")