# Objective 3: Outcome Rate Distribution Analysis Using Box Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Cleaned_Dataset.csv")

# Calculate outcome rates per 100k
df['rate_unvaccinated'] = (df['outcome_unvaccinated'] / df['population_unvaccinated']) * 100000
df['rate_vaccinated'] = (df['outcome_vaccinated'] / df['population_vaccinated']) * 100000
df['rate_boosted'] = (df['outcome_boosted'] / df['population_boosted']) * 100000

# Melt the dataframe for plotting
rate_df = df.melt(
    id_vars=['outcome'],
    value_vars=['rate_unvaccinated', 'rate_vaccinated', 'rate_boosted'],
    var_name='Vaccination_Status',
    value_name='Rate_per_100k'
)

# Format vaccination labels
rate_df['Vaccination_Status'] = rate_df['Vaccination_Status'].str.replace('rate_', '').str.capitalize()

# Plot
plt.figure(figsize=(8, 7))
sns.boxplot(
    data=rate_df,
    x='outcome',
    y='Rate_per_100k',
    hue='Vaccination_Status',
    palette='Set2',
    width=0.5
)

# Optional: add jittered points to show distribution
sns.stripplot(
    data=rate_df,
    x='outcome',
    y='Rate_per_100k',
    hue='Vaccination_Status',
    dodge=True,
    color='black',
    alpha=0.3,
    size=2,
    marker='.'
)

plt.yscale("log")  # handle extreme values
plt.title('Outcome Rate Distribution by Vaccination Status (Log Scale)', fontsize=14)
plt.xlabel('Health Outcome')
plt.ylabel('Rate per 100,000 (Log Scale)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='Vaccination Status', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
