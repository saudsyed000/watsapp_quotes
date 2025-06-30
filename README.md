# 💬 WhatsApp Motivation Bot

An automated Python bot that sends a daily motivational quote to your WhatsApp using `pywhatkit` and web scraping. Perfect for starting your day with inspiration—or sharing it with friends!

---

## 🚀 Features

- ✅ Scrapes fresh motivational quotes from the web
- ✅ Sends a random quote to a WhatsApp number at a scheduled time
- ✅ Easy to customize and extend
- ✅ Can be automated to run daily

---

## 🧰 Tech Stack

- Python 3
- [pywhatkit](https://pypi.org/project/pywhatkit/) – for WhatsApp messaging
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) – for web scraping
- `requests`, `datetime`, `random`

---

## 📦 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/watsapp-automator.git
   cd watsapp-automator
Install dependencies

bash
pip install -r requirements.txt
Create a .env file (optional for storing your phone number securely)

🧪 Usage
Open WhatsApp Web in your browser and stay logged in.

Run the script:

bash
python main.py
The bot will send a motivational quote to the configured number at the scheduled time.

🕒 Automation (Optional)
You can automate this script to run daily using:

schedule library in Python

Windows Task Scheduler

Linux/macOS cron jobs

📸 Demo
<!-- Optional: Add a screenshot of the bot in action -->

🙏 Acknowledgements
Quotes scraped from The STRIVE

Inspired by the need for daily positivity 💡

📜 License
MIT License. Feel free to use, modify, and share!

🤝 Contribute
Pull requests are welcome! If you have cool ideas (like adding a GUI or Telegram support), feel free to fork and build on it.
