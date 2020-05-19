import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# obtaining information
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()

#Functions for notification
def notifyMe(title,message):
	notification.notify(
		title = title,
		message = message,
		timeout = 5 )

#notification 
while True:
	notifyMe('Infected with coronavirus',cases)
#interval notification
	time.sleep(300)