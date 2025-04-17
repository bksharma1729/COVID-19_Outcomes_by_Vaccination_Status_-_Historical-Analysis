#Objective 1:
#To analyze COVID-19 trends over time across different vaccination statuses
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cleaned_Dataset.csv")
df["week_end"] = pd.to_datetime(df["week_end"])

outcomes = ["Cases", "Hospitalizations", "Deaths"]
df_filtered = df[df["outcome"].isin(outcomes)]

trend_data = df_filtered.groupby(["week_end", "outcome"]).agg({
    "unvaccinated_rate": "mean",
    "vaccinated_rate": "mean",
    "boosted_rate": "mean"
}).reset_index()

plt.figure(figsize=(8, 5))
for i, outcome in enumerate(outcomes):
    plt.subplot(3, 1, i + 1)
    subset = trend_data[trend_data["outcome"] == outcome]
    plt.plot(subset["week_end"], subset["unvaccinated_rate"], label="Unvaccinated", color="red")
    plt.plot(subset["week_end"], subset["vaccinated_rate"], label="Vaccinated", color="blue")
    plt.plot(subset["week_end"], subset["boosted_rate"], label="Boosted", color="green")
    plt.title(f"{outcome} Rate Over Time by Vaccination Status")
    plt.xlabel("Week End")
    plt.ylabel("Rate per 100k")
    plt.legend()
    plt.tight_layout()

plt.show()
