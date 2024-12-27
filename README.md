# Truphone Usage Data Scraper

This Python script is designed to scrape usage data from Truphone's IoT platform. It logs into your Truphone account, retrieves usage information for SIM cards, and outputs the results in JSON format. The script specifically extracts "Usage Since First Activation" and the "Total Rate Plans Used" for each SIM card.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `re` (Regular Expressions, part of the standard Python library)

You can install the necessary libraries using pip:

pip install requests beautifulsoup4
Setup

Before running the script, you need to configure the following:

ICCID List: Provide a list of ICCID values (SIM card identifiers) that you want to fetch usage data for. Update the list_SIM variable with the ICCID(s) you want to track.

Login Credentials: Set your Truphone account email and password for the login process. Update the login_data dictionary with your credentials.

Example
python
Copy code
list_SIM = ['SIM_ICCID_1', 'SIM_ICCID_2', 'SIM_ICCID_3']  # Replace with actual ICCIDs

login_data = {
    "email": "your_email@example.com",  # Replace with your email
    "password": "your_password"         # Replace with your password
}
How It Works
Login: The script sends a GET request to the Truphone login page to fetch a CSRF token (if required). After extracting the token (if available), it logs in using the provided email and password.

Data Extraction: After logging in, the script iterates through the provided list of ICCID values. For each SIM card, it fetches the usage data and extracts:

Usage Since First Activation (in MB or GB)
Total Rate Plans Used
The extracted data is stored in a JSON format.

Results: The final output is a list of JSON objects, where each object contains:

ICCID: The SIM card identifier.
usage: The data usage since first activation (e.g., 150.5 MB).
unit: The unit of measurement (MB or GB).
rate_plan: The total number of rate plans used.
Example Output
The script outputs a list of JSON objects in the following format:

json
Copy code
[
    {
        "ICCID": "SIM_ICCID_1",
        "usage": "150.5",
        "unit": "MB",
        "rate_plan": "3"
    },
    {
        "ICCID": "SIM_ICCID_2",
        "usage": "2.5",
        "unit": "GB",
        "rate_plan": "1"
    }
]
Usage
Edit the script: Set your list_SIM with the ICCDs you wish to query and provide your Truphone login credentials.

Run the script: Execute the script using Python:

Copy code
python truphone_usage_scraper.py
Check the output: The script will print the JSON results to the console, containing the usage data for each SIM card.
Notes
The script sleeps for 1 second between requests to avoid overloading the Truphone servers.
Ensure that you have the correct permissions to access the required data on the Truphone platform.
If you encounter any issues with the CSRF token or login, check that your credentials are correct and that the login process is functioning as expected.
