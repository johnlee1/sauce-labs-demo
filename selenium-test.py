from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
  

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}
driver = webdriver.Remote(
   command_executor='http://johnlee1:d26a6ba1-c5fd-4086-af56-6422d9e6e405@ondemand.saucelabs.com:80/wd/hub',
   #command_executor='http://YOUR_SAUCE_USERNAME:YOUR_SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub',
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