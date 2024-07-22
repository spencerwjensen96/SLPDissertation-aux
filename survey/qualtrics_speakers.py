import pandas as pd
import re
import os
from collections import Counter

# Load the Excel file
file_path = '/Users/spencer.jensen/Downloads/workspace-export-Accentedness-Pilot-Workspace_1-1105763008-251k1thb2a.xlsx'  # replace with the actual file path
excel_data = pd.ExcelFile(file_path)

# Initialize a Counter to store speaker counts
speaker_counts = Counter()

# Define a regex pattern to extract SPEAKERxxxx
pattern = re.compile(r'SPEAKER\d{4}')

# Loop through each sheet in the Excel file
for sheet_name in excel_data.sheet_names:
    # Load the sheet into a DataFrame
    df = pd.read_excel(excel_data, sheet_name=sheet_name, header=None)
    
    # Loop through each cell in the DataFrame
    for row in df.itertuples(index=False, name=None):
        for cell in row:
            if isinstance(cell, str):
                # Find all matches of the pattern in the cell
                matches = pattern.findall(cell)
                # Update the Counter with the found matches
                speaker_counts.update(matches)

# Convert the Counter to a DataFrame for easy viewing
speaker_counts_df = pd.DataFrame(speaker_counts.items(), columns=['Speaker', 'Count'])

# Print the number of speakers
for i in range(1, 11):
    print(f"Number of speakers with count of {i}: {len(speaker_counts_df[(speaker_counts_df['Count'] == i)])}")

# Sort the DataFrame by the 'Count' column in descending order
sorted_df = speaker_counts_df.sort_values('Count', ascending=False)

# Print the sorted DataFrame
# print(sorted_df)

wav_path = '/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/WAVE'
speakers = [f for f in os.listdir(wav_path) if os.path.isdir(os.path.join(wav_path, f))]
# print(speakers)

# Find the missing speakers
missing_speakers = [speaker for speaker in speakers if speaker not in speaker_counts_df['Speaker'].tolist()]

# Print the missing speakers
print("Missing Speakers: ", missing_speakers)
# # Save the result to a new Excel file
# output_file_path = '/mnt/data/speaker_counts.xlsx'
# speaker_counts_df.to_excel(output_file_path, index=False)

# output_file_path