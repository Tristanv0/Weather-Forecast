import json
import requests
'''
all API Status Codes:
200: Everything went okay, and the result has been returned (if any).
301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
400: The server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
401: The server thinks you're not authenticated. Many APIs require login credentials, so this happens when you don't send the right credentials to access an API.
403: The resource you're trying to access is forbidden: you don't have the right permissions to see it.
404: The resource you tried to access wasn't found on the server.
503: The server is not ready to handle the request.
'''

parameters = {
    "key" : 'a152189b0c2e4f4291e42103230803',
    "q"  : 'Scarborough, Ontario'
}
response = requests.get("http://api.weatherapi.com/v1/current.json", params=parameters) #key=a152189b0c2e4f4291e42103230803&q=London&aqi=no

print(response.status_code)

def jprint(obj):
    if obj.status_code == 200:
        # create a formatted string of the Python JSON object
        text = json.dumps(obj.json(), sort_keys=True, indent=4)
        print(text)
    else:
        print(f"Request failed with status code {obj.status_code}")

jprint(response)