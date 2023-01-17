import requests
import json


client_id = "CLIENT_ID"
client_secret = "CLIENT_SECRET"


meeting_id = "MEETING_ID"

# Get access token
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}
response = requests.post("https://zoom.us/oauth/token", data=data)
access_token = response.json()["access_token"]

# Request headers
headers = {
    "Authorization": f"Bearer {access_token}"
}

# API endpoint for getting the report of a specific meeting
url = f"https://api.zoom.us/v2/metrics/meetings/{meeting_id}/report"

# Send GET request
response = requests.get(url, headers=headers)

# Print the report
print(json.dumps(response.json(), indent=4))
