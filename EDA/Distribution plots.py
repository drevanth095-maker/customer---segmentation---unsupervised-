sns.histplot(df['chol'], kde=True)
plt.title("Cholesterol Distribution")
plt.show()

sns.histplot(df['bmi'], kde=True)
plt.title("BMI Distribution")
plt.show()
