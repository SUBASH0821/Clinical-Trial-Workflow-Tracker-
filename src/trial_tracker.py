import pandas as pd
from utils import check_compliance

# Load clinical trial site data
df = pd.read_csv("../data/trial_sites.csv")

print("Clinical Trial Site Overview\n")
print(df)

print("\nCompliance Check Report\n")
for _, row in df.iterrows():
    status = check_compliance(row)
    print(f"Site {row['Site_ID']} - {row['Site_Name']}: {status}")
