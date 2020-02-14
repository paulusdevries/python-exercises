# This code sample uses the 'requests' library: # http://docs.python-requests.org
import requests
import urllib3
from requests.auth import HTTPBasicAuth
from secrets import GetPassword
import json
from save_game import SaveGame
from recursive_json import extract_values
import re



# Authenticatie instellen (basic Auth zoals op de website, zo ook op de API)
urllib3.disable_warnings()
getpassword = GetPassword()
password = getpassword.retrievePassword()
password = password.decode()

# Met de bovenstaande handelingen de onderstaande authenticatie opbouwen:
auth = HTTPBasicAuth("paulusdevries@kpn.com", password=password)

# Sla de ruwe resultaten op in het textbestandje "jira_version_report"
saveText = SaveGame('jira_burndown.txt')
saveCSV = SaveGame('jira_version.csv')

# URL de DATA en de HEADERS die aan de API-POST worden meegegeven:
url = f"https://jira.kpn.org/rest/api/2/search"
data = {
    "jql": "project = tb AND Sprint = 34716 and not Sprint in openSprints() and not Sprint in futureSprints() order by resolutiondate ASC",
    "startAt": 0,
    "maxResults": 100,
    "fields": [
        "key",
        "customfield_10002",
        "resolutiondate"
    ]
}
headers = {'Content-type': 'application/json'}

# Het opbouwen van de request met de requests module (let op, dat je de auth methode meegeeft die eerder gebouwd is
r = requests.post(url, data=json.dumps(data), headers=headers, auth=auth, verify=False)

r = r.json()

# Sla alle json data op: (debug)
saveText.saveGame(str(r) + "\n")

# Met een moduletje, van Internet gejat, de story points uit de json extraheren:
uitvogelen = extract_values(r, 'customfield_10002')

# Print alle resultaten
print(uitvogelen)

# Bereken het totaal van de story points met een list comprehension:
totaal = sum([int(ints) for ints in uitvogelen if ints is not None])

# Voor debugging de NONE's printen (waar geen storypoints zijn ingevuld)
print(f"{[inten for inten in uitvogelen if inten is None]} \n\n\n\n\n")

issues = r["issues"]
start = 'name='
end = ',startDate='
sprintnames = []
csv_buildup = {}

for i in issues:
    storykey = i["key"]
    points = i["fields"]["customfield_10002"]
    resolutiondate = i["fields"]["resolutiondate"]
    print(f"{storykey}; {points}; {resolutiondate}")


# Print de totalen en sla op in de csv:
print(f"Totaal; {totaal}")
# nu even geen save totalen:
# saveCSV.saveGame(f"\nTotaal;;;;;; {totaal}\n")




