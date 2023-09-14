# Функция для загрузки заметок из файла
from ast import NotEq
import json


def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes_data = json.load(f)
            for note_data in notes_data:
                note = NotEq(note_data["id"], note_data["title"], note_data["body"], note_data["date"])
                notes_manager.notes.append(note)
    except FileNotFoundError:
        pass
