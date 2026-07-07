from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Modèle d'embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

# Documents de démonstration
documents = [
    "Paris est la capitale de la France.",
    "Lyon est connue pour sa gastronomie.",
    "Marseille est située sur la côte méditerranéenne.",
    "Groupama est une compagnie d'assurance française."
]

# Génération des embeddings
embeddings = model.encode(documents)

# Création de l'index FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Ajout des vecteurs à l'index
index.add(np.array(embeddings, dtype=np.float32))

print(f"Index créé avec {index.ntotal} documents.")
