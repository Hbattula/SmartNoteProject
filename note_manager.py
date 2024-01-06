from encryption import encrypt, decrypt

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("Enter note title: ")
        content = input("Enter note content: ")

        category = input("Enter category (optional): ")
        if category not in self.get_all_categories():
            print("Invalid category. Please add the category first.")
            return

        self.notes.append({'title': title, 'content': content, 'category': category})
        print("Note added successfully!")

    def list_notes(self):
        print("\n--- List of Notes ---")
        for note in self.notes:
            print(f"Title: {note['title']}\nContent: {note['content']}\nCategory: {note['category']}\n")

    def search_notes(self):
        keyword = input("Enter search keyword: ")
        matching_notes = [note for note in self.notes if keyword.lower() in note['title'].lower()]
        if matching_notes:
            print("\n--- Matching Notes ---")
            for note in matching_notes:
                print(f"Title: {note['title']}\nContent: {note['content']}\nCategory: {note['category']}\n")
        else:
            print("No matching notes found.")

    def get_all_categories(self):
        return set(note['category'] for note in self.notes if 'category' in note)
