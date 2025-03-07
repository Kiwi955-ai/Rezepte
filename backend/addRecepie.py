import json
import os

def add_rezept( id ,name, image, zutaten, anleitung):
    dateipfad ="superDB.json"
    neues_rezept = {
        "id": id,
        "name": name,
        "image": image,
        "zutaten": zutaten, #in array form
        "anleitung": anleitung
    }

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

ordner_pfad = "/home/nnnkbp/Rezepte-main/Rezepte/img"

dateien_liste = os.listdir(ordner_pfad)
for i in range(len(dateien_liste)):
    name  = dateien_liste[i].split(".")[0]
    add_rezept(i+1,name,dateien_liste[i],["Null"],"Null")