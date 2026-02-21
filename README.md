COVID-19 Outcomes by Vaccination Status – Historical Analysis
***Overview***

This project analyzes COVID-19 cases, hospitalizations, and deaths based on vaccination status:

Unvaccinated

Fully Vaccinated

Boosted

The goal is to evaluate how vaccination impacts infection severity and risk over time using normalized rates (per 100,000 population).

🛠 Tools Used

Python

Pandas

Matplotlib

Seaborn

📊 Key Analyses
1️⃣ Trends Over Time

Compared weekly cases, hospitalizations, and deaths.

Unvaccinated individuals consistently showed higher rates.

Boosted individuals showed the lowest rates.

2️⃣ Severe Outcome Comparison

Focused on hospitalizations and deaths.

Clear reduction in severity with increased vaccination.

3️⃣ Risk Reduction

Calculated standardized rates:

rate = (outcome_count / population) * 100000

Risk decreases from Unvaccinated → Vaccinated → Boosted.

4️⃣ Age Vulnerability

Younger groups: higher case counts.

Older groups: higher hospitalization and death rates.

5️⃣ Distribution Analysis

Box plots show:

Greater variability and outliers among unvaccinated groups.

More stable and lower rates among boosted individuals.

✅ Key Findings

Vaccination significantly reduces severe outcomes.

Booster doses provide the strongest protection.

Unvaccinated populations show higher risk and variability.

Time-series trends align with major outbreak waves.

🚀 Future Improvements

Time-series forecasting

Machine learning risk prediction

Interactive dashboards
