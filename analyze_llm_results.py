import pandas as pd
import json

# Load the llm_results_processed.csv file
try:
    df = pd.read_csv('llm_results_processed.csv')
    print("llm_results_processed.csv loaded successfully:")
    print(df.head())
except FileNotFoundError:
    print("Error: llm_results_processed.csv not found. Please ensure it is in the correct directory.")
    exit()

# Function to safely parse JSON and extract values including 'url' and 'bbb_rating'
def extract_data(row):
    answer_value = None
    answer_reasoning = None
    url = None
    bbb_rating = None
    try:
        data = json.loads(row['data'])
        answer_value = data.get('answer_value')
        answer_reasoning = data.get('answer_reasoning')
        urls = data.get('urls')
        if urls:
            if isinstance(urls, list) and len(urls) > 0:
                url = urls[0]  # Take the first URL if it's a list
            elif isinstance(urls, str):
                url = urls
        # Extract BBB Rating if 'answer_value' is a dictionary
        if isinstance(answer_value, dict):
            bbb_rating = answer_value.get('BBB Rating')
    except (json.JSONDecodeError, AttributeError, TypeError):
        pass
    return pd.Series([answer_value, answer_reasoning, url, bbb_rating], index=['answer_value', 'answer_reasoning', 'url', 'bbb_rating'])

# Apply the function to create new columns
if 'data' in df.columns:
    df[['answer_value', 'answer_reasoning', 'url', 'bbb_rating']] = df.apply(extract_data, axis=1)

    # Rename the columns
    df = df.rename(columns={
        'Name': 'CompanyName',
        'Address': 'CompanyAddress',
        'Phone': 'CompanyPhone',
        'category': 'Category',
        'data': 'RawData',
        'answer_value': 'AnswerValue',
        'answer_reasoning': 'AnswerReasoning',
        'url': 'URL',
        'bbb_rating': 'BBBRating'
    })

    # Print the first few rows with the new column names
    print("\nDataFrame with renamed columns:")
    print(df.head())

    # Save the updated DataFrame to a new CSV file
    df.to_csv('llm_results_parsed.csv', index=False)
    print("\nDataFrame saved to llm_results_parsed.csv with renamed columns")
else:
    print("\nError: 'data' column not found in llm_results_processed.csv")