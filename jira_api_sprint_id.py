# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from secrets import GetPassword
import json
from save_game import SaveGame
from recursive_json import extract_values

#sprintId = int(input("Geef het ID van de sprint op: "))
query = input("Geed de sprint naam op: ")
version_id = "DVBT_Beheer"
# propertyKey = "goal"
urllib3.disable_warnings()
url = f"https://jira.kpn.org/rest/greenhopper/latest/sprintquery/3482?includeHistoricSprints=true&includeFutureSprints=true"
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
sprint_id = extract_values(response.json(), 'id')
sprint_name = extract_values(response.json(), 'name')
sprint_start = extract_values(response.json(), 'startDate')
sprint_end = extract_values(response.json(), 'endDate')
# print(f"Raw json response: {text}  \n  Sprint ID's: {sprint_id} \n names: {sprint_name}")
for _ in range(len(sprint_name)):
    if query == sprint_name[_]:
        print(f"Sprint id = {sprint_id[_]} and sprint startdate = {_}")

print(f"Sprint startdate: {sprint_start}")

