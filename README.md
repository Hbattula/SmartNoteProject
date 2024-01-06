# SmartNote - Command-Line Note Taking App

## Overview

SmartNote is a command-line note-taking application designed to provide users with a simple yet feature-rich experience. It allows users to organize their notes, search for specific content, and secure their notes using encryption.

## Project Structure

- **main.py:** The main file responsible for handling user input and executing actions.
- **note_manager.py:** A module for managing notes, including adding, listing, searching, and encrypting/decrypting notes.
- **category_manager.py:** A module for managing categories, allowing users to organize notes.
- **encryption.py:** A module for handling encryption and decryption of notes.

## Features

- **Add Note:** Users can add new notes with a title, content, and an optional category.
- **List Notes:** Display a list of all notes with their titles, content, and categories.
- **Search Notes:** Search for notes based on keywords in titles.
- **Add Category:** Users can add new categories to organize their notes.
- **List Categories:** Display a list of all categories.

## How to Use

1. Open `main.py` in a Python environment.
2. Run the script to start the SmartNote application.
3. Follow the on-screen prompts to perform various actions.

## Dependencies

- This project uses the `cryptography` library for encryption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
