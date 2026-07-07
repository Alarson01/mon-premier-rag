from vectordb import VectorDB
from moderator import Moderator


class RAG:

    def __init__(self):

        self.db = VectorDB()
        self.moderator = Moderator()

    def answer_question(self, question):

        moderation = self.moderator.moderate(
            question
        )

        if moderation["is_prompt_injection"]:

            return (
                "Question refusée : "
                "tentative de prompt injection détectée."
            )

        chunks = self.db.retrieve(
            question
        )

        return chunks["documents"][0]
