from datetime import datetime
import pandas as pd

# Load raw dataset
df = pd.read_csv('ai_companies_raw.csv')

# Ensure columns are numeric (converts any rogue strings/letters to NaN numbers)
df['Market_Cap_USD_Billions'] = pd.to_numeric(
    df['Market_Cap_USD_Billions'], errors='coerce'
)
df['Model_Parameters_Billions'] = pd.to_numeric(
    df['Model_Parameters_Billions'], errors='coerce'
)
df['Annual_RD_Spend_USD_Millions'] = pd.to_numeric(
    df['Annual_RD_Spend_USD_Millions'], errors='coerce'
)

# Data Cleaning: Fill missing values with median
df['Market_Cap_USD_Billions'] = df['Market_Cap_USD_Billions'].fillna(
    df['Market_Cap_USD_Billions'].median()
)
df['Model_Parameters_Billions'] = df['Model_Parameters_Billions'].fillna(
    df['Model_Parameters_Billions'].median()
)

# Anomaly Detection: Flag extreme R&D spenders using Z-score
mean_rd = df['Annual_RD_Spend_USD_Millions'].mean()
std_rd = df['Annual_RD_Spend_USD_Millions'].std()
df['Z_Score'] = (df['Annual_RD_Spend_USD_Millions'] - mean_rd) / std_rd
df['Anomaly_Flag'] = df['Z_Score'].apply(
    lambda x: 'High Spender Anomaly' if abs(x) > 1.5 else 'Normal'
)

# Save processed data for Power BI
df.to_csv('processed_ai_data.csv', index=False)
print(
    f"Pipeline executed successfully at {datetime.now()}. Cleaned file saved."
)