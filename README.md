# polito-auto-login
Your WiFi session  at Politecnico di Torino will expire at a given interval forcing you to re-enter your username and password at the wifiauth.polito.it. This Python3 script works on macOS and will ping www.google.it every third second, when a ping times out it will use a webdriver from Selenium to open wifiauth.polito.it and fill in your username and password and log you back in.

# Get started
Clone repo
  git clone https://github.com/erlingrj/polito-auto-login/
  cd  polito-auto-login
  
Download required python libraries
  pip3 install -r requirements.txt
  
Move the chromedriver to PATH
