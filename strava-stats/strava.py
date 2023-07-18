import requests
import urllib3
from datetime import datetime
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

RUN = 'Run'
RIDE = 'Ride'

def get_first_day_epoch_time():
    date_today = datetime.now()
    month_first_day = date_today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return time.mktime(month_first_day.timetuple())

def get_access_token():
    auth_url = "https://www.strava.com/oauth/token"
    # replace variables with values for your account
    # Leave grant type as 'refresh_token'
    payload = {
        'client_id': "75776",
        'client_secret': '30be6635d5ff63244632097a7a04bc78e83a6241',
        'refresh_token': '4e421f6e4900a4f856e725278fd050007b80ad40',
        'grant_type': "refresh_token",
        'f': 'json'
    }
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    return access_token

def request_monthly_activities():
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + get_access_token()}
    distances = {RUN: 0, RIDE: 0}

    param = {'per_page': 200, 'page': 1, 'after': get_first_day_epoch_time()}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()

    if len(my_dataset) == 0:
        print("No activities")
    else:
        for activity in my_dataset:
            sport_type = activity['sport_type']
            if (sport_type == RIDE):
                distances[RIDE] += activity['distance'] * 0.000621371
            if (sport_type == RUN):
                distances[RUN] += activity['distance'] * 0.000621371

    distances[RIDE] = round(distances[RIDE], 1)
    distances[RUN] = round(distances[RUN], 1)
    return distances