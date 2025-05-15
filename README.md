# instagram_auto_like_msg

**instagram_auto_like_msg** is a Python automation script that utilizes the Selenium WebDriver to interact with Instagram. The script performs the following actions:

- **Login to Instagram**: Automates the login process using provided credentials.
- **Like the First Photo**: Navigates to the Instagram feed and likes the first photo that appears.
- **Send Message to Latest Sender**: Accesses the Direct Messages and sends a predefined message to the most recent conversation.

## 🚀 Features

- Automates Instagram interactions to save time.
- Easy to configure with minimal setup.
- Utilizes Selenium for browser automation.

## 🛠️ Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Google Chrome**: The script is configured to work with the Chrome browser.
- **ChromeDriver**: Compatible version of ChromeDriver must be installed and added to your system's PATH.

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/instagram_auto_like_msg.git
cd instagram_auto_like_msg
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install selenium
```

3. **Download ChromeDriver**:

- Find your Chrome browser version by navigating to `chrome://version/`.
- Download the corresponding ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Add the ChromeDriver executable to your system's PATH.

## 🚀 Usage

1. **Configure Credentials**:

- Open the `instagram_auto_like_message.py` file.
- Locate the section where Instagram credentials are set.
- Replace the placeholder values with your actual Instagram username and password.

2. **Run the Script**:

```bash
python instagram_auto_like_message.py
```

The script will:

- Open a Chrome browser window.
- Log in to Instagram.
- Like the first photo on your feed.
- Send a message to the latest sender in your Direct Messages.

## ⚠️ Disclaimer

This script is intended for educational and personal use only. Automating interactions with websites may violate their terms of service. Use responsibly and at your own risk.
