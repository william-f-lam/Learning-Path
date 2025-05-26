import pandas as pd
from playwright.sync_api import sync_playwright
import Task1Credentials

def main():
    with sync_playwright() as p:
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

        # Collect station IDs.
        try:
            # Enter the report finder for I-5N, District 7, Stations dataset.
            page.select_option("select#rptFinderFwy_fwy", value = "5")
            page.select_option("select#rptFinderFwy_location", value = "7")
            page.select_option("select#rptFinderFwy_report_type", label = "Stations")

            # View all IDs and store into a dataframe for later use.

        except:
            print("Failed to gather station IDs.")

if __name__ == "__main__":
    main()
