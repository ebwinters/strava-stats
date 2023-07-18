import requests
import urllib3
from datetime import datetime
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_first_day_epoch_time():
    date_today = datetime.now()
    month_first_day = date_today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return time.mktime(month_first_day.timetuple())

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

# replace variables with values for your account
# Leave grant type as 'refresh_token'
payload = {
    'client_id': "75776",
    'client_secret': '30be6635d5ff63244632097a7a04bc78e83a6241',
    'refresh_token': '4e421f6e4900a4f856e725278fd050007b80ad40',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']

print("Access Token = {}\n".format(access_token))
header = {'Authorization': 'Bearer ' + access_token}

# First loop starts on page 1.
# It will then loop through any further pages required.
all_activities = []

param = {'per_page': 200, 'page': 1, 'after': 1689592453}
# initial request, where we request the first page of activities - 200 per page
my_dataset = requests.get(activites_url, headers=header, params=param).json()

# If the response is empty we will leave the loop, otherwise we will keep collecting data
if len(my_dataset) == 0:
    print("No activities")
else:
    distance = 0
    for activity in my_dataset:
        distance += activity['distance'] * 0.000621371
    print(distance)
