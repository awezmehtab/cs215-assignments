import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./data/Student_Marks.csv")

plt.figure(figsize=(10, 6))
sns.violinplot(x='number_courses', y='time_study', data=df)
plt.title('Violin plot of time spent by number of courses taken')
plt.xlabel('Number of courses taken')
plt.ylabel('Average number of hours spent per day')
plt.savefig('./images/violin-plot.png')
plt.show()
