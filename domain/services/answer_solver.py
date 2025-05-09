# Service métier : logique pour trouver une réponse

class AnswerSolver:
    def __init__(self, db, gpt):
        self.db = db
        self.gpt = gpt

    def solve(self, exercice):
        # Étape 1 : chercher si la question existe dans Mongo
        answer = self.db.find_answer(exercice.statement)

        # Étape 2 : si elle n'existe pas, appeler GPT
        if not answer:
            answer = self.gpt.ask(exercice.statement, exercice.options)
            self.db.save_answer(exercice.statement, answer)

        return answer
