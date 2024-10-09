import numpy as np
import matplotlib.pyplot as plt


# Custom Epanechnikov KDE class
class EpanechnikovKDE:
    def __init__(self, bandwidth=1.0):
        self.bandwidth = bandwidth
        self.data = None

    def fit(self, data):
        """Fit the KDE model with the given data."""
        self.data = np.array(data)

    def epanechnikov_kernel(self, x, xi):
        """Epanechnikov kernel function."""
        if ((x - xi) / self.bandwidth) ** 2 <= 1:
            return 3 * (1 - ((x - xi) / self.bandwidth) ** 2) / 4
        return 0

    def evaluate(self, x):
        """Evaluate the KDE at point x."""
        vectorized_ep = np.vectorize(self.epanechnikov_kernel)
        if self.data is not None:
            return np.sum(vectorized_ep(x, self.data)) / (
                len(self.data) * self.bandwidth
            )
        return


# Load the data from the NPZ file
data_file = np.load("transaction_data.npz")
data = data_file["data"]

ep_kernel = EpanechnikovKDE(1)
ep_kernel.fit(data)

x = np.linspace(-20, 20, 100)
y = ep_kernel.evaluate(x)

# TODO: Initialize the EpanechnikovKDE class

# TODO: Fit the data

# TODO: Plot the estimated density in a 3D plot

# TODO: Save the plot
