import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")

# Step 1: Calculate outcome rates per 100,000
df['rate_unvaccinated'] = (df['outcome_unvaccinated'] / df['population_unvaccinated']) * 100000
df['rate_vaccinated'] = (df['outcome_vaccinated'] / df['population_vaccinated']) * 100000
df['rate_boosted'] = (df['outcome_boosted'] / df['population_boosted']) * 100000

# Step 2: Group by outcome and compute mean rates
risk_df = df.groupby('outcome')[
    ['rate_unvaccinated', 'rate_vaccinated', 'rate_boosted']
].mean().reset_index()

# Step 3: Line Plot
plt.figure(figsize=(8, 6))

# Plot each line manually for full control
plt.plot(risk_df['outcome'], risk_df['rate_unvaccinated'], marker='o', label='Unvaccinated', color='red')
plt.plot(risk_df['outcome'], risk_df['rate_vaccinated'], marker='o', label='Vaccinated', color='blue')
plt.plot(risk_df['outcome'], risk_df['rate_boosted'], marker='o', label='Boosted', color='green')

# Enhancing the chart
plt.title('Average Outcome Rates per 100,000 by Vaccination Status', fontsize=14)
plt.xlabel('Health Outcome')
plt.ylabel('Avg Outcome Rate per 100k')
plt.grid(True)
plt.legend(title='Vaccination Status')
plt.tight_layout()
plt.show()
