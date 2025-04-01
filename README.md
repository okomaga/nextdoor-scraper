nextdoor-scraper

This project extracts company names, emails, and websites (if available) from 100 business pages on Nextdoor.com. The scraped data is saved into an Excel file using Python and Selenium.

Tech Stack
	•	Python
	•	Selenium (for web automation)
	•	Regular Expressions (re)
	•	openpyxl (for Excel output)

Project Structure

nextdoor-scraper/  
├── README.md  
├── scraper.py  
├── data/  
│   └── nextdoor_urls.xlsx  
└── output/  
    └── nextdoor_data.xlsx

How to Run

1. Clone the Repository

git clone https://github.com/okomaga/nextdoor-scraper.git  
cd nextdoor-scraper

2. Install Dependencies

pip install selenium openpyxl

Also install the correct WebDriver (e.g., ChromeDriver) and ensure it’s in your system PATH.

3. Prepare Input File

Add your 100 Nextdoor URLs (one per row) into:

data/nextdoor_urls.xlsx

4. Run the Script

python scraper.py

Scraped data will be saved into:

output/nextdoor_data.xlsx

Output Columns
	•	Company Name
	•	Email (if found)
	•	Website (if listed)
	•	Source URL

License

This project is licensed under the MIT License.
