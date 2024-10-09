import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


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

        new_x = (x - xi) / self.bandwidth
        norms = np.sum(new_x**2, axis=-1)
        mask = norms <= 1
        return np.where(mask, 3 * (1 - norms) / 4, 0)

    def evaluate(self, x):
        """Evaluate the KDE at point x."""
        if self.data is None:
            return np.array([])

        xn = np.expand_dims(x, axis=1)
        datan = np.expand_dims(self.data, axis=0)
        kernel_eval = self.epanechnikov_kernel(xn, datan)
        return np.sum(kernel_eval, axis=-1) / (self.bandwidth * len(self.data))


# Load the data from the NPZ file
data_file = np.load("transaction_data.npz")
data = data_file["data"]

# TODO: Initialize the EpanechnikovKDE class

ep_kernel = EpanechnikovKDE(1)

# TODO: Fit the data

ep_kernel.fit(data)

# TODO: Plot the estimated density in a 3D plot

x = np.linspace(-6, 6, 60)
y = np.linspace(-6, 6, 60)
xg, yg = np.meshgrid(x, y)

input = np.column_stack([xg.ravel(), yg.ravel()])
print(input.shape)
density = ep_kernel.evaluate(input).reshape(xg.shape)
print(density.shape)

fig = plt.figure(dpi=300)
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(xg, yg, density, cmap="viridis")

# plt.show()


# TODO: Save the plot

plt.savefig("transaction_distribution.jpg")
