# Auto-Login Bot

This project is a simple tool built with Python that automatically logs you into websites. It uses the Selenium library to open a browser, go to a login page, type in your username and password, and log into your account.

## Features

1. Automates the login process for websites.
2. Handles username and password input fields.
3. Clicks the login button programmatically.
4. Verifies successful login with URL redirection.

## **Requirements**

Before running the bot, ensure you have the following installed on your system:

1. **Python 3.7 or later**  
   Download from [python.org](https://www.python.org/downloads/).

2. **Google Chrome**  
   Download from [google.com/chrome](https://www.google.com/chrome/).

3. **ChromeDriver**  
   - Must match your installed Chrome version.  
   - Download from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads).

4. **Python Libraries**  
   Install the required Python packages using:
   ```bash
   pip install selenium

## **How to Use**

Follow these steps to run the **Auto-Login Bot**:

### **1. Clone the Repository**
First, clone the repository to your local machine:
```bash

git clone https://github.com/dushyant4665/autologin_bot.git
cd autologin_bot 

```
2. Setup ChromeDriver
Download ChromeDriver that matches your Google Chrome version from here. Once downloaded, place the chromedriver.exe file in the project folder where the autologin_bot.py file is located.
3. Edit the Script
Open the autologin_bot.py file in a code editor and replace the placeholders with your credentials and the target website URL:
```bash

username.send_keys("your_username")  # Replace with your username
password.send_keys("your_password")  # Replace with your password
driver.get("https://example.com/login/")  # Replace with your login page URL

```
4. Run the Script
Once you have edited the script, run the following command to execute the bot:

```bash
python autologin_bot.py
```

5. Observe the Browser
After running the script, the bot will:

a. Open a Chrome browser.
b. Navigate to the login page specified in the script.
c. Automatically input the credentials and log you in.

## Project Structure

```bash
autologin_bot/
├── README.md          # Project documentation
├── autologin_bot.py   # Main script for the bot
├── chromedriver.exe   # ChromeDriver for browser automation
└── venv/              # Optional virtual environment (if used)
```

## Important Notes 

1. Security: Avoid storing sensitive credentials directly in the script. Use environment variables for better security.
2. Website Restrictions: Some websites may block automated logins using CAPTCHA or other techniques.
3. Ethical Use: Use this bot responsibly and only on websites you own or have explicit permission to access.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request with your enhancements.

## License


