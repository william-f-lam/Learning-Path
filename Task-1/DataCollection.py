import pandas as pd
from playwright.sync_api import sync_playwright
import Task1Credentials

def main():
    with sync_playwright() as p:
        station_ids = []

        # Open PeMS website.
        try:
            browser = p.chromium.launch(headless = False, slow_mo = 50)
            page = browser.new_page()
            page.goto("https://pems.dot.ca.gov/")
        except:
            print("Could not open browser or enter webpage.")

        # Log-in to PeMS website.
        try:
            page.locator("#username").fill(Task1Credentials.username)
            page.locator("#password").fill(Task1Credentials.password)
            page.click("input[name=login]")
        except:
            print("Log-in Failed")

        # Enter the report finder for I-5N, District 7, Stations dataset.
        try: 
            page.select_option("select#rptFinderFwy_fwy", value = "5")
            page.select_option("select#rptFinderFwy_location", value = "7")
            page.select_option("select#rptFinderFwy_report_type", label = "Stations")
        except:
            print("Failed to view station IDs.")
        
        # Store all station IDs for I5-N, District 7, Stations.
        try:
            page.wait_for_selector("th:has-text('ID')")
            page.goto(page.url + "&pagenum_all=1")

            # Credit to ChatGPT for helping find the station IDs.
            links = page.locator("a[href*='station_id=']")
            for i in range(links.count()):
                text = links.nth(i).inner_text().strip()
                if text.isdigit():
                    station_ids.append(text)
        except:
            print("Failed to store all station IDs.")
        finally:
            browser.close()

if __name__ == "__main__":
    main()

    
