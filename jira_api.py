# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests, getpass
import urllib3
from requests.auth import HTTPBasicAuth
import json
from save_game import SaveGame

sprintId = int(input("Geef het ID van de sprint op: "))
propertyKey = "goal"
urllib3.disable_warnings()
url = f"https://jira.kpn.org/rest/agile/1.0/sprint/{sprintId}/"
auth = HTTPBasicAuth("paulusdevries@kpn.com", password=getpass.getpass())
response = requests.request(
    "GET",
    url,
    auth=auth,
    verify=False
)

saveText = SaveGame()

saveText.saveGame(response.text)

text = json.loads(response.text)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
print(f"Naam: {text['name']} \nSprint doel: {text['goal']} \n")