import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
data = pd.read_csv("../data/Restaurant-Complaints.csv")
data = data.sample(frac=1, random_state=42).reset_index(drop=True)

complaints = data["complaint"]
counts = data["count"]

n = len(complaints)
angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
angles += angles[:1]

counts = counts.tolist()
counts += counts[:1]

colors = plt.cm.viridis(np.linspace(0, 1, n))

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

for i in range(n):
    ax.bar(
        x=angles[i],
        height=counts[i],
        width=2 * np.pi / n,
        color=colors[i],
        edgecolor="black",
        align="edge",
    )

ax.set_xticks(angles[:-1])
ax.set_xticklabels(complaints)

ax.set_yticklabels([])
ax.yaxis.grid(False)
ax.spines["polar"].set_visible(False)
plt.title("Complaints from customers in a restaurant")
plt.savefig("./images/coxcomb.png")
plt.show()
