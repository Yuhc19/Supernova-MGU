- Premium analysis data cleaning log - raw_data.csv

1. Applied conditional formatting, alternating colors.
2. Applied conditional formatting to highlight missing values.
3. Removed duplicate records, Remaining 180 records out of 211.
4. Replaced 'Quebec (French)' with 'Quebec (American English)'.
5. Formatted Columns 'O' - 'X' to currency data type.
6. Formatted Columns 'D', 'F', 'G', 'K', 'L' and 'M' to currency data type.
7. Formatted text alignment 'Left'.
8. Sorted 'Category' column ('C') A>Z.
9. 4 null values detected on column 'P' ("output_premium_eq_premium") to be replaced with "0" per leadership instruction.
10. Created new clean data set before visualizations: Supernova-no-duplicates-dataset - raw_data.csv.

Assumptions:

1. Duplicate records removed.
2. Created an ID column to have a unique identifiable key. Numbered, 1 - 179.

Visualizations for premium analysis: Tableau.


- Decline rate analysis data cleaning log - decline_data.csv

1. Replaced blank fields with "Missing", column 'B'.
2. Deleted empty rows.
3. Froze first row, for headers.
4. Turned into 'Table'.
5. Exported table into Excel file.

Assumptions:

1. '0' means policy not rejected, '1' means policy rejected.

Visualization for Decline analysis: Tableau.

-LLM Results accuracy analysis- llm_results_processed.csv

1. Created new column 'Accurate', it will contain integer values, '1' for confirmation of accuracy and '0' for inaccuracy detected.
2. Turned data into 'Table'.
3. Deleted rows 58 - 1000.
4. Wrapped text on column G for readability.
5. Renamed 'Table' to 'LLM Results'.
6. Text alignment 'Top', 'Left'.


Assumptions:

1. Category = alert checking.
2. "N" = 'No'.
3. Crime rate, lower value = 'safer', higher value = 'higher risk of crime'.
4. For presentation, sample of 2 accurate and 2 inaccurate.

Instructions:

1. Paste business name and address, look at google search results
2. Read what the business is about, what they do, check 'data' field for matching.




















