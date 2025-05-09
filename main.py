# main.py

# Importer le usecase principal (l'orchestrateur de l'automatisation)
from app.run_certification import run_certification

# Point d'entrée principal
if __name__ == "__main__":
    # Démarrer le processus automatisé de résolution de certification
    run_certification()
