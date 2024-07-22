import pandas as pd
import re
import os
from collections import Counter
from itertools import combinations


# Load the Excel file
file_path = '/Users/spencer.jensen/Downloads/workspace-export-Accentedness-Pilot-Workspace_1-1105763008-251k1thb2a.xlsx'
excel_data = pd.ExcelFile(file_path)

# Initialize a Counter to store speaker counts
speaker_counts = Counter()

# Define a regex pattern to extract SPEAKERxxxx
pattern = re.compile(r'SPEAKER\d{4}')
rows = []
# Loop through each sheet in the Excel file
for sheet_name in excel_data.sheet_names:
    # Load the sheet into a DataFrame
    df = pd.read_excel(excel_data, sheet_name=sheet_name, header=None)

    # Extract the pattern from column 0 rows 4 through 6
    pattern_rows = df.iloc[4:7, 0].tolist()
    # Extract the numbers from column 2 rows 4 through 6
    numbers_rows = df.iloc[4:7, 2].tolist()
    
    # Print the pattern and numbers
    pattern_rows = [pattern.split("/")[-2] for pattern in pattern_rows]

    # Zip the pattern_rows and numbers_rows into a dictionary
    pattern_numbers_dict = dict(zip(pattern_rows, numbers_rows))
    
    sorted_dict = dict(sorted(pattern_numbers_dict.items(), key=lambda x: x[1]))
    # print(sorted_dict)
    # Compare all pairwise combinations of the 3 speaker, number combos
    for combo1, combo2 in combinations(sorted_dict.items(), 2):
        speaker1, number1 = combo1
        speaker2, number2 = combo2
        # print(f"Comparing {speaker1} with {speaker2}")
        # Compare the numbers and perform desired operations
        if number1 > number2:
            # print(f"{speaker1} has a higher number than {speaker2}")
            rows.append(f"{speaker1} > {speaker2}")
        elif number1 < number2:
            # print(f"{speaker1} has a lower number than {speaker2}")
            rows.append(f"{speaker1} < {speaker2}")
        else:
            # print(f"{speaker1} has the same number as {speaker2}")
            rows.append(f"{speaker1} = {speaker2}")
# print(rows)

with open('/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/survey/rankings.txt', 'w') as f:
    for row in rows:
        f.write(row + '\n')
print("DONE")
