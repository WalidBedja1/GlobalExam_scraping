# Automatisation du site GlobalExam avec Selenium

from selenium import webdriver
from config import EMAIL, PASSWORD, GLOBAL_EXAM_URL

class GlobalExamBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # Navigue vers le site, remplit le formulaire de connexion
        self.driver.get(GLOBAL_EXAM_URL)
        # Trouver les champs, envoyer EMAIL + PASSWORD, cliquer login

    def start_certification(self):
        # Accéder à la certification ciblée
        # Cliquer sur la bonne section

    def has_next_exercise(self):
        # Détecter si un nouvel exercice est chargé
        return True or False

    def get_current_question(self):
        # Récupère l’énoncé + les options visibles
        return Exercice(statement, options)

    def submit_answer(self, answer):
        # Clique sur la bonne option en fonction de la réponse
        # Passe à la question suivante
