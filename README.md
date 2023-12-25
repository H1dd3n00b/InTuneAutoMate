# InTuneAutoMate
This Python script automates security scans and updates within the Microsoft Intune environment.

## Description

IntuneAutoMate is designed to perform automated security scans, update Windows Defender security intelligence, and synchronize devices in the Microsoft Intune platform. It interacts with the Intune web interface using Selenium.

It performs the following actions, in the following order:

- **Update Windows Defender Security Intelligence, followed by a 3 second pause**
- **Full Scan**
- **Quick Scan**

The script operates interactively, simulating user actions in the Microsoft Intune environment. Using Selenium's automation features, IntuneAutoMate seamlessly conducts security scans and updates. Simply provide a file listing the machines to be scanned, allowing you the freedom to step away for a coffee break. Upon your return, the scans will be seamlessly completed.

## Usage
```
1. Clone the repository:
git clone https://github.com/H1dd3n00b/IntuneAutoMate.git
2. Navigate to the directory:
cd IntuneAutoMate
3. Install the necessary dependencies:
pip install -r requirements.txt
4. Run the script:
python IntuneAutoMate.py <file.txt>
Replace `<file.txt>` with the path to your text file containing device names, each on a separate line.
5. Follow the script prompts; you will be asked for an email and password. These credentials will be used to execute the script actions.
```
## 

## Potential Issues

Please note that all machines listed in the input file will be converted to capital letters before being processed by the script. For instance, 'machine123' will be transformed into 'MACHINE123'. **This conversion is intentional** since the Microsoft Intune platform recognizes Windows devices exclusively in capital letters.

If this behavior conflicts with your device naming convention or if you encounter issues due to case sensitivity, you can modify the script's behavior. Navigate to line 69 in the script:
findmachine = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, machine.upper())))

To accommodate different naming conventions, adjust the line to use the original machine name without converting it to uppercase:
findmachine = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, machine)))

Feel free to modify the script according to your requirements and device naming conventions.

### Compatibility

This script has been thoroughly tested on Windows 10 and Windows 11 devices. Please note that it is designed specifically for these operating systems and their respective environments.

**Compatibility Limitation:** 
The script may not function as intended on mobile devices, including phones, or on other operating systems. It is optimized for Windows environments and their unique configurations.
