import pandas as pd


df = pd.read_csv(
    "C:/Users/Souljah_Pc/Desktop/miuul/Veri Bilimi için Python Programlama/pythonProgramlama/"
    "python_for_data_science/data_analysis_with_python/datasets/breast_cancer.csv"
    )
df = df.iloc[:, 1: -1]
num_cols = [i for i in df.columns if df[i].dtype in ['int64', 'float64']]

corr_matrix = df[num_cols].corr().abs()
print(corr_matrix)

