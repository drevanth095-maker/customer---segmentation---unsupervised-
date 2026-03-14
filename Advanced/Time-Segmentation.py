import pandas as pd
df = pd.read_csv("heart_disease_dataset.csv")

print("First 5 rows of dataset:\n")
print(df.head())
#  Time-Based Segmentation
bins = [0, 40, 55, 70, 100]
labels = ["Young", "Middle_Age", "Senior", "Elderly"]
df["age_segment"] = pd.cut(df["age"], bins=bins, labels=labels)
print("\nTime-Based Segmentation (Age Groups):\n")
age_segmentation = df["age_segment"].value_counts()
print(age_segmentation)
