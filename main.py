from telethon import TelegramClient, events
import asyncio
import csv
import os
from datetime import datetime

# Configuration
CSV_FILE = 'telegram_users.csv'

# Your API credentials from https://my.telegram.org/
api_id = ''  # Replace with your API ID
api_hash = ''  # Replace with your API hash

# Groups to monitor
groups_to_monitor = [
    'GP1',
    'GP2',
    # Add more groups as needed
]

# Initialize the client
client = TelegramClient('session_name', api_id, api_hash)

def initialize_csv():
    """Check if CSV exists, create it with headers if not."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'username', 'first_name', 'last_name', 'group_name', 'date_collected', 'message_sent'])

async def save_user_to_csv(user, group_name):
    """Add user to CSV if not already present."""
    # Check if user already exists in CSV
    user_exists = False
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                if row and row[0] == str(user.id):
                    user_exists = True
                    break
    
    # Add user if not exists
    if not user_exists:
        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                user.id,
                user.username if hasattr(user, 'username') and user.username else '',
                user.first_name if hasattr(user, 'first_name') and user.first_name else '',
                user.last_name if hasattr(user, 'last_name') and user.last_name else '',
                group_name,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'No'  # Message sent status
            ])
        return True
    return False

@client.on(events.NewMessage(chats=groups_to_monitor))
async def handler(event):
    """Handle new messages in monitored groups."""
    try:
        # Get the sender
        sender = await event.get_sender()
        
        # Get the chat where the message was sent
        chat = await event.get_chat()
        group_name = getattr(chat, 'title', str(chat.id))
        
        # Save user to CSV
        user_added = await save_user_to_csv(sender, group_name)
        
        if user_added:
            print(f"Added user {sender.id} ({getattr(sender, 'username', 'No username')}) from {group_name} to CSV")
        
    except Exception as e:
        print(f"Error handling message: {e}")


async def main():
    """Main function to run the client."""
    # Initialize CSV file
    initialize_csv()
    
    await client.start()
    print("Client is running...")
    print(f"Monitoring {len(groups_to_monitor)} groups")
    print(f"Saving user data to {CSV_FILE}")
    
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
