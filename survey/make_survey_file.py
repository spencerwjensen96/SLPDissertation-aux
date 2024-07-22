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

def select_random_files(file_path, directories, num_choices=4, word_counts={}):
    
    selected_directories = random.sample(directories, num_choices)
    
    selected_files = {}
    for directory in selected_directories:
        files = [f for f in os.listdir(os.path.join(file_path, directory)) if os.path.isfile(os.path.join(file_path, directory, f))]
        # we want to select files with more word count
        if word_counts:
            new_files = []
            for f in files:
                if f.split(".")[0] in word_counts:
                    new_files.append((f, word_counts[f.split(".")[0]]))
            # sort by word count
            max_value = max([int(f[1]) for f in new_files])
            # only select files that are within 2 words of the max value
            new_files = [f[0] for f in sorted(new_files, key=lambda x: x[1], reverse=True) if max_value - int(f[1]) <= 2]
            files = new_files

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

    file_path = '/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/WAVE'
    files = {}
    rows = []

    # represents a count of transcript length for each file
    word_counts = {}
    with open('word_counts.txt', 'r') as f:
        for line in f:
            file, count = line.strip().split()
            word_counts[file] = int(count)

    directories = [d for d in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, d))]
    for i in range(questions):
        selected_files = select_random_files(file_path, directories, num_choices, word_counts)
        for key, value in selected_files.items():
            if key not in files.keys():
                files[key] = [value]
            files[key].append(value)
        rows.append(selected_files)

    print(len(files.keys()), " speakers represented in the survey.")
    print(len(rows), " questions to select for the survey.")
    print(len(rows) * num_comparisons(num_choices), " number of comparisons made.")

    # when writing survey file -> Folder1/File1.wav Folder2/File2.wav etc
    include_folder_location = True
    #else -> File1.wav File2.wav etc

    with open('survey.txt', 'w') as f:
        for row in rows:
            for key, value in row.items():
                if include_folder_location:
                    f.write(f"{key}/{value} ")
                else:
                    f.write(f"{value} ")
            f.write("\n")
