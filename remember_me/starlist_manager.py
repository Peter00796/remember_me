import csv
import os

class StarListManager:
    def __init__(self, file_path="star_words/stared.csv"):
        self.file_path = file_path
        directory = os.path.dirname(self.file_path)
        if not os.path.exists(directory):
            raise FileNotFoundError(f"The directory for the file path '{self.file_path}' does not exist.")
        
        if not os.path.exists(self.file_path):
            user_input = input(f"The file '{self.file_path}' does not exist. Do you want to create a new star list? (y/n): ").strip().lower()
            if user_input == 'y':
                os.makedirs(directory, exist_ok=True)
                with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Word", "Definition"])
                self.starred_words = []
            else:
                raise FileNotFoundError(f"The file '{self.file_path}' does not exist and no new file was created.")
        else:
            self.starred_words = self.load_starred_words()

    def add_to_star_list(self, word):
        if word not in self.starred_words:
            self.starred_words.append(word)
            return f"'{word['word']}' has been added to the star list."
        return f"'{word['word']}' is already in the star list."

    def remove_from_star_list(self, word):
        if word in self.starred_words:
            self.starred_words.remove(word)
            return f"'{word['word']}' has been removed from the star list."
        return f"'{word['word']}' is not in the star list."

    def display_star_list(self):
        if self.starred_words:
            output = "\nStarred Words:\n"
            for idx, w in enumerate(self.starred_words, start=1):
                output += f"{idx}. {w['word']}: {w['definition']}\n"
            return output
        return "Star list is empty."

    def save_starred_words(self):
        with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Word", "Definition"])
            for word in self.starred_words:
                writer.writerow([word['word'], word['definition']])

    def load_starred_words(self):
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [{'word': row['Word'], 'definition': row['Definition']} for row in reader]
        except FileNotFoundError:
            return []