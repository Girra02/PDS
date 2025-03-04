# 1. Histogram of Grip Strength
plt.figure(figsize=(8,5))
sns.histplot(df["Grip strength"], bins=5, kde=True)
plt.title("Distribution of Grip Strength")
plt.xlabel("Grip Strength (kg)")
plt.ylabel("Count")
plt.savefig("/content/histogram_grip_strength.png")
plt.show()

# 2. Heatmap correlation
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.savefig("/content/heatmap_correlation.png")
plt.show()
