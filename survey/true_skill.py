import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from trueskill import Rating, rate_1vs1, quality_1vs1, rate


root_dir = "/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/survey"

def get_speakers(dir="/Users/spencer.jensen/Desktop/university/dissertation/code/SLPDissertation-aux/WAVE"):
    return [i for i in os.listdir(dir)]
        
def read_listening_test_csv(file_name):
    results = []
    with open(file_name) as infile:
        reader = csv.reader(infile)
        key = next(reader) 
        for row in reader:
            results.append(row[0])
    results = np.array(results, dtype=str)
    return results

def calculate_ratings(results, init_mean=25, init_std=8.333):

    speakers = get_speakers()
    ratings = {}
    for speaker in speakers:
        ratings[speaker] = Rating(init_mean, init_std)

    # simulate rankings
    for pair in results:
        r = pair.split()
        speaker1 = r[0]
        speaker2 = r[2]
        if r[1] == '>':
            ratings[speaker1], ratings[speaker2] = rate_1vs1(ratings[speaker1], ratings[speaker2])
        elif r[1] == '<':
            ratings[speaker2], ratings[speaker1] = rate_1vs1(ratings[speaker2], ratings[speaker1])
        elif r[1] == '=':
            ratings[speaker2], ratings[speaker1] = rate_1vs1(ratings[speaker1], ratings[speaker2], drawn=True)

    return ratings

def plot_rankings(ratings, sort=True, avg_line=True):
    a = {}
    for key, value in ratings.items():
        a[key] = {'mu': value.mu, 'sigma': value.sigma}
    a = dict(sorted(a.items(), key=lambda item: item[1]['mu'], reverse=sort))
    print(a.items())
    np.save('ranking_results.npy', a)
    # # Sort the ratings based on the value.mu
    # ratings = dict(sorted(ratings.items(), key=lambda item: item[1].mu, reverse=sort))

    # # Extract the speaker names, ratings, and standard deviations
    # speakers = list(ratings.keys())
    # ratings_values = [rating.mu for rating in ratings.values()]
    # std_values = [rating.sigma for rating in ratings.values()]
    # Calculate the average rating
    avg_rating = np.mean([rating['mu'] for rating in a.values()])

    # Plot the ratings
    plt.errorbar(range(len(a)), [rating['mu'] for rating in a.values()], yerr=[rating['sigma'] for rating in a.values()], fmt='o')
    plt.axhline(y=avg_rating, color='r', linestyle='--')  # Add a horizontal line for average rating
    # plt.xticks(range(len(a)), a.keys(), rotation=45)
    plt.xlabel('Speaker')
    plt.ylabel('Rating')
    plt.title('Speaker Ratings')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__" :
    listening_test_csv = f"{root_dir}/rankings.txt"
    
    results = read_listening_test_csv(listening_test_csv)
    ratings = calculate_ratings(results, 0, 3)

    plot_rankings(ratings)