#Objective 6: Correlation Analysis by using a donut chart (a stylized pie chart) to illustrate the relative contribution of outcome types across vaccination statuses.import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Load the dataset
df = pd.read_csv("Cleaned_Dataset.csv")
# Step 1: Filter for 'Deaths' and sum outcomes across all age groups and weeks
death_totals = df[df['outcome'] == 'Deaths'][[
    'outcome_unvaccinated', 'outcome_vaccinated', 'outcome_boosted'
]].sum()

# Step 2: Labels and colors
labels = ['Unvaccinated', 'Vaccinated', 'Boosted']
colors = ['#ff9999','#66b3ff','#99ff99']

# Step 3: Donut Chart
plt.figure(figsize=(8, 8))
wedges, texts, autotexts = plt.pie(death_totals, labels=labels, autopct='%1.1f%%',
                                   startangle=140, colors=colors, wedgeprops={'width': 0.4})
plt.title('Proportion of Deaths by Vaccination Status', fontsize=14)
plt.tight_layout()
plt.show()
