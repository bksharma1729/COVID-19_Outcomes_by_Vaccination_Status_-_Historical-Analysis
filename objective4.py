#Objective 5: Age Group Vulnerability Analysis   
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")
# Step 1: Filter data for each outcome type
cases_df = df[df['outcome'] == 'Cases'].groupby('age_group')[['outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted']].sum()
hospital_df = df[df['outcome'] == 'Hospitalizations'].groupby('age_group')[['outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted']].sum()
deaths_df = df[df['outcome'] == 'Deaths'].groupby('age_group')[['outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted']].sum()

# Step 2: Total outcomes per age group for each type
cases_df['Total_Cases'] = cases_df.sum(axis=1)
hospital_df['Total_Hosp'] = hospital_df.sum(axis=1)
deaths_df['Total_Deaths'] = deaths_df.sum(axis=1)

# Step 3: Plotting
fig, axes = plt.subplots(1, 3, figsize=(8, 6))

# Pie chart for Cases
axes[0].pie(cases_df['Total_Cases'], labels=cases_df.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
axes[0].set_title('Cases by Age Group')

# Pie chart for Hospitalizations
axes[1].pie(hospital_df['Total_Hosp'], labels=hospital_df.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set2.colors)
axes[1].set_title('Hospitalizations by Age Group')

# Pie chart for Deaths
axes[2].pie(deaths_df['Total_Deaths'], labels=deaths_df.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
axes[2].set_title('Deaths by Age Group')

plt.suptitle('Distribution of Outcomes by Age Group', fontsize=16)
plt.tight_layout()
plt.show()
