# Telegram Group Monitor

A Python utility for monitoring Telegram groups and collecting user information. This tool uses the Telethon library to track participants across multiple designated groups, storing user data in a CSV file for later analysis or outreach.

![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Features

- Monitors multiple Telegram groups simultaneously
- Automatically collects user information (ID, username, first/last name)
- Tracks which group users were found in
- Stores data in a structured CSV format
- Foundation for implementing targeted message distribution

## Prerequisites

- Python 3.6 or higher
- Telegram account
- Telegram API credentials (API ID and API Hash)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telegram-group-monitor.git
   cd telegram-group-monitor
   ```

2. Install required dependencies:
   ```bash
   pip install telethon
   ```

3. Set up your Telegram API credentials (see [Getting Telegram API Credentials](#getting-telegram-api-credentials) below)

## Getting Telegram API Credentials

To use this script, you need to obtain API credentials from Telegram:

1. Visit [my.telegram.org](https://my.telegram.org/auth) and log in with your phone number
2. Click on "API Development Tools"
3. Fill in the required fields (you can use "Telegram Monitor" as the app title and "Monitoring tool" as the short description)
4. Click on "Create application"
5. You will receive an `api_id` and `api_hash` - copy these values

## Configuration

1. Open the script and replace the placeholder values with your actual API credentials:
   ```python
   api_id = 12345678  # Replace with your API ID
   api_hash = 'your_api_hash_here'  # Replace with your API hash
   ```

2. Modify the `groups_to_monitor` list to include the Telegram groups you want to monitor:
   ```python
   groups_to_monitor = [
       'group1',
       'group2',
       # Add more groups as needed
   ]
   ```

## Usage

1. Run the script:
   ```bash
   python telegram_monitor.py
   ```

2. The script will:
   - Create a CSV file named `telegram_users.csv` if it doesn't exist
   - Start monitoring all specified groups
   - Collect user information when messages are sent
   - Save unique users to the CSV file

3. The collected data will be stored in `telegram_users.csv` with the following columns:
   - `user_id`: Telegram user ID
   - `username`: Telegram username (if available)
   - `first_name`: User's first name (if available)
   - `last_name`: User's last name (if available)
   - `group_name`: Name of the group where the user was found
   - `date_collected`: Date and time when the user data was collected
   - `message_sent`: Status of whether a message has been sent to this user

## Implementing Message Distribution

The script includes a placeholder function `send_messages_to_saved_users()` that you can modify to implement targeted message distribution to collected users.

To use this functionality:

1. Uncomment and modify the example code in the function
2. Set up a separate script to run this function after collecting users
3. Ensure you comply with Telegram's terms of service regarding messaging users

## Customization

- **Change CSV File Name**: Modify the `CSV_FILE` variable to use a different filename
- **Adjust Monitoring Behavior**: Edit the event handler to collect different types of information
- **Add More Groups**: Simply add more group usernames to the `groups_to_monitor` list

## Running as a Background Service

To keep the script running continuously:

### Linux (using systemd)

1. Create a systemd service file:
   ```bash
   sudo nano /etc/systemd/system/telegram-monitor.service
   ```

2. Add the following content:
   ```
   [Unit]
   Description=Telegram Group Monitor
   After=network.target

   [Service]
   User=yourusername
   WorkingDirectory=/path/to/telegram-group-monitor
   ExecStart=/usr/bin/python3 /path/to/telegram-group-monitor/telegram_monitor.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable telegram-monitor.service
   sudo systemctl start telegram-monitor.service
   ```

### Windows

1. Create a batch file (run.bat):
   ```batch
   @echo off
   python telegram_monitor.py
   pause
   ```

2. Set up a scheduled task to run this batch file at system startup

## Important Notes

- This tool should be used responsibly and in accordance with Telegram's [Terms of Service](https://telegram.org/tos)
- Respect user privacy and data protection regulations in your region
- Avoid excessive automation that could trigger Telegram's anti-spam measures
- The tool doesn't collect message content, only user information from messages

## Keywords

Telegram, Python, Telethon, Data Collection, User Monitoring, Group Analysis, Marketing, Outreach, Automation, CSV, User Data

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
