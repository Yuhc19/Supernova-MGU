# Supernova MGU Analysis

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 

## Overview

This project focuses on the cleaning and preparation of a supernova dataset obtained from Supernova MGU. The goal is to transform the raw data into a clean and structured format suitable for creating insightful visualizations using Tableau.

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

# Supernova MGU - LLM Results Analysis and Accuracy Verification

Assumptions:

1. Category = alert checking.
2. "N" = 'No'.
3. Crime rate, lower value = 'safer', higher value = 'higher risk of crime'.
4. For presentation, sample of 2 accurate and 2 inaccurate.

Instructions:

1. Paste business name and address, look at google search results
2. Read what the business is about, what they do, check 'data' field for matching.

This README outlines the steps taken to process and analyze data involving LLM-generated results for Supernova MGU. The goal was to clean the initial dataset, parse information from a specific 'data' column containing JSON, manually verify the accuracy of the LLM outputs, and finally, perform an initial analysis of surcharges and discounts.

## Project Steps

### 1. Initial Data Cleaning and Preparation (`analyze_llm_results.py` - Initial Version)

1.  **Loading the Dataset:** The initial dataset (`Supernova-no-duplicates-dataset.xlsx`) was loaded using the pandas library in Python.
2.  **Column Removal:** The column 'vlookup for column P' was removed as it was deemed irrelevant.
3.  **Column Renaming:** Several columns with abbreviations and acronyms were renamed to be more descriptive and Tableau-friendly (e.g., 'insured_address_state' to 'Insured Address State/Province').
4.  **Saving Cleaned Data:** The cleaned and renamed data was saved to a CSV file (`supernova_cleaned.csv`).
5.  **GitHub Repository Initialization:** A new public GitHub repository named 'Supernova-MGU' was created, and the local project files were initialized as a Git repository using `git init`.
6.  **Committing and Pushing:** The initial project files (Python script, cleaned CSV, etc.) were committed and pushed to the 'Supernova-MGU' repository on GitHub.

### 2. Parsing the LLM Results (`analyze_llm_results.py` - Parsing Version)

1.  **Loading LLM Results:** A new CSV file containing LLM processed results (`llm_results_processed.csv`) was loaded using pandas.
2.  **Parsing the 'data' Column:** A Python function (`extract_data`) was created to parse the JSON strings within the 'data' column. This function extracted:
    * `answer_value`
    * `answer_reasoning`
    * `url` (taking the first URL if a list was present)
    * `bbb_rating` (if present within a nested 'answer_value' dictionary)
3.  **Creating New Columns:** The extracted information was used to create new columns in the DataFrame: 'AnswerValue', 'AnswerReasoning', 'URL', and 'BBBRating'.
4.  **Renaming Columns (Final):** The column names were further refined to be more descriptive and without abbreviations (e.g., 'Name' to 'CompanyName', 'category' to 'Category').
5.  **Saving Parsed Data:** The DataFrame with the parsed columns was saved to a new CSV file (`llm_results_parsed.csv`).

### 3. Manual Accuracy Verification (External Process)

1.  **Import to Spreadsheet Software (Google Sheets):** The `llm_results_parsed.csv` file was manually imported into a Google Sheets.
2.  **Manual Review:** Each record was manually reviewed to assess the accuracy of the LLM's 'AnswerValue' and 'AnswerReasoning'.
3.  **Creating Verification Columns:** Two new columns were manually created and populated:
    * **'Accurate'**: A binary indicator (1 for accurate, 0 for inaccurate).
    * **'Verifier Finding'**: A text field to record any specific findings or reasons for inaccuracy identified during the review.
4.  **Saving Verified Data:** The spreadsheet with the added 'Accurate' and 'Verifier Finding' columns was saved as a new Excel file named `LLM Returned Data Accuracy Analysis.xlsx`.

### 4. Surcharge and Discount Analysis in Tableau

1.  **Data Source Connection:** The `LLM Returned Data Accuracy Analysis.xlsx` file was connected as a data source in Tableau.
2.  **Creating Binned Risk Factor Dimensions:** The continuous risk factor measures (`output_debug_sd_factor_bi`, `output_debug_sd_factor_gl`, `output_debug_sd_factor_prop`) were binned in Tableau to create categorical dimensions representing different risk levels (e.g., Low Risk, Medium Risk, High Risk). The bin sizes were determined based on the data distribution.
3.  **Analyzing Average Total Premium by Binned Risk Factors and Segments:** Visualizations were created to analyze the average total premium (`output_premium_total_total_prem`) across different segments (like 'Category', 'insured_address_state', or 'industry code') for each bin of the risk factors.
4.  **Identifying Segments with Potential Surcharges and Discounts:** By observing the average total premium in the lower (potential discount) and higher (potential surcharge) risk factor bins for different segments, insights were gained into which segments might be receiving more implicit surcharges or discounts. Color coding was used to enhance the visualization of premium differences.

## Next Steps

Creating a Google Slides presentation link below:


















