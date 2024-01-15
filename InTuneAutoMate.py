#!/bin/python3

import sys
import base64
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style
import time

init()  # This line makes colorama work


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python script.py <file.txt>{Style.RESET_ALL}")
        sys.exit(1)

    InputFile = sys.argv[1]
    AccountName = input(
        f"{Fore.GREEN}Enter your admin account email: {Style.RESET_ALL}")
    Password = input(
        f"{Fore.GREEN}Enter your admin account password: {Style.RESET_ALL}")

    # Encode the above provided credentials for slightly better security
    encoded_account = base64.b64encode(
        AccountName.encode("utf-8")).decode("utf-8")
    encoded_password = base64.b64encode(
        Password.encode("utf-8")).decode("utf-8")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get("https://endpoint.microsoft.com")

    # Log into InTune
    try:
        AccInput = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "i0116")))
        AccInput.send_keys(base64.b64decode(encoded_account).decode("utf-8"))
        AccInput.send_keys(Keys.RETURN)
        PassInput = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "i0118")))
        PassInput.send_keys(base64.b64decode(encoded_password).decode("utf-8"))
        PassInput.send_keys(Keys.RETURN)
        StaySignedIn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idBtn_Back")))
        StaySignedIn.click()
    except TimeoutException as e:
        try:
            OtherWaysToSignIn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "idA_PWD_SwitchToCredPicker")))
            OtherWaysToSignIn.click()
            PasswordSelect = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By. CSS_SELECTOR, "#credentialList > div:nth-child(3) > div > div")))
            PasswordSelect.click()
            PassInput = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "i0118")))
            PassInput.send_keys(base64.b64decode(
                encoded_password).decode("utf-8"))
            PassInput.send_keys(Keys.RETURN)
            StaySignedIn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "idBtn_Back")))
            StaySignedIn.click()
        except TimeoutException:
            print(f"{Fore.LIGHTRED_EX}Oopsie, something went wrong!")
            print(f"{Fore.LIGHTMAGENTA_EX}The script encountered an error:")
            print(f"{e}{Style.RESET_ALL}")
            print(f"{Fore.LIGHTYELLOW_EX}Most likely reason:{Style.RESET_ALL}")
            print(
                f"{Fore.LIGHTRED_EX}Invalid or non-existent username/password combination!{Style.RESET_ALL}")
            sys.exit()

    # Function to perform actions on each machine

    def process_machine(machine):
        devices = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "_weave_e_58")))
        devices.click()
        alldevices = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'div[data-telemetryname="Menu-mDMDevicesPreview"]')))
        alldevices.click()
        iframe1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "_react_frame_2")))
        driver.switch_to.frame(iframe1)
        intunesearch = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SearchBox5")))
        intunesearch.click()
        intunesearch.send_keys(machine)
        findmachine = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, machine.upper())))
        findmachine.click()
        driver.switch_to.default_content()
        time.sleep(2)
        moreoptions = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'li[class="azc-toolbar-item azc-toolbarButton azc-toolbar-item-overflow fxs-commandBar-item fxs-commandBar-item-expandList"]')))
        moreoptions.click()
        updatewindowsthreatintelligence = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'div[title="Update Windows Defender security intelligence"]')))
        updatewindowsthreatintelligence.click()
        updatewindowsthreatintelligenceyes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'div[title="Yes"]')))
        updatewindowsthreatintelligenceyes.click()
        time.sleep(3)
        quickscan = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'li[title="Quick scan"]')))
        time.sleep(1)
        quickscan.click()
        quickscanyes = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[title="Yes"]')))
        quickscanyes.click()
        time.sleep(1)
        fullscan = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'li[title="Full scan"]')))
        fullscan.click()
        fullscanyes = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[title="Yes"]')))
        fullscanyes.click()
        sync = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li[title="Sync"]')))
        sync.click()
        syncupdateyes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, 'div[title="Yes"]')))
        syncupdateyes.click()
        home = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "_weave_e_40")))
        home.click()
        driver.refresh()
        print(f"{Fore.YELLOW}Done with {Fore.LIGHTRED_EX} {machine}")

    # Read machines from the file and process each one
    try:
        with open(InputFile, 'r') as file:
            machines = file.read().splitlines()
        for machine in machines:
            process_machine(machine)
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Oopsie, something went wrong! {Style.RESET_ALL}")
        print(f"{Fore.LIGHTMAGENTA_EX}\nThe script encountered an error:\n")
        print(f"{Fore.LIGHTRED_EX}{e}\n{Style.RESET_ALL}")
        print(f"{Fore.LIGHTYELLOW_EX}Potential Resolution:\n{Fore.LIGHTGREEN_EX}1. Check your internet connection.\n2. Ensure all necessary elements are present on the page and accessible.\n3. If using a virtual machine, maximize the screen for full visibility of page elements.\n4. Verify that every device in the input file is listed on a separate line.\n5. Close any unnecessary browser tabs/windows to optimize script execution.\n{Style.RESET_ALL}")

        print(f"{Fore.LIGHTGREEN_EX}Thanks for using my script!")
        print(
            f"For updates and more, please visit {Fore.RED} https://github.com/H1dd3n00b {Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}Have a great day!{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
