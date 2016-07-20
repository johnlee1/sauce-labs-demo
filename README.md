# sauce-labs-demo
This repository contains a sample flask application with automated selenium testing using Sauce Labs.

The tests are triggered and run on codeship.

# codeship setup
###Setup commands 
`pip install -r requirements.txt`

###Test commands
```
cd sc-4.3.16-linux
cd bin
chmod 764 sc
cd ..
bin/sc -u $SAUCE_USERNAME -k $SAUCE_ACCESS_KEY &
sleep 60
cd ..
python app.py &
sleep 5
python selenium-test.py
```
