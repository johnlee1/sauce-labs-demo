# sauce-labs-demo
This repository contains a sample flask application with automated selenium testing using Sauce Labs and Sauce Connect.

The tests are triggered and run on codeship as part of the continuous integration process.

# codeship setup
###Setup commands 
`pip install -r requirements.txt`

###Test commands
```
chmod 764 sc-4.3.16-linux/bin/sc
sc-4.3.16-linux/bin/sc -u $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY &
sleep 45
python app.py &
sleep 5
python selenium-test.py
```
