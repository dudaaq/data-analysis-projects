import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

Base_Dir = Path(__file__).resolve().parent
Data_Path = Base_Dir / "data" / "students.csv"
Output_Dir = Base_Dir / "outputs"
Output_Dir.mkdir(exist_ok=True)

df = pd.read_csv(Data_Path, sep = ";")
Age_counts = df["Age"].value_counts()

print("Age distribution: ")
print(Age_counts)

plt.figure()
Age_counts.plot(kind="bar")
plt.title("Gender Distribution of Students")
plt.xlabel("Age")
plt.ylabel("Number of Students")