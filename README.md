# polito-auto-login
Your WiFi session  at Politecnico di Torino will expire at a given interval forcing you to re-enter your username and password at the wifiauth.polito.it. This Python3 script works on macOS and will ping www.google.it every third second, when a ping times out it will use a webdriver from Selenium to open wifiauth.polito.it and fill in your username and password and log you back in.

# Get started
Clone repo
'git clone https://github.com/erlingrj/polito-auto-login/'
'cd  polito-auto-login'
  
Download required python libraries
'pip3 install -r requirements.txt'
  
To use the script the chromedriver executable in this repo needs to be moved into the system path. If not except an error like:
"selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH."

Open auto-login.py and provide your username and password to "USERNAME" and "PASSWORD" variables in line 9 and 10.

Run script
'python3 auto-login.py'

# Prerequisites
* You have to be "connected" to the polito wifi when running the script
* The script will fail if the login-page is opened. This typically happens automatically the first time you open your Mac.
