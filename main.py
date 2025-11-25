import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000
age = np.random.randint(18, 76, n)
income = np.random.normal(60, 15, n)
income = np.clip(income, 20, 150)
spending = income * 0.6 + np.random.normal(0, 10, n)
spending = np.clip(spending, 0, 100)

df = pd.DataFrame({
    "CustomerID": np.arange(1, n+1),
    "Age": age,
    "AnnualIncome_k": income,
    "MonthlySpendingScore": spending
})

df.to_csv("dataset.csv", index=False)
print("Dataset generated as dataset.csv")
