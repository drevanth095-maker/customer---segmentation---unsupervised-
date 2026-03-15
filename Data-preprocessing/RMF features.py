# Recency
df['recency'] = df['age'].max() - df['age']
df['frequency'] = df['exang'] + df['fbs']
df['monetary'] = df['trestbps'] + df['chol']
df['lifestyle_risk'] = df['smoking'] + df['diabetes']
df['exercise_risk'] = df['exang'] + df['oldpeak']
df['chol_bmi_ratio'] = df['chol'] / df['bmi']
df['bp_bmi_ratio'] = df['trestbps'] / df['bmi']
