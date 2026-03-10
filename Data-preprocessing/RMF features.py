# Recency
df['recency'] = df['age'].max() - df['age']

# Frequency
df['frequency'] = df['exang'] + df['fbs']

# Monetary
df['monetary'] = df['trestbps'] + df['chol']
#Behavioral Features
df['lifestyle_risk'] = df['smoking'] + df['diabetes']
df['exercise_risk'] = df['exang'] + df['oldpeak']
