class CategoryManager:
    def __init__(self):
        self.categories = set()

    def add_category(self):
        category = input("Enter category name: ")
        if category not in self.categories:
            self.categories.add(category)
            print("Category added successfully!")
        else:
            print("Category already exists. Please choose a different name.")

    def list_categories(self):
        print("\n--- List of Categories ---")
        for category in self.categories:
            print(category)
