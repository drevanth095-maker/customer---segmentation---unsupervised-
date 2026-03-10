scaler = StandardScaler()

columns_to_scale = ['age','trestbps','chol','thalach','oldpeak','bmi']

df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

print("\nScaled Data Sample:")
print(df[columns_to_scale].head())
