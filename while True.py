# Загружаем заметки из файла при запуске программы
load_notes()

# Бесконечный цикл для ввода команд с консоли
while True:
    print("Введите команду (для помощи введите 'help'): ")
    command = input()
    if command == "help":
        print("Список команд:\n"
              "create - создать новую заметку\n"
              "edit - редактировать существующую заметку\n"
              "delete - удалить существующую заметку\n"
              "search - найти заметки по ключевому слову\n"
              "list - вывести список всех заметок\n"
              "exit - выйти из программы")
    elif command == "create":
        print("Введите заголовок заметки:")
        title = input()
        print("Введите текст заметки:")
        body = input()
        notes_manager.create_note(title, body)
        save_notes()
        print("Заметка успешно создана.")
    elif command == "edit":
        print("Введите ID заметки, которую необходимо отредактировать:")
        note_id = int(input())
        note = notes_manager.get_note_by_id(note_id)
        if note:
            print(f"Заголовок: {note.title}")
            print(f"Текст: {note.body}")
            print("Введите новый заголовок (оставьте пустым, чтобы оставить прежний):")
            new_title = input()
            print("Введите новый текст (оставьте пустым, чтобы оставить прежний):")
            new_body = input()
            if new_title or new_body:
                notes_manager.edit_note(note_id, new_title, new_body)
                save_notes()
                print("Заметка успешно отредактирована.")
            else:
                print("Новый заголовок или текст не введены.")
        else:
            print("Заметка с указанным ID не найдена.")
    elif command == "delete":
        print("Введите ID заметки, которую необходимо удалить:")
        note_id = int(input())
        note = notes_manager.get_note_by_id(note_id)
        if note:
            notes_manager.delete_note(note_id)
            save_notes()
            print("Заметка успешно удалена.")
        else:
            print("Заметка с указанным ID не найдена.")
    elif command == "search":
        print("Введите ключевое слово для поиска:")
        keyword = input()
        found_notes = notes_manager.search_notes(keyword)
        print_notes(found_notes)
    elif command == "list":
        sorted_notes = notes_manager.sort_notes()
        print_notes(sorted_notes)
    elif command == "exit":
        break
    else:
        print("Неверная команда. Введите 'help', чтобы узнать список команд.") 

