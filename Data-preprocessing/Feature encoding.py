df = pd.get_dummies(df, columns=['cp','thal','slope'], drop_first=True)

print("\nAfter Encoding:")
print(df.head())
