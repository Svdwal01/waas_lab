import requests

# API key and base URL
API_KEY = "token"
BASE_URL = "https://api.waas.barracudanetworks.com/v2/waasapi/applications/"

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def get_applications():
    try:
        response = requests.get(BASE_URL, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def delete_application(app_id):
    delete_url = f"{BASE_URL}{app_id}/"
    try:
        response = requests.delete(delete_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        if response.status_code == 204:
            print(f"Successfully deleted application with ID: {app_id}")
        else:
            print(f"Failed to delete application with ID: {app_id}, Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while deleting application with ID: {app_id}: {e}")

def main():
    applications = get_applications()

    if applications is not None:
        id_name_list = [{"id": app["id"], "name": app["name"]} for app in applications["results"]]
        for item in id_name_list:
            print(f"ID: {item['id']}, Name: {item['name']}")
            if item['name'].startswith('Student') and item['name'][7:].isdigit() and 1 <= int(item['name'][7:]) <= 25:
                delete_application(item['id'])
    else:
        print("Failed to retrieve applications.")

if __name__ == "__main__":
    main()
