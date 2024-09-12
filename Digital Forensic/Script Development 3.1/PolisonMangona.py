import pandas as pd
import csv
import json

# Load data
data = pd.read_json('Script Development 3.1/forensic_data.json')
# Extract relevant columns
extracted_data = data[['timestamp', 'ip_address', 'user_activity']]
print("************************")
# Display extracted data
print(extracted_data)


