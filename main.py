import requests
from bs4 import BeautifulSoup
import re
import json
import time
list_SIM =['']
    

jsonresult = {}
all_result = []

# Create a session to persist cookies and manage login
session = requests.Session()

# Step 1: Fetch the login page to get the CSRF token (if required)
login_url = "https://account.truphone.com/login"
login_page_response = session.get(login_url)

# Check if the page was fetched successfully
if login_page_response.status_code != 200:
    print(f"Failed to fetch login page: {login_page_response.status_code}")
    exit()

# Step 2: Parse the page to extract the CSRF token (if present)
soup = BeautifulSoup(login_page_response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})

if csrf_token:
    csrf_token = csrf_token['value']
    print(f"CSRF Token Found: {csrf_token}")
else:
    print("No CSRF token found. Proceeding without it.")

# Step 3: Define login form data (adjust if CSRF is required)
login_data = {
    "email": "",  # Your email
    "password": ""  # Your password
}

# Add CSRF token to the login data if needed
if csrf_token:
    login_data['csrfmiddlewaretoken'] = csrf_token

# Step 4: Submit the login form
login_response = session.post(login_url, data=login_data)

# Step 5: Check if login was successful
if login_response.status_code == 200 and "Dashboard" in login_response.text:
    print("Login successful!")
else:
    print(f"Login failed! Status code: {login_response.status_code}")
    print(login_response.text)  # For debugging, print the response content

# Step 6: Make authenticated requests after login (optional)
for sim in list_SIM:

    url = "https://iot.truphone.com/sims/"+sim+"/"
    protected_response = session.get(url)
    if protected_response.status_code == 200:
        print("Success!")
        # print(protected_response.content)  # Assuming the response is in JSON format
    else:
        print(f"Error: {protected_response.status_code}")

    # Sample response content
    response_text =protected_response.text

    # Regular expression to capture the usage amount
    pattern = r'Usage Since First Activation.*?<td>\s*(\d+\.?\d*)\s*(MB|GB)\s*</td>'
    # Regular expression pattern to extract the total rate plans used
    pattern_2 = r'Total Rate Plans Used</th>\s*<td><a href=[^>]+>(\d+)</a></td>'



    # Search for the pattern in the response text
    match = re.search(pattern, response_text, re.DOTALL)
    rate_plan_match = re.search(pattern_2, response_text,re.DOTALL)

    if match:

# Search for the pattern in the response text
        usage = match.group(1)
        unit = match.group(2)
        result = f"Usage Since First Activation: {usage} {unit}"
        # print(result)
        
    else:
        print("No match found.")
        usage = "Not found"
        unit = "Not Found"

# Check if a match was found
    if rate_plan_match:
        total_rate_plans = rate_plan_match.group(1)
        rate_plan_result = total_rate_plans
    else:
        rate_plan_result = "Total Rate Plans Used: No match found."

    jsonresult["ICCID"] = sim
    jsonresult["usage"] = usage
    jsonresult["unit"] = unit
    jsonresult["rate_plan"] = rate_plan_result

    all_result.append(jsonresult)
    jsonresult = {}


        
  
    time.sleep(1)


print(all_result)
