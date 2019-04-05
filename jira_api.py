# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests, getpass
from requests.auth import HTTPBasicAuth
import json

sprintId = 23645
propertyKey = "goal"
url = f"https://jira.kpn.org/rest/agile/1.0/sprint/{sprintId}/"
auth = HTTPBasicAuth("paulusdevries@kpn.com",password=getpass.getpass())

response = requests.request(
    "GET",
    url,
    auth=auth,
    verify=False
)

text = json.loads(response.text)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
print(f"Naam: {text['name']} \nSprint doel: {text['goal']} \n")