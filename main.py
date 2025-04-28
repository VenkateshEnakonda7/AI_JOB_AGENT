from Scraping.driver_setup import create_driver
from Scraping.google_sheet_handler import setup_google_sheet
from Scraping.job_scrapper import scrape_naukri_jobs
from utils.logger import log

def main():
    log("Starting AI Job Scraper...")

    driver = create_driver()
    sheet = setup_google_sheet()

    scrape_naukri_jobs(driver, sheet)

    driver.quit()
    log("✅✅✅ All jobs inserted successfully into Google Sheet!")

if __name__ == "__main__":
    main()
    log("AI Job Scraper finished.")