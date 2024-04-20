from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


""" Usage Variables """

limiter = 20

table_xpath = '//*[@id="data-table"]'

where_table_index = 6

where_cell_is = ['Chile', 'Bosnia and Herzegovina', 'Togo']


""" Usage Variables """

if limiter == 0:
    limiter = -2

service = Service('geckodriver')
driver = webdriver.Firefox(service=service)
driver.get('http://127.0.0.1:5500/index.html')

table = driver.find_element(By.XPATH, table_xpath)  # Replace with actual ID or other locators

rows = table.find_elements(By.TAG_NAME, 'tr')

table_data = []


def right_click_and_delete(_row):
    # driver.execute_script("arguments[0].scrollIntoView();", _row)

    # Right-click on the row using ActionChains
    actions = ActionChains(driver)
    actions.context_click(_row).perform()
    time.sleep(2)

    delete_option = driver.find_element(By.XPATH, '/html/body/ul/li[1]')  # Adjust XPath if needed
    delete_option.click()
    time.sleep(1)


time.sleep(2)

for row in rows:
    print(row)
    limiter -= 1
    if (limiter + 2) == 0:
        break
    isHeader = False
    cells = row.find_elements(By.TAG_NAME, 'td')

    if not cells:
        cells = row.find_elements(By.TAG_NAME, 'th')
        isHeader = True

    print(cells[where_table_index].text.strip())

    if not isHeader and cells[where_table_index].text.strip() in where_cell_is:
        right_click_and_delete(row)

driver.quit()
