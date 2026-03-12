print("\nSummary Statistics")
print(df.describe())

plt.hist(df['age'], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.countplot(x='heart_disease', data=df)
plt.title("Heart Disease Count")
plt.show()
