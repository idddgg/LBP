# Analyse des Finances Locales 

Ce répertoire contient l'analyse approfondie des finances locales françaises pour l'exercice 2022. 
L'intégralité du code utilisé pour générer les visualisations et les indicateurs de notre support de présentation est ici documentée de manière reproductible.

## Architecture du projet

* **Gestion des dépendances :** Utilisation de `uv` pour une gestion des dépendances moderne, rapide et performante.
* **Structure des dossiers :**
    * `notebooks/` : Contient le notebook Jupyter documenté : ce notebook a été utilisé uniquement pour générer les visuels, graphiques et statistiques qui sont présentés dans le support PowerPoint (Notebook Propre).
    * `src/` : Dossier contenant le fichier de configuration (path des repos).
    * `figures/` : Dossier contenant les images et graphiques.
    * `data/` : Espace de stockage pour le jeu de données (fichier CSV brut).
