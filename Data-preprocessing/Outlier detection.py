Q1 = df['chol'].quantile(0.25)
Q3 = df['chol'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Lower Limit:", lower)
print("Upper Limit:", upper)

# Cap outliers
df['chol'] = np.where(df['chol'] > upper, upper, df['chol'])
df['chol'] = np.where(df['chol'] < lower, lower, df['chol'])
