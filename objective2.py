#To evaluate the effectiveness of vaccination in reducing severe outcomes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")
df["week_end"] = pd.to_datetime(df["week_end"])

# Filter severe outcomes
severe_outcomes = df[df["outcome"].isin(["Hospitalizations", "Deaths"])]

# Calculate average rates
avg_rates = severe_outcomes.groupby("outcome").agg({
    "unvaccinated_rate": "mean",
    "vaccinated_rate": "mean",
    "boosted_rate": "mean"
}).reset_index()

# Reshape for plotting
avg_rates = avg_rates.melt(
    id_vars="outcome",
    var_name="Vaccination_Status",
    value_name="Average_Rate"
)

# Plot
plt.figure(figsize=(7, 6))
sns.set(style="whitegrid")
sns.barplot(data=avg_rates, x="outcome", y="Average_Rate", hue="Vaccination_Status", palette="Set2")
plt.title("Comparison of Average Severe Outcome Rates by Vaccination Status", fontsize=14, fontweight='bold')
plt.ylabel("Average Rate per 100,000", fontsize=12)
plt.xlabel("Outcome", fontsize=12)
plt.legend(title="Vaccination Status", title_fontsize=11)
plt.tight_layout()
plt.show()
