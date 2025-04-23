# Supernova MGU Analysis

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ## Overview

This project focuses on the cleaning and preparation of a supernova dataset obtained by Supernova MGU. The goal is to transform the raw data into a clean and structured format suitable for creating insightful visualizations using Tableau.

## Goals

The primary objectives of this project include:

- **Loading and Inspecting the Data:** Utilizing Python and the pandas library to load the dataset and understand its initial structure and contents.
- **Data Cleaning:** Identifying and handling any inconsistencies, missing values (though none were found in this dataset), and irrelevant information. This included the removal of the `vlookup for column P` column.
- **Column Renaming:** Applying more descriptive and Tableau-friendly names to the columns, avoiding abbreviations and acronyms for better clarity.
- **Data Preparation for Visualization:** Saving the cleaned and transformed data into a CSV file (`supernova_cleaned.csv`) for seamless import into Tableau.

## Files Included

- `analyze_llm_results.py`: The Python script containing the code used for loading, cleaning, and preparing the supernova dataset.
- `supernova_cleaned.csv`: The resulting cleaned dataset in CSV format, ready for Tableau.
- `Supernova-no-duplicates-dataset.xlsx`: The original raw dataset in Excel format.
- `README.md`: This file, providing an overview and documentation for the project.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore (e.g., virtual environment files).

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Yuhc19/Supernova-MGU.git](https://github.com/Yuhc19/Supernova-MGU.git)
    cd Supernova-MGU
    ```
2.  **Ensure Dependencies:** Make sure you have Python 3 installed. It's recommended to use a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    . venv/Scripts/activate  # On Windows PowerShell
    pip install pandas openpyxl
    ```
3.  **Run the Data Cleaning Script:**
    ```bash
    python analyze_llm_results.py
    ```
    This script will:
    - Load the `Supernova-no-duplicates-dataset.xlsx` file
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




















