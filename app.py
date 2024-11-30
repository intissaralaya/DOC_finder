# Import des modules nécessaires
import os
from flask import Flask, render_template, request, send_file

# Création d'une instance de l'application Flask
app = Flask(__name__)

# Définition d'une fonction qui prend un répertoire en entrée et retourne une liste de chemins de fichiers contenus dans ce répertoire et ses sous-répertoires.
def index_files(directory):
    indexed_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            indexed_files.append(os.path.join(root, file))
    return indexed_files

# Définition d'une fonction qui prend une liste de chemins de fichiers indexés et une requête de recherche en entrée, puis retourne une liste des chemins de fichiers correspondant à la requête.
def search_files(indexed_files, query):
    results = []
    for file_path in indexed_files:
        if query.lower() in file_path.lower():
            results.append(file_path)
    return results

# Route pour la page d'accueil de l'application web.
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la recherche.
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    
    # Liste des répertoires à indexer
    directories_to_index = [
        r'C:\Users\pc\Desktop\2émé_LSI_S 1',
        r'C:\Users\pc\Desktop\desktop\docs',
        r'C:\Users\pc\Desktop\2éme_LSI_S2',
        r'C:\Users\pc\Desktop\java'
    ]
    
    # Indexation des fichiers pour chaque répertoire
    indexed_files = sum([index_files(directory) for directory in directories_to_index], [])
    
    # Recherche dans les fichiers indexés
    results = search_files(indexed_files, query)
    
    # Rendre le modèle HTML avec les résultats de la recherche
    return render_template('search.html', results=results)

# Route pour ouvrir le fichier sélectionné
@app.route('/open_file', methods=['POST'])
def open_file():
    file_path = request.form['file_path']
    return send_file(file_path, as_attachment=True)

# Point d'entrée de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
