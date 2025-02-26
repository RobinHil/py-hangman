# 🎮 Jeu du Pendu (Hangman)

## 📝 Description
Ce projet est une implémentation simple du jeu classique du pendu en Python dans le terminal. Le joueur doit deviner un mot caché en proposant des lettres une par une. Chaque erreur fait progresser le dessin du pendu!

## ✨ Fonctionnalités
- 🎲 Sélection aléatoire d'un mot parmi une liste prédéfinie
- 🖼️ Affichage graphique ASCII du pendu qui se construit progressivement
- 👀 Visualisation des lettres découvertes et restantes à trouver
- 🔄 Suivi du nombre de tentatives restantes

## 🚀 Comment jouer
1. Assurez-vous d'avoir Python installé sur votre ordinateur
2. Téléchargez ou clonez ce dépôt
3. Exécutez le fichier `hangman.py` avec Python:
   ```
   python hangman.py
   ```
4. Suivez les instructions à l'écran pour proposer des lettres

## 🎯 Règles du jeu
- Vous avez 7 tentatives pour deviner le mot complet
- À chaque erreur, une partie du dessin du pendu apparaît
- Vous gagnez si vous trouvez toutes les lettres avant que le dessin du pendu ne soit complet
- Vous perdez si le dessin du pendu est complété avant que vous n'ayez deviné le mot

## 🔤 Liste des mots
Par défaut, les mots à deviner sont sélectionnés parmi les suivants:
- souris
- clavier
- hexadecimal
- ecran
- ordinateur
- processeur
- guitare
- feuille
- argent
- corde

Vous pouvez changer les mots disponibles en modifiant simplement la liste.

## 🛠️ Personnalisation
Vous pouvez facilement modifier la liste des mots en éditant le tableau `choix` au début du fichier `hangman.py`.
