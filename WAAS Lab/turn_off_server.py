import requests

# Base URL for the API
base_url = "https://api.waas.barracudanetworks.com/v4/waasapi/applications/"

# Bearer token (replace with actual token)
bearer_token = "token"

# Loop through the range of student numbers (01 to 25)
for i in range(1, 26):
    student_number = f"{i:02}"  # Format student number with leading zero if needed
    url = base_url + f"Student{student_number}/servers/"

    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    # Perform GET request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        servers = response.json()

        # Check if any server is in "In Service" mode with "Up" health
        for server in servers:
            if server.get("mode") == "In Service" and server.get("health") == "Up":
                # Prepare data for PUT request
                put_data = server.copy()
                put_data["mode"] = "Out of Service"
                put_data["health"] = "Down"

                # Perform PUT request
                put_response = requests.put(url, headers=headers, json=[put_data])

                if put_response.status_code == 200:
                    print(f"PUT request successful for Student{student_number}")
                else:
                    print(f"Failed to send PUT request for Student{student_number}: {put_response.status_code}, {put_response.text}")
    else:
        print(f"Failed to retrieve data for Student{student_number}: {response.status_code}, {response.text}")
