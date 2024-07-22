# Read the file
with open('binary_rankings_cnn_no_temp_old.txt', 'r') as file:
    lines = file.readlines()

# Split each line into speaker id, number1, and number2
data = [line.strip().split() for line in lines]

# Sort the data based on the first number
sorted_data = sorted(data, key=lambda x: float(x[2]))

# Write the sorted data to a new file
with open('sorted_file_bin.txt', 'w') as file:
    for line in sorted_data:
        file.write(' '.join(line) + '\n')

# WE ALWAYS WANT WORST TO BEST ACCENT
