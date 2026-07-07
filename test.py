from vectordb import VectorDB

db = VectorDB()

result = db.retrieve(
    "Quelle est la couleur du chat de Bob ?"
)

print(result["documents"][0])
