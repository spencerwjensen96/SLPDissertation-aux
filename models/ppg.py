import csv

def process_csv(filename):
    ids = []
    column1_sum = 0
    column2_sum = 0
    count = 0
    speakers = {}

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            id = row[0][1:5]
            if id not in speakers:
                speakers[id] = {'l1': 0, 'l2': 0, 'count': 0}
            else:
                speakers[id]['l1'] += float(row[1])
                speakers[id]['l2'] += float(row[2])
                speakers[id]['count'] += 1
    new_rows = ["speaker,L1,L2"]
    for speaker, dictionary in speakers.items():
        new_rows.append(f"SPEAKER{speaker}, {dictionary['l1']/dictionary['count']}, {dictionary['l2']/dictionary['count']}")
    return new_rows

if __name__ == "__main__":
    filename = '/Users/spencer.jensen/Downloads/ppgs_probs_speech_ocean.csv'
    speakers = process_csv(filename)
    print(speakers)

    with open('ppg_rankings.txt', 'w') as file:
        for row in speakers:
            file.write(row + '\n')