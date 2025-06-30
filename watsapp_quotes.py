import requests
from bs4 import BeautifulSoup
import random
import pywhatkit
import datetime
import time

# Step 1: Scrape quotes from a website
def get_motivational_quotes():
    url = "https://thestrive.co/motivational-quotes/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    for li in soup.find_all("li"):
        text = li.get_text(strip=True)
        if len(text) > 30 and not text.startswith("—"):
            quotes.append(text)
    return quotes

# Step 2: Pick a random quote
def get_daily_quote():
    quotes = get_motivational_quotes()
    return random.choice(quotes)

# Step 3: Send the quote via WhatsApp
def send_whatsapp_message(phone_number, message, hour, minute):
    print(f"Sending quote to {phone_number} at {hour}:{minute}...")
    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
    time.sleep(10)  # Wait to ensure message is sent

# Step 4: Main function
if __name__ == "__main__":
    # Replace with your WhatsApp number (with country code)
    phone_number = "+917022089693"

    # Set time to send (e.g., 9:00 AM)
    send_hour = 8
    send_minute = 0

    quote = get_daily_quote()
    send_whatsapp_message(phone_number, quote, send_hour, send_minute)




import schedule

def job():
    quote = get_daily_quote()
    send_whatsapp_message(phone_number, quote, send_hour, send_minute)

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
