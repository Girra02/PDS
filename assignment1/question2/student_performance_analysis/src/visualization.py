# Visualization 1: Distribution of Math Scores
plt.figure(figsize=(8, 6))
plt.hist(df['math score'], bins=15, edgecolor='black', alpha=0.7)
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Math Scores")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 2: Boxplot of Scores by Gender
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='gender', y='math score')
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.title("Boxplot of Math Scores by Gender")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 3: Average Scores by Test Preparation Course
avg_scores = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()

# Plot the average scores
avg_scores.plot(kind='bar', figsize=(10, 6), edgecolor='black', alpha=0.7)
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.title("Average Scores by Test Preparation Course")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization 4: Scatter Plot of Math vs. Reading Scores
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='math score', y='reading score', alpha=0.6)
plt.xlabel("Math Score")
plt.ylabel("Reading Score")
plt.title("Scatter Plot of Math vs. Reading Scores")
plt.grid(linestyle='--', alpha=0.7)
plt.show()

# Visualization 5: Count Plot of Parental Education Level
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='parental level of education', 
              order=df['parental level of education'].value_counts().index)
plt.xlabel("Number of Students")
plt.ylabel("Parental Level of Education")
plt.title("Count of Students by Parental Education Level")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()
