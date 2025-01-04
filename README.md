# Pinterest Scraper

This project is a web scraping tool that automates the process of logging into Pinterest, searching for a topic, and downloading images from pins. It uses `selenium` for browser automation and `BeautifulSoup` for parsing HTML content.

---

## Features

- **Automated Login**: Logs into Pinterest using provided credentials.
- **Search**: Searches for a user-specified topic on Pinterest.
- **Scraping**: Collects and downloads images from pins found in the search results.
- **Cookie Management**: Saves and uses cookies for session persistence.
- **Error Logging**: Captures errors and writes them to a log file.

---

## Prerequisites

- Python 3.8+
- Google Chrome
- ChromeDriver
- Virtual Environment (optional but recommended)

---

### Set up .```env``` file

```bash
email_="your_email@example.com"
password_="your_password"
url="https://www.pinterest.com"
topic_="your_search_topic"
pages=5
```
___
### Project directory
```bash
.
├── main.py           # Main entry point for the script
├── login.py          # Handles login and cookie management
├── cleaner.py        # Contains scraping logic and helper functions
├── base.log          # Log file generated during execution
├── data/             # Directory where scraped images are stored
├── .env              # Environment variables
└── requirements.txt  # Python dependencies
```
___
### Run the script

linux
```
python3 main.py
```
windows 
```
py main.py
```
