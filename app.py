from bs4 import BeautifulSoup
from selenium import webdriver
from twilio.rest import Client
from dotenv import load_dotenv
from os import environ, path

# Setting .env path
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Web Driver
driver = webdriver.Chrome()

# Fetching website
template = 'https://www.verseoftheday.com/'
driver.get(template)

# Soup object
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find('div', {"class": "bilingual-left"})

# Filtering text
verse = results.text
driver.close()

# Twilio Environment settings and Client creation
account_sid = environ['TWILIO_ACCOUNT_SID']
auth_token = environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Creating message
message = client.messages \
                .create(
                     body="Daily Wisdom" + f"\n{verse}",
                     from_='+17065537047',
                     to='6193130753'
                 )

print(message.sid)
