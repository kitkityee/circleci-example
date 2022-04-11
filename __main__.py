from selenium import webdriver

driver = webdriver.Chrome(service_args=["--verbose", "--log-path=test-reports/chrome.log"])

driver.get("https://9gag.com")

driver.implicitly_wait(0.5)

print(driver.title)

assert driver.title == "9GAG: Go Fun The World"

driver.quit()
