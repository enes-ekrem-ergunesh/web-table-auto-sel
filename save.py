from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import csv


""" Usage Variables """

limiter = 1

table_xpath = '//*[@id="data-table"]'


""" Usage Variables """


if limiter == 0:
    limiter = -2

service = Service('geckodriver')
driver = webdriver.Firefox(service=service)
driver.get('http://127.0.0.1:5500/index.html')

# Locate the table element
table = driver.find_element(By.XPATH, table_xpath)  # Replace with actual ID or other locators

# Get all table rows (including headers)
rows = table.find_elements(By.TAG_NAME, 'tr')

# Create an empty list to store table data
table_data = []


# Extract data from each row
for row in rows:
    limiter -= 1
    if (limiter + 2) == 0:
        break
    # Get all cells in the current row
    cells = row.find_elements(By.TAG_NAME, 'td')  # 'td' for data cells, 'th' for headers
    if not cells:
        cells = row.find_elements(By.TAG_NAME, 'th')

    # Create a list to store data from this row
    row_data = []
    for cell in cells:
        # Extract text from each cell and append it to the row data list
        row_data.append(cell.text.strip())  # Remove leading/trailing whitespaces

    # Append the row data to the table data list
    table_data.append(row_data)

# Close the browser window (optional)
driver.quit()

# Open a CSV file for writing
with open('extracted_table_data.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the table data to the CSV file
    csv_writer.writerows(table_data)

print("Table data extracted and saved to 'extracted_table_data.csv'.")
