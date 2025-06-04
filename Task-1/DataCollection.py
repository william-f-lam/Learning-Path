import pandas as pd
from playwright.sync_api import sync_playwright
from io import StringIO
import Task1Credentials

def main():
    with sync_playwright() as p:
        station_ids = []
        base_url = "https://pems.dot.ca.gov/?dnode=VDS&content=loops&tab=det_timeseries&station_id="
        truck_flow_results = []

        # Open PeMS website.
        try:
            print("Opening browser.")
            browser = p.chromium.launch(headless = False, slow_mo = 0)
            page = browser.new_page()
            page.goto("https://pems.dot.ca.gov/")
        except:
            print("Could not open browser or enter webpage.")

        # Log-in to PeMS website.
        try:
            print("Logging in.")
            page.locator("#username").fill(Task1Credentials.username)
            page.locator("#password").fill(Task1Credentials.password)
            page.click("input[name=login]")
        except:
            print("Log-in Failed")

        # Enter the report finder for I-5N, District 7, Stations dataset.
        try: 
            print("Visiting I5-N, District 7, Stations.")
            page.select_option("select#rptFinderFwy_fwy", value = "5")
            page.select_option("select#rptFinderFwy_location", value = "7")
            page.select_option("select#rptFinderFwy_report_type", label = "Stations")
        except:
            print("Failed to view station IDs.")
        
        # Store all station IDs for I5-N, District 7, Stations.
        try:
            print("Storing Station IDs.")
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
        
        # For each station, check for and store truck flow data.
        with pd.ExcelWriter('Station_Data.xlsx', engine='openpyxl') as writer:
            for index, station in enumerate(station_ids):
                try:
                    print(f"Checking for truck flow data at station: {station}.")
                    page.goto(base_url + str(station))
                    page.wait_for_selector("select[id=q]")
                    page.select_option("select[id=q]", value = "truck_flow", timeout = 500)
                    truck_flow_results.append({"ID" :station, "Flow" : 1})
                except:
                    print("Truck flow not available at station: " + station + ".")
                    truck_flow_results.append({"ID" :station, "Flow" : 0})

                # Store truck flow of station in a new Excel page.
                if truck_flow_results[-1]["Flow"] == 1:
                    try:
                        # View truck flow data in table format.
                        page.wait_for_selector('select[id=q]', timeout=1000) 
                        page.select_option('select[id=q]', value='truck_flow', timeout=1000)
                        page.click('input[type="image"][alt="View Table"]')

                        # Scrape table of truck data.
                        table = page.wait_for_selector("table.inlayTable", timeout=10000)
                        page.wait_for_selector("table.inlayTable tbody tr", timeout=10000)
                        html = table.evaluate("node => node.outerHTML")

                        # Store data of truck flow.
                        scraped_data = pd.read_html(StringIO(html))[0]
                        scraped_data.to_excel(writer, sheet_name=str(station))

                        print(f"Successfully stored truck flow for station: {station}.")
                    except:
                        print(f"Could not store truck flow at station: {station}.")
        browser.close()
        print(truck_flow_results)
        df_truck_flow_results = pd.DataFrame(truck_flow_results)
        df_truck_flow_results.to_csv("Truck_Flow_Results.csv", index = False)
        

if __name__ == "__main__":
    main()
    
