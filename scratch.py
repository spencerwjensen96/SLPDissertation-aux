import os

import numpy as np

dictionary = {}
file = '/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/models/ppg_rankings_no_temp.txt'

rows = []
with open(file, 'r') as f:
    for line in f:
        if f"SPEAKER{line[1:5]}" not in dictionary:
            dictionary[f"SPEAKER{line[1:5]}"] = {'l1': float(line.split(',')[1]), 'l2': float(line.split(',')[2]), 'count': 1}
        else:
            dictionary[f"SPEAKER{line[1:5]}"]['l1'] += float(line.split(',')[1])
            dictionary[f"SPEAKER{line[1:5]}"]['l2'] += float(line.split(',')[2])
            dictionary[f"SPEAKER{line[1:5]}"]['count'] += 1

for speaker, dictionary in dictionary.items():
    rows.append(f"{speaker} {float(dictionary['l1'])/dictionary['count']} {float(dictionary['l2'])/dictionary['count']}")
        
with open('ppg_ranking.txt', 'w') as f:
    for row in rows:
        f.write(f"{row}\n")