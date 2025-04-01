# nextdoor-scraper

This project extracts **company names**, **emails**, and **websites (if available)** from 100 business pages on [Nextdoor.com](https://nextdoor.com). The scraped data is saved into an Excel file using Python and Selenium.

> ⚠️ **Note:** Nextdoor may block your IP address if you send too many requests in a short time. It's highly recommended to use a VPN or proxy to avoid rate-limiting or being blocked during scraping.


## Tech Stack

- Python  
- Selenium (for web automation)  
- Regular Expressions (`re`)  
- openpyxl (for Excel output)

## How to Run

### Install Dependencies

```bash
pip install selenium openpyxl
```

Also install the correct WebDriver (e.g., ChromeDriver) and ensure it’s in your system PATH.

Prepare Input File

Add your 100 Nextdoor URLs (one per row) into:

data/nextdoor_urls.xlsx

Run the Script
``` bash
nextdoor_data_scraper.py
```
Output Columns
	•	Company Name
	•	Email (if found)
	•	Website (if listed)
	•	Source URL

License

This project is licensed under the MIT License.

