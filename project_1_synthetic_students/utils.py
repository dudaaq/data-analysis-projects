import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path 


Base_Dir = Path(__file__).resolve().parent

Data_Path = Base_Dir/ "data" / "students.csv"
OutPut_Dir = Base_Dir / "outputs"
OutPut_Dir.mkdir(parents=True, exist_ok=True)

def load_data():
    return pd.read_csv(Data_Path, sep=";")

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(OutPut_Dir / filename)
    plt.close()

