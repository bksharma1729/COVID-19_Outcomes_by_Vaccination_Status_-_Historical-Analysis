# COVID-19_Outcomes_by_Vaccination_Status_-_Historical-Analysis
Analysis on dataset (for each analysis) 
4.1 COVID-19 Trends Over Time by Vaccination Status 
i. Introduction 
This part of the analysis focuses on how COVID-19 trends—specifically cases, 
hospitalizations, and deaths—have changed over time based on vaccination status. It 
helps us understand the effectiveness of vaccines in reducing the spread and severity of 
the virus. By comparing these outcomes across unvaccinated, vaccinated, and boosted 
groups, we can observe the impact of vaccination efforts over the course of the pandemic. 
ii. General Description 
The dataset contains weekly data showing rates of COVID-19 cases, hospitalizations, and 
deaths per 100,000 people for three groups: Unvaccinated, Vaccinated, and Boosted. 
These outcomes are recorded over a period of time, allowing us to track and compare 
trends. This time-based comparison provides insights into how different levels of 
vaccination protection affected health outcomes during different stages of the pandemic. 
iii. Specific Requirements, Functions and Tools 
The analysis was performed using Python, with the help of libraries like Pandas and 
Matplotlib. Key steps and techniques included: 
• Filtering the dataset to include only relevant outcomes (cases, hospitalizations, 
deaths) 
• Grouping the data by week and outcome using groupby() to calculate average 
rates 
• Plotting line graphs for each outcome over time for all vaccination statuses 
• Customizing each subplot for clear visual comparison 
iv. Analysis Results 
The results of the analysis show a clear difference in outcomes between vaccination 
groups. Unvaccinated individuals consistently had higher rates of cases, hospitalizations, 
and deaths across most weeks. Vaccinated individuals had lower rates, and boosted 
individuals showed the lowest rates throughout the timeline. 
This trend highlights the effectiveness of vaccines, especially booster shots, in reducing 
severe outcomes. It also supports public health efforts that encourage full vaccination and 
boosters as a key strategy in managing the impact of COVID-19 
v. Visualization 
4.2 Effectiveness of Vaccination in Reducing Severe Outcomes 
i. Introduction 
This analysis assesses how vaccination impacts the severity of COVID-19 outcomes, 
focusing on hospitalizations and deaths. The aim is to determine whether higher 
vaccination levels correlate with lower severe outcome rates. 
ii. General Description 
The dataset records weekly hospitalization and death rates by vaccination status—
 Unvaccinated, Vaccinated, and Boosted. This allows for a direct comparison of outcome 
