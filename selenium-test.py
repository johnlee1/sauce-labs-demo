from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import os

SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')
print SAUCE_USERNAME

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}
driver = webdriver.Remote(
   command_executor='http://'+SAUCE_USERNAME+':'+SAUCE_ACCESS_KEY+'@ondemand.saucelabs.com:80/wd/hub',
   desired_capabilities=desired_cap)
  

# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5000/")

link = driver.find_element_by_name('about')
link.click()

elem = driver.find_element_by_id("aboutHeader")
assert "About" in driver.page_source

  
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()