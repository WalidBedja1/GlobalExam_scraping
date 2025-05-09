# Fichier principal d'orchestration du processus complet

from infrastructure.scraping.globalexam_bot import GlobalExamBot
from infrastructure.ia.chatgpt import ChatGPTClient
from infrastructure.db.mongo_repo import MongoRepo
from domain.services.answer_solver import AnswerSolver

def run_certification():
    # Étape 1 : initialisation des dépendances
    bot = GlobalExamBot()
    gpt = ChatGPTClient()
    db = MongoRepo()
    solver = AnswerSolver(db, gpt)

    # Étape 2 : connexion au site et démarrage de l'examen
    bot.login()
    bot.start_certification()

    # Étape 3 : boucle sur les questions
    while bot.has_next_exercise():
        question = bot.get_current_question()  # récupère énoncé + options
        answer = solver.solve(question)       # cherche réponse dans Mongo, sinon GPT
        bot.submit_answer(answer)             # répond sur l'interface GlobalExam
