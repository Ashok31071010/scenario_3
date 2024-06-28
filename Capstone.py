import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def wordpress():
    chromedriver_path = 'C://Users//automation//Videos//chrome-win64.exe'
    service = Service(chromedriver_path)
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()
print("*Browser launched successfully*")
print(driver.title)
time.sleep(5)
# Verify the Title of the Page
def test_verify_title(setup):
    driver = setup
    expected_title = "The Internet"
    #assert expected_title in driver.title
# Click on Checkboxes Link and Verify Checkbox Status
    #Themes = driver.find_element(By.XPATH,"//*[text()='Checkboxes']").click()
    # Click on Checkboxes link
    checkboxes_link = driver.find_element(By.XPATH,"//*[text()='Checkboxes']")
    checkboxes_link.click()
    
    # Verify the text on the page
    expected_text = "Checkboxes"
    assert expected_text in driver.find_element_by_tag_name("h3").text
    
    # Verify checkbox statuses
    assert not is_checkbox_checked(driver, 1)  # Checkbox 1 should not be checked
    assert is_checkbox_checked(driver, 2)      # Checkbox 2 should be checked

def is_checkbox_checked(driver, index):
    checkbox = driver.find_element_by_xpath(f"//form/input[{index}]")
    return checkbox.is_selected()
#4. Task 3: Navigate Back to Home Page and Click on File Upload Link

def test_file_upload(setup):
    driver = setup
    
    # Navigate back to Home page
    driver.back()
    # Click on File Upload link
    file_upload_link = driver.find_element_by_link_text("File Upload")
    file_upload_link.click()
    
    # Verify the text on the page
    expected_text = "File Uploader"
    assert expected_text in driver.find_element_by_tag_name("h3").text
    
    # Click on Choose File button (Assuming file upload functionality)
    choose_file_button = driver.find_element_by_id("file-upload")
    choose_file_button.send_keys("C:/Users/automation/Videos/python.txt")  # Replace with your file path
    
    # Click on Upload button
    upload_button = driver.find_element_by_id("file-submit")
    upload_button.click()
    