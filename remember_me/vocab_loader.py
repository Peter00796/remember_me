import csv

def load_vocabulary(file_path):
    vocabulary = []
    sections = {}
    current_section = "General"  # Default section if no section is defined

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if it exists
        for row in reader:
            if len(row) >= 2:
                if row[1].startswith("Section") or not row[2].strip(): # new section detected if the definition is empty
                    # New section identified
                    current_section = row[1].strip()
                    if current_section not in sections:
                        sections[current_section] = []
                else:
                    # Add the word to the current section
                    word_entry = {'word': row[1], 'definition': row[2]}
                    sections[current_section].append(word_entry)
                    vocabulary.append(word_entry)  # Keep for general mode
                 
                 

    return vocabulary, sections