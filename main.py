import requests
from bs4 import BeautifulSoup
import re
import json
import time

list_SIM = []  # Add your list of SIMs here
jsonresult = {}
output_file = "sim_data.json"  # File to store the JSON data
iteration_count = 0  # Counter to track iterations

def login():
    """Function to handle login and return a session."""
    session = requests.Session()
    login_url = "https://account.truphone.com/login"
    login_page_response = session.get(login_url)

    if login_page_response.status_code != 200:
        print(f"Failed to fetch login page: {login_page_response.status_code}")
        exit()

    soup = BeautifulSoup(login_page_response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})

    login_data = {
        "email": "",  # Your email
        "password": ""  # Your password
    }

    if csrf_token:
        login_data['csrfmiddlewaretoken'] = csrf_token['value']

    login_response = session.post(login_url, data=login_data)
    if login_response.status_code == 200 and "Dashboard" in login_response.text:
        print("Login successful!")
        return session
    else:
        print(f"Login failed! Status code: {login_response.status_code}")
        exit()

# Start with an initial login
session = login()

# Process each SIM
for sim in list_SIM:
    iteration_count += 1

    # Re-login every 500 iterations
    if iteration_count % 500 == 0:
        print("Re-logging in after 500 iterations...")
        session = login()

    url = f"https://iot.truphone.com/sims/{sim}/"
    protected_response = session.get(url)
    if protected_response.status_code != 200:
        print(f"Error fetching SIM data: {protected_response.status_code}")
        continue

    response_text = protected_response.text
    soup = BeautifulSoup(response_text, 'html.parser')

    # Extract the dates from the table
    dates = {}
    rows = soup.select('.panel-body table.table-striped tr')
    for row in rows:
        th = row.find('th')
        td = row.find('td')
        if th and td:
            dates[th.text.strip()] = td.text.strip()

    # Regular expression to capture the usage amount
    pattern = r'Usage Since First Activation.*?<td>\s*(\d+\.?\d*)\s*(MB|GB|KB|kB|kb)\s*</td>'
    pattern_2 = r'Total Rate Plans Used</th>\s*<td><a href=[^>]+>(\d+)</a></td>'

    match = re.search(pattern, response_text, re.DOTALL)
    rate_plan_match = re.search(pattern_2, response_text, re.DOTALL)

    usage = match.group(1) if match else "Not found"
    unit = match.group(2) if match else "Not Found"
    total_rate_plans = rate_plan_match.group(1) if rate_plan_match else "No match found"

    jsonresult = {
        "ICCID": sim,
        "usage": usage,
        "unit": unit,
        "rate_plan": total_rate_plans
    }
    jsonresult.update(dates)

    # Write JSON result to file
    with open(output_file, "a") as file:
        file.write(json.dumps(jsonresult) + "\n")

    print(f"Data for SIM {sim} written to {output_file}")
    time.sleep(1)  # To avoid overloading the server

print(f"Processing completed. Data saved to {output_file}.")
