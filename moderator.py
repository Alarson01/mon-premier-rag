class Moderator:

    def __init__(self):
        pass

    def moderate(self, question):

        suspicious_words = [
            "ignore",
            "oublie",
            "ignore toutes les instructions",
            "prompt injection"
        ]

        for word in suspicious_words:

            if word.lower() in question.lower():

                return {
                    "is_prompt_injection": True
                }

        return {
            "is_prompt_injection": False
        }
