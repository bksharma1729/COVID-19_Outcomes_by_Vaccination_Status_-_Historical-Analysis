COVID-19 Outcomes by Vaccination Status – Historical Analysis


📌 Project Overview

This project analyzes how COVID-19 cases, hospitalizations, and deaths differ based on vaccination status over time.

The main objective is to evaluate the effectiveness of vaccination — including booster doses — in reducing infection severity and mortality risk.

The analysis is based on weekly COVID-19 data categorized into:

Unvaccinated

Fully Vaccinated

Boosted

All comparisons use rates per 100,000 people to ensure fair and standardized analysis.

🎯 Project Goals

Compare COVID-19 outcomes across vaccination groups

Identify trends over time

Measure risk reduction due to vaccination

Analyze age-related vulnerability

Examine distribution patterns and variability

🛠 Tools & Libraries

Python

Pandas – Data cleaning and aggregation

Matplotlib – Data visualization

Seaborn – Statistical visualization

📊 What Was Analyzed
1️⃣ Trends Over Time

Weekly cases, hospitalizations, and deaths were plotted.

Unvaccinated individuals consistently showed higher rates.

Boosted individuals showed the lowest outcome rates.

2️⃣ Severe Outcome Comparison

Focused on hospitalizations and deaths.

Calculated average rates per vaccination group.

Found clear reduction in severity with increased vaccination.

3️⃣ Risk Reduction Calculation

Outcome rates were standardized using:

rate = (outcome_count / population) × 100,000

Risk consistently decreased from:
Unvaccinated → Vaccinated → Boosted

4️⃣ Age Group Vulnerability

Younger groups recorded more cases.

Older groups had higher hospitalization and death rates.

Confirms increased severity risk with age.

5️⃣ Distribution Analysis

Box plots showed higher variability and extreme values among unvaccinated groups.

Boosted individuals had lower and more stable outcome rates.

✅ Key Findings

Vaccination significantly reduces severe COVID-19 outcomes.

Booster doses provide the strongest protection.

Unvaccinated populations face higher risk and greater variability.

Time-series analysis highlights clear outbreak waves.

🚀 Future Improvements

Time-series forecasting models

Machine learning for risk prediction

Interactive dashboards (e.g., Plotly or Streamlit)

Advanced statistical modeling

📂 How to Run

Clone the repository

Install required libraries:

pip install pandas matplotlib seaborn

Run the analysis scripts or Jupyter Notebook
