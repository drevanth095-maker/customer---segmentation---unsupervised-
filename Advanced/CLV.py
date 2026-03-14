# Create a CLV score (health risk value proxy)
df["clv_score"] = (
    df["chol"] * 0.3 +
    df["bmi"] * 2 +
    df["trestbps"] * 0.2
)
df["clv_group"] = pd.qcut(df["clv_score"], q=3,
                          labels=["Low_Value", "Medium_Value", "High_Value"])
print("\nCustomer Lifetime Value Groups:\n")
clv_groups = df["clv_group"].value_counts()
print(clv_groups)
print("\nSample Data with New Columns:\n")
print(df[["age", "age_segment", "clv_score", "clv_group"]].head())
df.to_csv("segmented_heart_dataset.csv", index=False)
print("\nUpdated dataset saved as 'segmented_heart_dataset.csv'")
