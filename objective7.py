# Objective 7: 
# ➤Line chart to visualize trends in numerical features across records.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")

# Select only numerical columns
numerical_cols = [
    'unvaccinated_rate', 'vaccinated_rate', 'boosted_rate',
    'crude_vaccinated_ratio', 'crude_boosted_ratio',
    'population_unvaccinated', 'population_vaccinated', 'population_boosted',
    'outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted'
]

# Create a long-form DataFrame for plotting
df_long = df[numerical_cols].reset_index().melt(id_vars="index", var_name="Feature", value_name="Value")

# Plot line chart
plt.figure(figsize=(8, 8))
for feature in df_long["Feature"].unique():
    subset = df_long[df_long["Feature"] == feature]
    plt.plot(subset["index"], subset["Value"], label=feature)

plt.title("Line Chart of Numerical Features Across Records")
plt.xlabel("Record Index")
plt.ylabel("Value")
plt.legend(loc="upper right", bbox_to_anchor=(1.15, 1))
plt.tight_layout()
plt.show()
