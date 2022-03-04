"""
This script will ping an API to keep it awake every X minutes that you set.
This was built on a PC and the API is from a Windows Server. The auth will change if the API is a non windows OS.

Change the number 1 in this command:
schedule.every(1).minutes.do(pingapi)
To the amount of time in minutes, that you want it to ping.

User input for the base URL, user name and password. You will need to edit the rest of the URL and headers for your
test.

For this version of the code, you must manually stop it or it will go forever.
"""

from datetime import datetime

__version__ = '2.0'
__author__ = 'Michael A Wagner'

import os
import requests
import time
import schedule

os.system("")

COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "YELLOW": "\033[0;93m",
    "WHITE=": "\033[97m",
    "BLINK": "\033[5m",
    "ENDC": "\033[0m",
}

requests.packages.urllib3.disable_warnings()

start_time = datetime.now()
print(f'The report started at {start_time}')
print()
print('This query will provide a heartbeat so that the API connector does not fall asleep.')

ip = input('What is the IP Address of the API that you want to test: ')
user = input('What is the user name: ')
pwd = input('What is the Password: ')

def pingapi():

    url = f"https://{ip}:8111/cvp-config/snmp/community"

    payload = ""
    headers = {
        'Content-Type': 'application/xml',
        'Accept': 'application/xml'
        }

    response = requests.request("GET", url, headers=headers, data=payload, auth=(user, pwd), verify=False)
    print(response.text)
    print()
    #print(response.status_code)
    if response.status_code == 200:
        print(COLOR["GREEN"], response.status_code)
    if response.status_code == 401:
        print(COLOR["RED"], response.status_code)
    if response.status_code == 404:
        print(COLOR["RED"], response.status_code)
    if response.status_code == "___":
        print(COLOR["YELLOW"], response.status_code)
        print("New response code needs added to the script ")
    print()
    print('We are pinging the API every minute to keep it alive')
    print()
    print(response.elapsed.total_seconds())
    print()
    print(datetime.now())
    print()
    time.sleep(1)
    return


schedule.every(1).minutes.do(pingapi)

if __name__ == '__main__':
    try:
        pingapi()
        while True:
            schedule.run_pending()

    except requests.exceptions.ConnectionError as n:
        print(COLOR["RED"], 'IP address is not responding OR ', COLOR["ENDC"])
        print(COLOR["RED"], 'IP address is incorrect OR', COLOR["ENDC"])
        print(COLOR["RED"], 'The VPN is down', COLOR["ENDC"])

    except ConnectionRefusedError as n:
        print(COLOR["RED"], 'Check your userID or Password again', COLOR["ENDC"])

    except KeyboardInterrupt as n:
        print(COLOR["RED"], 'We had to stop the testing!', COLOR["ENDC"])