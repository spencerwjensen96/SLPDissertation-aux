import os
import random
import math
import sys
import matplotlib.pyplot as plt

def num_comparisons(n):
    if n == 1 :
        return 0 
    else:
        return n-1 + num_comparisons(n-1)

def select_random_files(file_path, directories, num_choices=4):
    
    selected_directories = random.sample(directories, num_choices)

    selected_files = {}
    for directory in selected_directories:
        files = [f for f in os.listdir(os.path.join(file_path, directory)) if os.path.isfile(os.path.join(file_path, directory, f))]
        if files:
            selected_file = random.choice(files)
            selected_files[directory] = selected_file

    return selected_files

if __name__ == "__main__":
    try:
        questions = int(sys.argv[1])
        if len(sys.argv) > 2:
            num_choices = int(sys.argv[2])
    except:
        raise ValueError(f"please provide the number of questions to generate as an argument. Ex: \"python {sys.argv[0]} <num-questions> <num-options-in-question>\"")

    file_path = '/Users/spencer.jensen/Downloads/speechocean762/WAVE'
    files = {}
    csv_rows = []

    directories = [d for d in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, d))]
    for i in range(questions):
        selected_files = select_random_files(file_path, directories, num_choices)
        for key, value in selected_files.items():
            if key not in files.keys():
                files[key] = [value]
            files[key].append(value)
        csv_rows.append(selected_files)

    print(num_comparisons(num_choices))
    print(len(files.keys()), " speakers represented in the survey.")
    print(len(csv_rows), " questions to select for the survey.")
    print(len(csv_rows) * num_comparisons(num_choices), " number of comparisons made.")

    # when writing survey file -> Folder1/File1.wav Folder2/File2.wav etc
    include_folder_location = False
    #else -> File1.wav File2.wav etc

    with open('survey.csv', 'w') as f:
        for row in csv_rows:
            for key, value in row.items():
                if include_folder_location:
                    f.write(f"{key}/{value} ")
                else:
                    f.write(f"{value} ")
            f.write("\n")
