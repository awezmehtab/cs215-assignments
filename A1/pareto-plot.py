import pandas as pd
import matplotlib.pyplot as plt

complaint_data = pd.read_csv("./data/Restaurant-Complaints")
complaint_data = complaint_data.sort_values(by="count", ascending=False)
complaint_data["Cumulative Percentage"] = (
    complaint_data["count"].cumsum() / complaint_data["count"].sum() * 100
)
fig, ax1 = plt.subplots()

ax1.bar(complaint_data["complaint"], complaint_data["count"], color="C0")
ax1.set_xlabel("complaint")
ax1.set_ylabel("count", color="C0")
ax1.tick_params(axis="y", labelcolor="C0")

ax2 = ax1.twinx()
ax2.plot(
    complaint_data["complaint"],
    complaint_data["Cumulative Percentage"],
    color="C1",
    marker="o",
)
ax2.set_ylabel("cumulative %", color="C1")
ax2.tick_params(axis="y", labelcolor="C1")

plt.xticks(rotation=45, ha="right")
plt.title("Complaints by customers of a restaurant")
plt.tight_layout()
plt.savefig("./images/pareto-plot.png")
plt.show()
