# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from secrets import GetPassword
import json
from save_game import SaveGame

sprintId = int(input("Geef het ID van de sprint op: "))
# propertyKey = "goal"
urllib3.disable_warnings()
url = f"https://jira.kpn.org/rest/agile/1.0/sprint/{sprintId}/"
# auth = HTTPBasicAuth("paulusdevries@kpn.com", password=getpass.getpass('Please provide the Jira password: '))
getpassword = GetPassword()
password = getpassword.retrievePassword()
password = password.decode()
auth = HTTPBasicAuth("paulusdevries@kpn.com", password=password)
response = requests.request(
    "GET",
    url,
    auth=auth,
    verify=False
)

saveText = SaveGame('jira')
saveText.saveGame(response.text)
text = json.loads(response.text)
print(f"Naam: {text['name']} \nSprint doel: {text['goal']} \n")