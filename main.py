import pandas as pd

try:
    df_male = pd.read_csv("oscar_age_male.csv")
    df_female = pd.read_csv("oscar_age_female.csv")
except FileNotFoundError:
    print("Файл не найден!")
    exit(-1)

min_5_male = df_male.sort_values(["Age"]).head(5)
print(f"5 самых младших лауреатов среди мужчин\n{min_5_male}")

min_5_female = df_female.sort_values(["Age"]).tail(5)
print(f"5 самых старших лауреатов среди женщин\n{min_5_female}")

merged_tables = pd.concat([min_5_male, min_5_female])
median_age = merged_tables["Age"].median()
print(f"Медианный возраст: {median_age}")

merged_tables = pd.concat([df_male, df_female])
max_reward_age = merged_tables["Age"].mode().tail(1).values[0]
print(f"Возраст, при котором было получено максимальное количество наград: {max_reward_age}")

max_rewarded_artist = merged_tables["Name"].mode().tail(1).values[0]
print(f"Актёр, который получил максимальное количество наград: {max_rewarded_artist}")
