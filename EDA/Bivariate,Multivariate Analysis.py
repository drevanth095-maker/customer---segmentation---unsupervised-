#--Brative analysis--
sns.boxplot(x='heart_disease', y='age', data=df)
plt.title("Age vs Heart Disease")
plt.show()

sns.boxplot(x='heart_disease', y='chol', data=df)
plt.title("Cholesterol vs Heart Disease")
plt.show()
#---Multivariate analysis---
sns.pairplot(df[['age','chol','trestbps','thalach','bmi','heart_disease']],
             hue='heart_disease')
plt.show()
