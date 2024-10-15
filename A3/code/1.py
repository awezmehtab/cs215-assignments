from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt

filename=list(uploaded.keys())[0]

header=pd.read_csv(io.BytesIO(uploaded[filename]),skiprows=12, nrows=1)
#print(header)
df= pd.read_csv(io.BytesIO(uploaded[filename]), skiprows=13, nrows=1500)
#print(df.iloc[10,6])
# Assuming the 7th column is the 6th index (since indexing starts at 0)
filtered_df = df[df.iloc[:, 6] < 4]



# Extract the data for the histogram (7th column)
data = filtered_df.iloc[:, 6].dropna()  # Drop NaN values for the histogram

plt.figure(1)
plt.hist(data, bins=10)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Filtered Data (10 Bins)")

# Calculate estimated probabilities for each bin
hist, bin_edges = np.histogram(data, bins=10, density=False)  # Get the counts in each bin

# Calculate total number of data points in the histogram
total_data_points = len(data)

# Calculate the probability for each bin (p_j = count_j / total_data_points)
p_j = hist / total_data_points

# Print the probabilities for each bin
for i in range(len(p_j)):
    print(f"Bin {i+1} [{bin_edges[i]:.2f}, {bin_edges[i+1]:.2f}]: p_j = {p_j[i]:.4f}")

plt.show()
plt.savefig("10binhistogram.png")








plt.figure(2)
n = len(data)  # Number of data points
cv_scores = []
bin_widths = []

for num_bins in range(1, 1001):
    h = (data.max() - data.min()) / num_bins  # Bin width
    hist, bin_edges = np.histogram(data, bins=num_bins, density=True)
    estimated_probabilities = hist * np.diff(bin_edges)

    cv_score = (2 / ((n - 1) * h)) - (((n + 1) / ((n - 1) * h)) * np.sum(estimated_probabilities**2))

    cv_scores.append(cv_score)
    bin_widths.append(h)

# Plot the cross-validation scores
plt.plot(bin_widths, cv_scores)
plt.xlabel("Bin Width (h)")
plt.ylabel("Cross-Validation Score (Jˆ(h))")
plt.title("Cross-Validation Score vs. Bin Width")

# Save the plot


plt.show()
plt.savefig("crossvalidation.png")

# Find the index of the minimum cross-validation score
optimal_idx = np.argmin(cv_scores)

# Get the optimal bin width
optimal_bin_width = bin_widths[optimal_idx]

# Print the optimal bin width
print(f"The optimal bin width (bandwidth) is: {optimal_bin_width}")

# Calculate the number of bins
data_range = data.max() - data.min()
num_bins = int(data_range / optimal_bin_width)

# Plot the histogram with the specified bin width
plt.figure(1)
plt.hist(data, bins=num_bins)  # setting the range explicitly
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title(f"Histogram with Bin Width {optimal_bin_width}")

# Calculate estimated probabilities for each bin
hist, bin_edges = np.histogram(data, bins=num_bins, range=(data.min(), data.min() + data_range), density=True)

# Show the plot
plt.show()
plt.savefig("optimalhistogram.png")
