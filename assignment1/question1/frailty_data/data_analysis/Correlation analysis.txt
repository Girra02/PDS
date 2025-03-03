# Convert categorical 'Frailty' to binary (0 = No, 1 = Yes)
df["Frailty"] = df["Frailty"].map({"N": 0, "Y": 1})
correlation_matrix = df.corr()
print("Correlation matrix:\n", correlation_matrix)
