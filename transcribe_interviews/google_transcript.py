import os
import json

rows = []
with open('trans.json', 'r') as file:
    data = json.load(file)

    for obj in data['results']:
        # print(obj)
        if 'transcript' in obj['alternatives'][0]:
            continue
            # print(obj['alternatives'][0]['transcript'])
        elif obj['alternatives'][0]['words']:
            sentence = []
            for word in obj['alternatives'][0]['words']:
                if len(sentence) == 0:
                    sentence.append(word)
                elif sentence[-1]['speakerLabel'] == word['speakerLabel']:
                    sentence.append(word)
                else:
                    speaker = "Interviewer"
                    if sentence[0]['speakerLabel'] == '2':
                        speaker = "Volunteer"
                    rows.append(f"{speaker}")
                    rows.append(" ".join(list(word['word'] for word in sentence)))
                    print("SPEAKER:", sentence[0]['speakerLabel'])
                    print(" ".join(list(word['word'] for word in sentence)))
                    sentence = []
              
with open('output.txt', 'w') as file:
    for row in rows:
        file.write(row + '\n')

# Rest of your code goes here

    