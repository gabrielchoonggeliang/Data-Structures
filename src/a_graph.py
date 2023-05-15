import re
import matplotlib.pyplot as plt
import os

# Define the sorting algorithm names
algorithm_names = ['Selection Sort', 'Merge Sort', 'Quick Sort v1', 'Quick Sort v2']

# Read the time taken from the "output.txt" file
time_taken = [[] for _ in range(len(algorithm_names))]

with open('output.txt', 'r') as file:
    content = file.read()

    for i, algorithm_name in enumerate(algorithm_names):
        pattern = f"Time elapsed for {algorithm_name} with n = \\d+: (\\d+\\.\\d+) seconds"
        matches = re.findall(pattern, content)

        if matches:
            time_taken[i] = [float(time) for time in matches]
        else:
            time_taken[i] = [0.0]

# X-axis values (array sizes)
array_sizes = [100, 10000, 50000, 75000, 500000]

# Create the "img" directory if it doesn't exist
img_dir = "../img"
os.makedirs(img_dir, exist_ok=True)

# Set plot style for Thesis paper
plt.style.use('seaborn-whitegrid')

# Define colors for each algorithm
colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red']

# Plotting and saving the figures
for i, algorithm_name in enumerate(algorithm_names, start=1):
    plt.figure(i, figsize=(10, 8))  # Adjust figure size according to your preference
    plt.plot(array_sizes, time_taken[i-1], label=algorithm_name, color=colors[i-1])
    plt.xlabel('Array Size', fontsize=12)
    plt.ylabel('Execution Time (seconds)', fontsize=12)
    plt.title(algorithm_name, fontsize=14)
    plt.legend(fontsize=10)
    plt.savefig(os.path.join(img_dir, f'a_{algorithm_name.lower().replace(" ", "_")}.png'), dpi=300)
    plt.close()

# Display the figures
for i in range(1, len(algorithm_names) + 1):
    fig_path = os.path.join(img_dir, f'a_{algorithm_names[i-1].lower().replace(" ", "_")}.png')
    plt.figure(figsize=(10, 8))  # Adjust figure size according to your preference
    img = plt.imread(fig_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
