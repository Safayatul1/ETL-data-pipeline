import pandas as pd
import matplotlib.pyplot as plt

# Load the insurance data
df = pd.read_csv('insurance.csv')

# Step 1: Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Step 2: Fill missing values
df_cleaned = df_cleaned.fillna({
    'age': df_cleaned['age'].median(),
    'sex': df_cleaned['sex'].mode()[0],
    'bmi': df_cleaned['bmi'].mean(),
    'children': df_cleaned['children'].median(),
    'smoker': df_cleaned['smoker'].mode()[0],
    'region': df_cleaned['region'].mode()[0],
    'charges': df_cleaned['charges'].mean()
})

# Step 3: (Optional) If you had a date column, you'd fix it like this:
# df_cleaned['claim_date'] = pd.to_datetime(df_cleaned['claim_date'], errors='coerce')

# Step 4: Save the cleaned data
df_cleaned.to_csv('cleaned_insurance.csv', index=False)

# Step 5: Create visualizations

# Bar chart: Number of people per region
plt.figure(figsize=(10, 5))
df_cleaned['region'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Number of Insurance Policyholders by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('region_distribution.png')
plt.close()

# Bar chart: Average charges for smokers vs non-smokers
plt.figure(figsize=(10, 5))
df_cleaned.groupby('smoker')['charges'].mean().plot(kind='bar', color='salmon')
plt.title('Average Charges for Smokers vs Non-Smokers')
plt.xlabel('Smoker')
plt.ylabel('Average Charges')
plt.tight_layout()
plt.savefig('smoker_charges.png')
plt.close()
