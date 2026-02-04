import pandas as pd
import numpy as np

# Load CSV
df = pd.read_csv("sales_10000.csv")

# Create random ratings: 1.0 to 5.0, step 0.5
df["sales_rating"] = (
    np.clip(
        np.random.normal(loc=4.3, scale=0.5, size=len(df)),
        1, 5
    )
    .round(1)
)

# Save back to CSV (overwrite or new file)
df.to_csv("sales_10000_rate.csv", index=False)


