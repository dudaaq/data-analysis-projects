import matplotlib.pyplot as plt
from utils import load_data, save_plot


df = load_data()
gender_counts = df["Gender"].value_counts()

print("Gender distribution: ")
print(gender_counts)

plt.figure()
gender_counts.plot(kind="bar")
plt.title("Gender Distribution of students")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

save_plot("gender_distribuition.png")