import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("../data/pulse_spectrum_over_time.csv")

frequencies = df.columns[:-1].astype(float)
times = df["Time"]
X, Y = np.meshgrid(frequencies, times)
Z = df.iloc[:, :-1].values

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection="3d")

cmap = plt.get_cmap("Blues")

for i in range(len(times)):
    x = frequencies
    y = times[i]
    z = Z[i]

    X_surface, Y_surface = np.meshgrid(x, [y, y])
    Z_surface = np.vstack([np.zeros_like(z), z])

    ax.plot_surface(
        X_surface,
        Y_surface,
        Z_surface,
        color=cmap(0.8),
        alpha=1.0,
        rstride=1,
        cstride=1,
        edgecolor="k",
    )

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Time (s)")
ax.set_zlabel("Amplitude")

plt.title("Waterfall plot of pulse spectrum over time")
plt.savefig("../images/q7-waterfall.png")
plt.show()
