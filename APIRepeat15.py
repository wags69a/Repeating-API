import requests
import time
from datetime import datetime
import schedule

#print()
start_time = datetime.now()
print('The report started at: ' + (str(start_time)))
print()
print('This query will provide a heartbeat so that the connector does not fall asleep')


def pingApi():
    url = "https://<URLBASE>?employeeNumber=XXXXX"

    payload = ""
    headers = {
        'us-customer-api-key': '<APIKEY',
        'Authorization': 'Basic <ACCESS TOKEN>'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    print()
    print(response.status_code)
    print()
    print('We are looking pinging the API every 15 minutes to keep it alive')
    print()
    print(response.elapsed.total_seconds())
    print()
    print(datetime.now())
    print()
    time.sleep(1)
    return

schedule.every(1).minutes.do(pingApi)

while True:
    schedule.run_pending()


