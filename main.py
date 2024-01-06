from note_manager import NoteManager
from category_manager import CategoryManager

class SmartNoteApp:
    def __init__(self):
        self.note_manager = NoteManager()
        self.category_manager = CategoryManager()

    def run(self):
        while True:
            print("\nSmartNote - Command-Line Note Taking App")
            print("1. Add Note")
            print("2. List Notes")
            print("3. Search Notes")
            print("4. Add Category")
            print("5. List Categories")
            print("0. Exit")

            choice = input("Enter your choice: ")
            if choice == '1':
                self.note_manager.add_note()
            elif choice == '2':
                self.note_manager.list_notes()
            elif choice == '3':
                self.note_manager.search_notes()
            elif choice == '4':
                self.category_manager.add_category()
            elif choice == '5':
                self.category_manager.list_categories()
            elif choice == '0':
                print("Exiting SmartNote. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = SmartNoteApp()
    app.run()
