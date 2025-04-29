import time
import re
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
from services.gpt_resume_modifier import generate_resumes_from_sheet




def scrape_naukri_jobs(driver, sheet):
    driver.get("https://www.naukri.com/jobs-in-india")
    time.sleep(2)

    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='close']"))
        )
        close_button.click()
    except Exception:
        log("No pop-up appeared.")

    # Search for the job
    driver.find_element(By.CLASS_NAME, "nI-gNb-sb__main").click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/input"))
    )
    search_box.send_keys("Automation Testing,API Testing,API Automation Testing")
    time.sleep(2)
    dropdown_element = driver.find_element("id", "experienceDD")  # or By.NAME, By.XPATH, etc.
    dropdown_element.click()
    exp= driver.find_element(By.XPATH, "//*[@id='sa-dd-scrollexperienceDD']/div[1]/ul/li[4]")
    exp.click()
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    n = 0
    while n < 1:
        log(f"Scraping page {n}...")
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')
        log(f"Number of job cards found: {len(job_cards)}")

        for job in job_cards:
            try:
                title = job.find('a', class_='title').text.strip()
                company = job.find('a', class_='comp-name mw-25').text.strip()
                experience = job.find('span', class_='expwdth').text.strip()
                salary = job.find('span', class_='ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal').text.strip()
                location = job.find('span', class_='locWdth').text.strip()
                posted_text = job.find('span', class_='job-post-day').text.strip()

                match = re.search(r'(\d+)\s+day', posted_text.lower())
                days_ago = int(match.group(1)) if match else 0
                posted_date = datetime.now() - timedelta(days=days_ago)
                posted_date_str = posted_date.strftime('%Y-%m-%d')

                link = job.find('a', class_='title').get('href')
            except Exception as e:
                log(f"Error extracting job details: {e}")
                continue

            # Open job link to extract description
            driver.execute_script("window.open(arguments[0], '_blank');", link)
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)

            try:
                job_description = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "styles_JDC__dang-inner-html__h0K4t"))
                ).text.strip()
                resume = generate_resumes_from_sheet(job_description)
            except Exception:
                job_description = "No description available"

            driver.close()
            driver.switch_to.window(driver.window_handles[0])

            # Save to sheet
            sheet.append_row([title, company, experience, salary, location, posted_date_str, link, job_description,resume])
            log(f"✅ Inserted: {title} - {company}")

        try:
            next_button = driver.find_element(By.XPATH, "//*[@id='lastCompMark']/a[2]")
            next_button.click()
            n += 1
            time.sleep(5)
        except Exception:
            log("No next button. Ending scraping.")
            break
