import pandas as pd

# Load the Excel file
try:
    df = pd.read_excel('Supernova-no-duplicates-dataset.xlsx')
    print("Supernova dataset loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print("Error: Supernova-no-duplicates-dataset.xlsx not found. Make sure the file is in the correct directory.")
    exit()

print("\nDataFrame Info:")
df.info()

print("\nDescriptive Statistics:")
print(df.describe(include='all'))

# Check unique values in 'insured_address_state'
print("\nUnique values in 'insured_address_state':")
print(df['insured_address_state'].unique())

# Check unique values in 'Category'
print("\nUnique values in 'Category':")
print(df['Category'].unique())

# Delete the 'vlookup for column P' column
df = df.drop(columns=['vlookup for column P'])

# Print the updated DataFrame info to confirm the column is gone
print("\nDataFrame Info after deleting 'vlookup for column P':")
df.info()

# Print the first few rows of the updated DataFrame
print("\nFirst 5 rows after deleting the column:")
print(df.head())

print("\nAll Remaining Column Names:")
print(df.columns.tolist())

# Print all column names for review
print("\nAll Remaining Column Names (Again):")
print(df.columns.tolist())

# Trim whitespace from object (string) columns
object_cols = df.select_dtypes(include='object').columns
for col in object_cols:
    df[col] = df[col].str.strip()
    print(f"Whitespace trimmed from column: {col}")

# Print the unique values of the object columns again to confirm
print("\nUnique values in 'insured_address_state' after trimming:")
print(df['insured_address_state'].unique())

print("\nUnique values in 'Category' after trimming:")
print(df['Category'].unique())

# Rename columns for better readability in Tableau (no abbreviations or acronyms)
df = df.rename(columns={
    'insured_address_state': 'Insured Address State/Province',
    'input_gl_revenue': 'General Liability Revenue (Input)',
    'input_gl_employee': 'General Liability Employees (Input)',
    'input_gl_gl_limit': 'General Liability Limit (Input)',
    'input_gl_gl_deductible': 'General Liability Deductible (Input)',
    'input_property_bldg_limit': 'Property Building Limit (Input)',
    'input_property_num_claims': 'Property Number of Claims (Input)',
    'input_property_town_grade': 'Property Town Grade (Input)',
    'input_property_content_limit': 'Property Content Limit (Input)',
    'input_property_bldg_deductible': 'Property Building Deductible (Input)',
    'input_property_cont_deductible': 'Property Content Deductible (Input)',
    'input_property_construction_class': 'Property Construction Class (Input)',
    'output_premium_crime_prem': 'Crime Premium (Output)',
    'output_premium_eq_premium': 'Earthquake Premium (Output)',
    'output_premium_ebi_premium': 'Extra Business Interruption Premium (Output)',
    'output_premium_bldg_premium': 'Building Premium (Output)',
    'output_premium_flood_premium': 'Flood Premium (Output)',
    'output_premium_content_premium': 'Content Premium (Output)',
    'output_premium_on_prem_gl_prem': 'General Liability On-Premises Premium (Output)',
    'output_premium_products_gl_prem': 'General Liability Products Premium (Output)',
    'output_premium_business_interuption_prem': 'Business Interruption Premium (Output)',
    'output_premium_total_total_prem': 'Total Premium (Output)'
})

# Print the updated column names
print("\nUpdated Column Names (No Abbreviations):")
print(df.columns.tolist())

# Print the first few rows with the new column names
print("\nFirst 5 rows with updated column names (No Abbreviations):")
print(df.head())

# Save the cleaned DataFrame to a CSV file
df.to_csv('supernova_cleaned.csv', index=False)
print("\nCleaned data saved to supernova_cleaned.csv")
