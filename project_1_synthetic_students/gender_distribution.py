import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

Base_dir = Path(__file__).resolve().parent
Data_Path = Base_dir / "data" / "students.csv"
Output_dir = Base_dir / "outputs"
Output_dir.mkdir(exist_ok=True)

df = pd.read_csv(Data_Path, sep=";")

gender_counts = df["Gender"].value_counts()

print("Gender distribution: ")
print(gender_counts)

plt.figure()
gender_counts.plot(kind="bar")
plt.title("Gender Distribution of students")
plt.xlabel("Gender")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig(Output_dir/ "gender_distribution.png")
plt.close()