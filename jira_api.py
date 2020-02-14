# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from secrets import GetPassword
import json
from save_game import SaveGame

sprintId = int(input("Geef het ID van de sprint op: "))
version_id = "DVBT_Beheer"
# propertyKey = "goal"
urllib3.disable_warnings()
url = f"https://jira.kpn.org/rest/agile/latest/sprint/{sprintId}/"
url_versions = f"https://jira.kpn.org/rest/agile/latest/version/{version_id}/relatedIssueCounts"
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

version_resp = requests.request(
    "GET",
    url_versions,
    auth=auth,
    verify=False
)

saveText = SaveGame('jira')
saveText.saveGame(response.text)
text = json.loads(response.text)
# ver_text = json.loads(version_resp.text)
print(f"Naam: {text['name']} \nSprint doel: {text['goal']} \nData: {text['startDate']} and {text['endDate']}")
#print(ver_text)