severity across immunization levels. 
iii. Specific Requirements, Functions and Formulas 
Using Python (pandas, seaborn, matplotlib), we: 
• Filtered for severe outcomes (Hospitalizations, Deaths) 
• Calculated average rates per vaccination status 
• Reshaped data with melt() for visualization 
• Created a grouped bar chart using seaborn bar plot() 
These steps quantified and visually compared severity based on vaccination coverage. 
iv. Analysis Results 
Findings show a clear decline in severe outcome rates with increased vaccination. 
Unvaccinated individuals had the highest rates, while boosted individuals had the lowest. 
This pattern confirms the effectiveness of vaccines in reducing critical health risks. 
.v. Visualization 
4.3 Risk Reduction Analysis 
i. Introduction 
This analysis quantifies how vaccination reduces the risk of adverse health outcomes due 
to COVID-19. By calculating outcome rates per 100,000 population, the objective is to 
assess the relative risk for unvaccinated, vaccinated, and boosted individuals. 
ii. General Description 
The dataset includes weekly counts of outcomes and the respective population sizes for 
each vaccination group. Rates per 100,000 were computed to standardize comparisons 
across varying population sizes and identify patterns in outcome severity linked to 
vaccination status. 
iii. Specific Requirements, Functions and Formulas 
Using Python (pandas, matplotlib), the following steps were performed: 
• Rate Calculation: Outcome rates per 100,000 were computed for each vaccination 
group. 
• Aggregation: Average rates by outcome type were derived using groupby() and 
mean(). 
• Visualization: A multi-line chart was created to compare average rates across 
outcomes and vaccination statuses. 
Key functions used: 
• Mathematical operations for rate calculation 
• groupby() for structured aggregation 
• matplotlib.pyplot for custom line plotting 
iv. Analysis Results 
The analysis reveals that outcome rates consistently decline with increasing vaccination 
coverage. Unvaccinated individuals show the highest average risk, followed by 
vaccinated individuals, with boosted individuals having the lowest risk. This trend 
reinforces the role of vaccines in risk reduction. 
v. Visualization 
4.4 Age Group Vulnerability Analysis 
i. Introduction 
This analysis identifies which age groups are most affected by COVID-19 in terms of 
cases, hospitalizations, and deaths. 
ii. General Description 
The dataset contains outcome data segmented by age group and vaccination status. Total 
counts were calculated to assess vulnerability across demographics. 
iii. Specific Requirements, Functions and Formulas 
Using Python: 
• Filtered data by outcome type 
• Aggregated totals per age group 
• Created pie charts to show proportional impact 
Key functions: groupby(), sum(), and matplotlib.pyplot.pie(). 
iv. Analysis Results 
Results show younger groups report more cases, while older groups have higher shares of 
hospitalizations and deaths, confirming increased risk with age. 
v. Visualization 
4.5 Temporal Trends Analysis 
i. Introduction 
This analysis tracks weekly changes in COVID-19 cases to identify trends such as 
outbreak peaks, seasonal patterns, and the potential impact of vaccination or 
interventions. 
ii. General Description 
The dataset includes weekly case counts by vaccination status. By aggregating data over 
time, the analysis highlights how infection rates evolve across groups. 
iii. Specific Requirements, Functions and Formulas 
Using Python: 
• Converted week_end to datetime for proper time-series analysis 
• Grouped case data weekly 
• Used matplotlib.pyplot.plot() to visualize trends across vaccination 
categories 
Key functions: groupby(), sum(), and plot(). 
iv. Analysis Results 
The visualization reveals clear case surges during specific periods, with unvaccinated 
individuals consistently showing higher case counts. Vaccinated and boosted groups 
experience comparatively lower peaks, reflecting vaccine impact. 
v. Visualization 
4.6 Correlation Analysis of Deaths by Vaccination Status 
i. Introduction 
This analysis visualizes the correlation between vaccination status and COVID-19-related 
deaths to assess the relative burden among different population groups. 
ii. General Description 
The dataset includes cumulative death counts across unvaccinated, vaccinated, and 
boosted individuals. The aim is to show the proportional impact of each group on overall 
mortality. 
iii. Specific Requirements, Functions and Formulas 
Using Python: 
• Filtered for the “Deaths” outcome 
• Aggregated total deaths by vaccination status 
• Used a donut chart (a stylized pie chart) for visual clarity 
Key methods: sum(), matplotlib.pyplot.pie() with wedgeprops={'width': 0.4} 
for donut styling. 
iv. Analysis Results 
The visualization shows that unvaccinated individuals account for the highest proportion 
of deaths. This underlines the critical role of vaccination and booster doses in reducing 
fatality risk. 
v. Visualization 
4.7 Numerical Feature Trend Analysis 
i. Introduction 
This analysis visualizes the trends of key numerical metrics related to COVID-19 
outcomes and vaccination statistics across records, enabling pattern recognition and 
outlier detection. 
ii. General Description 
The dataset includes various numerical attributes such as outcome rates, population 
counts, and crude vaccination ratios. By tracking these values across records, the analysis 
uncovers underlying fluctuations and correlations. 
iii. Specific Requirements, Functions and Formulas 
Using Python: 
• Selected relevant numerical columns 
• Reshaped the data using melt() for long-form plotting 
• Utilized a multi-line chart for side-by-side trend visualization 
Key functions: melt(), plot() from matplotlib. 
iv. Analysis Results 
The line chart reveals distinct trends and relative movement of features such as infection 
rates and vaccination coverage. Some variables remain stable, while others fluctuate 
significantly, indicating areas needing further investigation. 
v. Visualization 
4.8 Outcome Rate Distribution Analysis Using Box Plots 
i. Introduction 
This analysis investigates the distribution of COVID-19 outcome rates across different 
vaccination statuses (unvaccinated, vaccinated, boosted) using statistical visualization. 
Box plots are employed to highlight central tendencies, variability, and outliers in the 
outcome rates across groups. 
ii. General Description 
The dataset contains COVID-19 outcome counts (cases, hospitalizations, deaths) 
alongside population sizes for each vaccination status. To fairly compare across groups, 
outcome rates are normalized per 100,000 individuals. The analysis reshapes the data to 
facilitate grouped box plot visualization and applies a log scale to accommodate varying 
rate magnitudes. 
iii. Specific Requirements, Functions and Formulas 
Using Python: 
• Calculated normalized outcome rates using the formula: 
rate = (outcome_count / population) * 100,000 
• Used melt() to reshape data from wide to long format for plotting 
• Visualized with seaborn.boxplot() and enhanced distribution clarity using 
seaborn.stripplot() 
• Applied logarithmic scaling with plt.yscale("log") to manage skewed distributions 
Key functions: melt(), boxplot(), stripplot(), yscale("log") 
iv. Analysis Results 
The resulting visualization reveals clear differences in outcome rate distributions among 
the three vaccination groups. Unvaccinated individuals exhibit significantly higher 
median and outlier rates across all outcomes. The log scale effectively captures both 
subtle variations and extreme values. Booster recipients show the most consistent and 
lowest risk levels, while unvaccinated groups display greater variability and frequent 
outliers —signaling elevated vulnerability and inconsistency. 
v. Visualization 
5. Conclusion: 
The exploratory data analysis of COVID-19 outcomes by vaccination status offers 
compelling insights into the trends, disparities, and effectiveness of vaccination efforts. 
Through a series of structured visualizations and statistical examinations, the following 
key conclusions emerged: 
• Vaccination Impact: Fully vaccinated and boosted individuals consistently show 
lower rates of cases, hospitalizations, and deaths compared to unvaccinated 
groups, validating the protective effect of vaccination. 
• Temporal Trends: Time-series analysis highlighted key periods of spikes and 
declines, often aligning with known variant waves or public health policy 
changes. 
• Data Quality: The dataset demonstrated high consistency and completeness, with 
only minimal missing values and no significant gaps in weekly reporting. 
• Distribution Patterns: Outcome rates show significant variability among 
unvaccinated populations, with broader distributions and higher outliers, 
emphasizing greater vulnerability and unpredictability. 
• Normalized Insights: By using age-adjusted and population-normalized metrics, 
the analysis ensured fairness in comparisons and revealed deeper patterns often 
obscured in raw counts. 
6. Future Scope: 
Future enhancements of this analysis could focus on expanding its analytical depth and 
interactivity. Incorporating predictive modelling techniques, such as time-series 
forecasting or classification models, would allow for estimating future case counts, 
hospitalization risks, or mortality probabilities across vaccination groups. This could 
support health agencies in preparing for potential surges. 
7. References: 
[1] Microsoft Excel Documentation: https://support.microsoft.com/en-us/excel.
