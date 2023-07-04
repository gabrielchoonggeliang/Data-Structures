import re
import matplotlib.pyplot as plt
import numpy as np
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

# Convert time_taken to a NumPy array
time_taken = np.array(time_taken)

# X-axis values (array sizes)
array_sizes = [100, 10000, 50000, 75000, 100000, 500000]

# Create the "img" directory if it doesn't exist
img_dir = "../img"
os.makedirs(img_dir, exist_ok=True)

# Define colors for the bars
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plotting and saving the figures
for i, size in enumerate(array_sizes):
    fig, ax = plt.subplots(figsize=(8, 6))
    algorithms = ['Selection Sort', 'Merge Sort', 'Quick Sort v1', 'Quick Sort v2']
    execution_times = time_taken[:, i]  # Extract execution times for the specific array size

    # Plot the bar chart
    bars = ax.bar(algorithms, execution_times, color=colors)

    # Add black lines at each y-axis label
    for bar in bars:
        height = bar.get_height()
        ax.plot([bar.get_x(), bar.get_x() + bar.get_width()], [height, height], color='black', linewidth=0.5)

    # Adjust the y-limits to include the black lines
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(ymin, ymax + 0.1 * ymax)

    # Add grid
    ax.grid(axis='y', linestyle='--')

    # Increase font size of axis labels and tick labels
    ax.set_xlabel('Sorting Algorithm', fontsize=12)
    ax.set_ylabel('Execution Time (seconds)', fontsize=12)
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)

    # Provide a clear legend
    ax.legend(bars, algorithms, loc='upper right', fontsize=10)

    plt.title(f'Sorting Algorithms Comparison for Array Size {size}', fontsize=14)

    plt.tight_layout()  # Adjust spacing
    plt.savefig(os.path.join(img_dir, f'b_Figure_{i+5}.png'))
    plt.close(fig)

# Display the figures
for i in range(len(array_sizes)):
    fig_path = os.path.join(img_dir, f'b_Figure_{i+5}.png')
    plt.figure(figsize=(8, 6))
    img = plt.imread(fig_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()