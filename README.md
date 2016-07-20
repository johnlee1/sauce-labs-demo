# sauce-labs-demo
This repository contains a sample flask application with automated selenium testing using Sauce Labs and Sauce Connect.

The tests are triggered and run on codeship as part of the continuous integration process.

# codeship setup
###Environment variables
```
SAUCE_USERNAME
SAUCE_ACCESS_KEY 
SC_DISTRIBUTION (ex: sc-4.3.16-linux)
```

###Setup commands 
```
pip install -r requirements.txt
```

###Test commands
```
wget https://saucelabs.com/downloads/${SC_DISTRIBUTION}.tar.gz
tar -zxvf ${SC_DISTRIBUTION}.tar.gz
${SC_DISTRIBUTION}/bin/sc -u $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY &
sleep 45
python app.py &
sleep 5
python selenium-test.py
killall --wait sc
```
