# Repeating-API
This script acts as a heartbeat to an API so it doesn't fall asleep.

## Installation 
I used python on my Windows PC which had access to a lab.

Pip Istall these libraries: <br />
from datetime import datetime <br />
import os <br />
import requests <br />
import time <br />
import schedule <br />

## Usage 
This code was originally used in a customer environment. It will change with each user. The URL should match what the customer gives you to test. Your heading will be different from this script and will need updated too. The API that you ping can be anything. The script will call the API over and over until you stop the script. The output is to the python terminal. I added colors to the API response code: green for good(200), red for bad and yellow, meaning that response needs to be added to the script. Contact the owner to update.

## DevNet 
Sandbox - All sandboxes with APIs can use this script.

## Known issues 
There is no stop time for the script. Due to customer time, I have the script working and will add a stop time in a later version. You have to manually stop this script from running.

## Getting help 
Contact the owner if he is not too busy.

## Credits and references 
The Cisco requests library. <br />
The book - Automate the boring stuff with python. <br />
Stack Overflow.

## Best Practice 
Run the script on 1 API to verify the script runs. Ramp up to 10,15 or 20 minutes when you know the script is working.

## Step by Step

    - Download python script based on the operating system you use to run the script.
    - PIP install the requirements.
    - Edit the file with your URL(Line 14), key(Line 18) and token(Line 19).
    - Run the script at the 1 minute setting. The script runs a minute after you start it.
    - Hit stop button in pycharm to stop, or equivalent in your app.
    
    

## Example Output
[]
200
We are looking pinging the API every 10 minutes to keep it alive
0.697998
2021-08-31 02:37:49.068387

[]
200
We are looking pinging the API every 10 minutes to keep it alive
0.403552
2021-08-31 02:38:50.489381








