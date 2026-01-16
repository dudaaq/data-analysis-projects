import matplotlib.pyplot as plt
from utils import load_data, save_plot


df = load_data()
Age_counts = df["Age"].value_counts().sort_index()

print("Age distribution: ")
print(Age_counts)

plt.figure()
Age_counts.plot(kind="bar")
plt.title("Age Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")

save_plot("age_distribution.png")
