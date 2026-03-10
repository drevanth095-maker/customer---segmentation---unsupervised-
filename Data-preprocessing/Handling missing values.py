# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# If missing values exist, fill them
df = df.fillna(df.median(numeric_only=True))
