from Scraping.driver_setup import create_driver
from Scraping.google_sheet_handler import setup_google_sheet
# from services.keyword_extractor import extract_keywords
import openai
from Scraping.job_scrapper import scrape_naukri_jobs
from utils.logger import log

def main():
    log("Starting AI Job Scraper...")

    driver = create_driver()
    sheet = setup_google_sheet()

    scrape_naukri_jobs(driver, sheet)
    # Step 1: Get Job Descriptions
    # job_descriptions = get_job_descriptions()
    # print(f"🔍 Found {len(job_descriptions)} job descriptions")

    # Step 2: Extract Keywords
    # keywords = extract_keywords(job_descriptions)
    # print(f"🧠 Extracted {len(keywords)} keywords: {keywords}")
    # generate_resumes_from_sheet()
    driver.quit()
    log("✅✅✅ All jobs inserted successfully into Google Sheet!")

if __name__ == "__main__":
    main()
    log("AI Job Scraper finished.")