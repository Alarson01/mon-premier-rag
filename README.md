# Mon Premier RAG

Mini-TP réalisé dans le cadre du Master 2 MD5.

## Technologies

- ChromaDB
- Sentence Transformers
- Groq
- Python

## Modèle d'embedding

distiluse-base-multilingual-cased-v2

## Modèle LLM

llama-3.3-70b-versatile

## Architecture

Question utilisateur
↓
Agent modérateur
↓
VectorDB (ChromaDB)
↓
RAG
↓
Réponse

## Structure

- config.py : configuration
- vectordb.py : base vectorielle
- moderator.py : détection des injections
- rag.py : pipeline RAG
- main.py : point d'entrée
- prompts/moderator_system.txt : prompt du modérateur
- prompts/rag_system.txt : prompt du RAG
