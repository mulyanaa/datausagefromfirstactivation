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


#Sample output:

{"ICCID": "124343342342342", "usage": "252.82", "unit": "MB", "rate_plan": "1", "Primary IMSI": "12312312323", "Additional IMSI's": "208090082920238\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t204080923287079\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t234259996682045\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t310300996626053\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t505389996626045\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t454089996626053\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t214279996626039\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t204339996676027\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t262429996626013\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t260339996626032\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t\t208129996607983", "Primary MSISDN": "23123123", "Additional MSISDN's": "N/A", "Type": "Mini-SIM", "Initial PIN1": "1231", "Initial PIN2": "12312312", "PUK1": "1231213", "PUK2": "12312312", "Provisioned Date": "2023/05/23 07:48 UTC", "Shipping Date": "2023/05/23 07:48 UTC", "Delivery Date": "2023/05/23 07:48 UTC", "Date First Activated": "2023/10/09 08:20 UTC", "Rate Plan": "example", "Total Rate Plans Used": "1", "Billing Cycle": "", "Label": "example ", "Description": " Truphone", "SIM Card": "Active", "Data Service": "Active", "SMS MO Service": "Active", "SMS MT Service": "Active", "Current Device": "86053706700402\n\t\t\t\n\t\t\t\t\u00a0(SIMCOM Wireless Solutions Co Ltd - SIM7600E,SIM7600EI,SIM7600EI-H)", "Last Location": "Malaysia / MMS & MB  (Last Date Seen:&nbsp2025/01/16 11:43 UTC)", "Status": "Offline", "Start Date": "N/A", "IP Address": "N/A", "Last Call Detail Record": "Data", "Monthly Data Usage": "6.05 MB", "Monthly Number Of Connections": "", "Monthly Outbound SMS": "0 SMS", "Usage Since First Activation": "252.82 MB", "Usage On Current Rate Plan": "252.82 MB"},
