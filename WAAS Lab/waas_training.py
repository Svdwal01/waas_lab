import requests
import json

# Base URL for the API
base_url = "https://api.waas.barracudanetworks.com/v2/"

# Bearer token (replace with actual token)
bearer_token = "Token"

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {bearer_token}",  # Use bearer token
    "Referer": base_url,
}

# Endpoint for application creation
api_url = "https://api.waas.barracudanetworks.com/v2/waasapi/applications/"

# Base payload template
base_payload = {
  "backendPort": 8000,
  "useHttp": True,
  "useExistingIp": True,
  "backendIp": "172.190.141.153",
  "maliciousTraffic": "Active",
  "serviceIp": "2.2.2.2",
  "httpsServicePort": 443,
  "redirectHTTP": True,
  "useHttps": True,
  "httpServicePort": 80,
  "backendType": "HTTP",
  "serviceType": "HTTP",
  "account_ips": {},
  "hostnames": [
    {
      "hostname": ""
    }
  ]
}

# Function to generate the payload for each call
def generate_payload(number):
    application_name = f"Student{number:02}"
    backend_port = 8000 + number
    hostname = f"student{number:02}.acmestores.nl"
    
    payload = base_payload.copy()
    payload["applicationName"] = application_name
    payload["backendPort"] = backend_port
    payload["hostnames"][0]["hostname"] = hostname
    
    return payload

# Loop through the range and make the API calls
for i in range(1, 26):  # Adjusted the range to run 25 iterations
    payload = generate_payload(i)
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print(f"Successfully created application {payload['applicationName']}")
    else:
        print(f"Failed to create application {payload['applicationName']}: {response.status_code}, {response.text}")
