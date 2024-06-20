import os
import random
import matplotlib.pyplot as plt

def select_random_files(file_path, directories, num_choices=4):
    
    selected_directories = random.sample(directories, num_choices)

    selected_files = {}
    for directory in selected_directories:
        files = [f for f in os.listdir(os.path.join(file_path, directory)) if os.path.isfile(os.path.join(file_path, directory, f))]
        if files:
            selected_file = random.choice(files)
            selected_files[directory] = selected_file

    return selected_files

# Usage example
file_path = '/Users/spencer.jensen/Downloads/speechocean762/WAVE'
questions = 500

directories = [d for d in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, d))]

files = {}
csv_rows = []

for i in range(questions):
    selected_files = select_random_files(file_path, directories)
    for key, value in selected_files.items():
        if key not in files.keys():
            files[key] = [value]
        files[key].append(value)
    csv_rows.append(selected_files)

print(len(files.keys()), " speakers represented in the survey.")
print(len(csv_rows), " questions to select for the survey.")
