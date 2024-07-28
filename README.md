# Scraper de Manga LelManga

## Description
Ce script Python permet de télécharger automatiquement des chapitres de manga depuis le site LelManga. Il peut télécharger un seul chapitre ou une série de chapitres consécutifs, en organisant les images dans des dossiers appropriés.

## Fonctionnalités
- Téléchargement d'un seul chapitre de manga
- Téléchargement de plusieurs chapitres consécutifs
- Organisation automatique des images dans des dossiers par manga et par chapitre
- Gestion des erreurs pour les chapitres non disponibles

## Prérequis
- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation
1. Clonez ce dépôt ou téléchargez le script `scraplel.py`
2. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Utilisation
Pour télécharger un seul chapitre :
```
python scraplel.py [URL du chapitre]
```

Pour télécharger une série de chapitres :
```
python scraplel.py [URL du premier chapitre] [Numéro du dernier chapitre]
```

Exemple :
```
python scraplel.py https://www.lelmanga.com/my-hero-academia-340 380
```
Cela téléchargera les chapitres 340 à 380 de My Hero Academia.

## Structure des dossiers
Le script crée la structure de dossiers suivante :
```
[Nom du Manga]/
    Chapter_[Numéro du Chapitre]/
        page_001.jpg
        page_002.jpg
        ...
```

