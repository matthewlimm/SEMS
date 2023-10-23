import pandas as pd

def analyze_radiation(data_frame):
    # Conversion factor from CPM to µSv/h (a general approximation)
    cpm_to_microsieverts_per_hour = 0.0057

    # Check against legal safety limits
    legal_limit_microsieverts_per_hour = 1.0  # Example limit, please check your local regulations

    exceeded_limit = data_frame['CPM'] * cpm_to_microsieverts_per_hour > legal_limit_microsieverts_per_hour

    return exceeded_limit

# Load the CSV data into a pandas DataFrame
data = pd.read_csv('radiation_data.csv')

# Analyze the data
exceeded_safety_limits = analyze_radiation(data)

# Print out data rows that exceed safety limits
print("Data exceeding safety limits:")
print(data[exceeded_safety_limits])
