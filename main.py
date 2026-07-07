from rag import RAG

rag = RAG()

question = input("Question : ")

response = rag.answer_question(
    question
)

print(response)
