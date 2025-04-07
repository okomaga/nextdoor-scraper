# 🕵️‍♂️ nextdoor-scraper

A Python-based web scraper that extracts **company names**, **emails**, and **websites** (if available) from up to 100 business pages on [Nextdoor.com](https://nextdoor.com).

Collected data is exported to an Excel file for further analysis.  
Useful for local business research, lead generation, or exploratory data collection in a geographic context.

> ⚠️ **Important:** Nextdoor may block your IP if too many requests are sent in a short time. It's highly recommended to use a **VPN or proxy** to avoid rate-limiting or being blocked.

---

## 🔧 Tech Stack

- Python  
- **Selenium** (web automation)  
- `re` (**regular expressions**)  
- **openpyxl** (Excel export)

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install selenium openpyxl
```

Also install the appropriate WebDriver (e.g. [ChromeDriver](https://sites.google.com/chromium.org/driver/)) and make sure it’s in your system `PATH`.

---

## 2. Prepare Input File

Add up to **100 Nextdoor business page URLs** (one per row) into the following file:

```bash
data/nextdoor_urls.xlsx
```

---

## 3. Run the Script

```bash
python nextdoor_data_scraper.py
```

## 📁 Output Columns

- **Company Name**  
- **Email** (if found)  
- **Website** (if listed)  
- **Source URL** (the page scraped)

The data will be saved into an Excel file in the `output/` directory.

---

## 💼 Sample Use Case

- Lead generation for local business outreach  
- Business intelligence collection in neighborhood economies  
- Input source for geolocation-based marketing  
- Practice in Selenium-based scraping and structured output formatting

---

## 📜 License

This project is licensed under the **MIT License**.
