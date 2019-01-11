# from config_local import TENCHANAPI_BASIC_AUTH_USER, TENCHANAPI_BASIC_AUTH_PASS
# from config_starging import TENCHANAPI_BASIC_AUTH_USER, TENCHANAPI_BASIC_AUTH_PASS
from config_production import TENCHANAPI_BASIC_AUTH_USER, TENCHANAPI_BASIC_AUTH_PASS
import requests
import datetime
import time

url = "https://myapi.com/"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

queries = {
            "sleep": {"path":"sleeps", "device":"Nokia Sleep"},
            "body": {"path":"bodies", "device":"Nokia Body Plus"}
            }

now = datetime.datetime.now()
now_unixtime = int(time.mktime(now.timetuple()))

a_day_to_seconds = 86400
scheduler_launch_gap = 1800 # record_nokia_healthとtweet_bio_infomationの起動タイミングのギャップを加算する

startdate = now_unixtime - (a_day_to_seconds + scheduler_launch_gap)
enddate = now_unixtime

def request_bio_infomation(member):
    bio_infomation = {}

    for key, value in queries.items():

        query = "?startdate=%i&enddate=%i&member=%i&device=%s" % (startdate, enddate, member, value["device"])

        response = requests.get(url + value["path"] + query, headers=headers, auth=(TENCHANAPI_BASIC_AUTH_USER , TENCHANAPI_BASIC_AUTH_PASS))

        bio_infomation[key] = response.json()

    return bio_infomation

if __name__ == "__main__":
    bio_infomation = request_bio_infomation(0)