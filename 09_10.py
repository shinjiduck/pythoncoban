import pandas as pd

ds_khach = [
    {"ten": "Nam", "quoc_gia": "Vietnam", "tong_chi": 45},
    {"ten": "John", "quoc_gia": "USA", "tong_chi": 12},
    {"ten": "Anna", "quoc_gia": "Germany", "tong_chi": 30},
    {"ten": "Mike", "quoc_gia": "USA", "tong_chi": 25}
]

df = pd.DataFrame(ds_khach)
print(df)
df[df["tong_chi"] > 20]
df.groupby("quoc_gia")["tong_chi"].sum()