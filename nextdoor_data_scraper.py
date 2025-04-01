import csv
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
import time

def extract_company_name(driver):
    """Extracts the company name using multiple approaches."""
    company = ""
    try:
        # First, try to get the text from the first <h1> element.
        company_h1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        company = company_h1.text.strip()
    except Exception:
        pass

    # If the extracted text is empty or contains promotional text, try using a meta tag.
    if not company or "Don't miss updates" in company:
        try:
            meta = driver.find_element(By.XPATH, "//meta[@property='og:title']")
            company = meta.get_attribute("content").strip()
        except Exception:
            company = driver.title.strip()

    # Clean up company name if it contains extra text after a dash.
    if ' - ' in company:
        company = company.split(' - ', 1)[0].strip()
    return company

def extract_info(driver, url):
    url = url.strip()
    try:
        driver.get(url)
        # Wait for the page's body to load completely
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        # Wait until document.readyState is complete
        WebDriverWait(driver, 15).until(lambda d: d.execute_script('return document.readyState') == 'complete')
        # Explicitly wait until at least one link is present
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href,'http')]") ))
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return "", "", "", url

    # Extract company name using the dedicated function
    company = extract_company_name(driver)

    # If company name is not captured, fallback to extracting from the URL
    if not company:
        parsed_url = urlparse(url)
        path_segments = [seg for seg in parsed_url.path.split('/') if seg]
        if path_segments:
            company = path_segments[-1].replace('-', ' ').title()
        else:
            company = url

    # ---- Email Extraction ----
    email = ""
    emails = []
    # Extract emails from mailto links
    mailto_links = driver.find_elements(By.XPATH, "//a[starts-with(@href, 'mailto:')]")
    for link in mailto_links:
        candidate = link.get_attribute('href').replace('mailto:', '').strip()
        if candidate:
            emails.append(candidate)

    # If no mailto email found, fallback to regex extraction on the page source
    if not emails:
        page_source = driver.page_source
        email_candidates = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', page_source)
        for candidate in email_candidates:
            if not candidate.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico')):
                emails.append(candidate)

        # If still no email, wait briefly and try again
        if not emails:
            time.sleep(2)
            page_source = driver.page_source
            email_candidates = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', page_source)
            for candidate in email_candidates:
                if not candidate.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico')):
                    emails.append(candidate)

    # Use the first valid email if available
    if emails:
        email = emails[0]
    else:
        email = "Not Found"

    # ---- Website Extraction ----
    website = ""
    websites = []
    try:
        links = driver.find_elements(By.XPATH, "//a[contains(@href,'http')]")
        for link in links:
            href = link.get_attribute('href')
            if href and "nextdoor" not in href.lower():
                websites.append(href.strip())
        # Use the first candidate if available; else leave blank
        if websites:
            website = websites[0]
    except Exception:
        pass

    return company, email, website, url

def main(input_csv, output_csv):
    # Initialize Selenium WebDriver (Chrome example).
    driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
    with open(input_csv, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader if row]
        if rows and rows[0][0].strip().lower() == 'url':
            rows = rows[1:]
        urls = [row[0] for row in rows]

    results = []
    for url in urls:
        print(f"Processing: {url}")
        company, email, website, url_extracted = extract_info(driver, url)
        results.append({
            'URL': url_extracted,
            'Company': company,
            'Website': website,
            'Email': email
        })

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Company', 'Website', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    driver.quit()

if __name__ == '__main__':
    input_csv = "urls_part_10.csv"
    output_csv = "output10.csv"
    main(input_csv, output_csv)