import re
import os
import numpy as np

from rbo import rbo
from scipy.stats import pearsonr   

def get_list_of_speaker_ids(speaker_list, speaker_to_id):
    return [speaker_to_id[speaker] for speaker in speaker_list]

def get_first_texts(file1_path, file2_path, file3_path):
    texts1 = []
    texts2 = []
    texts3 = []

    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(file3_path, 'r') as file3:
        
        for line in file1:
            text1 = line.split()[0]  # Get the first text of each line
            if re.match(r'SPEAKER\d{4}', text1):
                texts1.append(text1)

        for line in file2:
            text2 = line.split()[0]  # Get the first text of each line
            if re.match(r'SPEAKER\d{4}', text2):
                texts2.append(text2)
        
        for line in file3:
            text3 = line.split()[0]
            if re.match(r'SPEAKER\d{4}', text3):
                texts3.append(text3)

    return texts1, texts2, texts3

# Example usage
file1_path = 'binary_rankings_cnn_no_temp.txt'
file2_path = 'whisper_rankings.txt'
file3_path = 'ppg_rankings_no_temp.txt'

speaker_to_id = np.load('/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/models/speaker_to_id.npy', allow_pickle=True).item()
base = np.load('/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/survey/ranking_results.npy', allow_pickle=True).item()
base = list(base.keys())

texts1, texts2, texts3 = get_first_texts(file1_path, file2_path, file3_path)

# Calculate ranking score using rbo.rank function
for i, compare in enumerate([texts1, texts2, texts3]):
    assert len(compare) == len(base), "The number of texts in the files must be equal"

    print(f"Comparing base with text{i+1}")
    ranking_score = rbo(base, compare, 0.9)
    print(f"RBO score:", ranking_score)
    pearson_stats = pearsonr(get_list_of_speaker_ids(base, speaker_to_id), get_list_of_speaker_ids(compare, speaker_to_id))
    print(f"Pearson correlation:", pearson_stats[0], f"p={pearson_stats[1]}")
