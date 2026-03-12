plt.figure(figsize=(10,8))

corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()
