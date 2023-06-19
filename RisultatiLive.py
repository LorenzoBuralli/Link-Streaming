import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException, TimeoutException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import win32gui, win32con
import os

def main():
    # Set browser options for incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Path to the Chrome driver (make sure to download and place it in the same directory)
    chrome_driver_path = os.path.join(os.getcwd(), "chromedriver_win32", "chromedriver.exe")

    # Path to the AdBlock extension file (make sure to download and place it in the same directory)
    adblock_extension_path = os.path.join(os.getcwd(), "extension_1_50_0_0.crx")

    # Websites to open
    site_web = [
        "https://www.google.com/search?q=firstrow+calcio",
        "https://www.google.com/search?q=calcio+ga",
        "https://www.google.com/search?q=Stream2watch",
        "https://www.google.com/search?q=pepperlive",
        "https://www.google.com/search?q=socceron"
    ]

    # Open a new Chrome window in incognito mode with the AdBlock extension
    chrome_options.add_extension(adblock_extension_path)
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

    # Maximize the browser window
    driver.maximize_window()

    # Open the first website and refresh to trigger opening of other websites
    first_website = "https://www.google.com/search?q=firstrow+calcio"
    driver.get(first_website)

    # Perform code to interact with the first website
    try:
        element = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "W0wltc")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except TimeoutException:
        pass

    # Function to open a website in a new tab
    def open_website(url):
        try:
            if "://" not in url:
                raise InvalidArgumentException("Invalid URL")
            driver.execute_script(f"window.open('{url}');")
        except InvalidArgumentException:
            pass

    # Open the remaining websites in separate tabs after 1 second
    for i, site in enumerate(site_web):
        if site != first_website:
            threading.Timer(1, open_website, args=[site]).start()

    # Wait for all tabs to open
    time.sleep(1)

    # Refresh the first tab (index 0)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()

    # Wait for all tabs to load completely
    try:
        WebDriverWait(driver, 0).until(lambda driver: len(driver.window_handles) == len(site_web))
    except TimeoutException:
        pass

    # Check if there are at least 6 tabs open
    if len(driver.window_handles) >= 6:
        # Switch to the sixth tab (index 5)
        driver.switch_to.window(driver.window_handles[5])
    else:
        # Open a new tab and switch to it
        driver.execute_script("window.open();")
        driver.switch_to.window(driver.window_handles[-1])

    # Open the "chrome://extensions/?id=cjpalhdlnbpafiamejdnhcphjbkeiagm" page in the fourth tab
    driver.get('chrome://extensions/?id=cjpalhdlnbpafiamejdnhcphjbkeiagm')
    time.sleep(1)
    action = ActionChains(driver)

    # Flip the switch that enables it in incognito
    for _ in range(5):
        action.send_keys(Keys.TAB).perform()
    action.send_keys(Keys.RETURN).perform()

    # Switch back to the last tab
    driver.switch_to.window(driver.window_handles[5])

    # Close the fifth tab
    driver.close()

    # Switch back to the first tab
    driver.switch_to.window(driver.window_handles[0])

    # Continue executing the script as long as the browser window is open
    while True:
        try:
            driver.title  # Check the state of the window
        except NoSuchWindowException:
            break

    # Close the browser window
    driver.quit()

if __name__ == "__main__":
    # Hide the console
    hide_console = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hide_console, win32con.SW_HIDE)

    # Execute the main script
    main()
