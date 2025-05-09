# Modèle d’un exercice (énoncé + choix)

class Exercice:
    def __init__(self, statement: str, options: list[str]):
        self.statement = statement
        self.options = options
