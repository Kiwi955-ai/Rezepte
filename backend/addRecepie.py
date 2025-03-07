import json
import os

def add_rezept( name, image, zutaten, anleitung, id):
    dateipfad ="superDB.json"
    neues_rezept = {
        "id": id,
        "name": name,
        "image": image,
        "zutaten": zutaten,
        "anleitung": anleitung
    }

    # Prüfen, ob die Datei existiert und lesen
    if os.path.exists(dateipfad):
        with open(dateipfad, "r", encoding="utf-8") as file:
            try:
                rezepte = json.load(file)
            except json.JSONDecodeError:
                rezepte = []  # Falls die Datei leer oder beschädigt ist
    else:
        rezepte = []

    # Rezept hinzufügen
    rezepte.append(neues_rezept)

    # JSON-Datei überschreiben
    with open(dateipfad, "w", encoding="utf-8") as file:
        json.dump(rezepte, file, indent=4, ensure_ascii=False)

    print(f"Rezept '{name}' wurde hinzugefügt.")


