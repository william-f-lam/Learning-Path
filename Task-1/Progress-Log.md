**5/26/25**  
- After visiting the PeMS website, I've decided to choose the Playwright library for my task of webscraping thanks to it's accessibility and ease of use for dynamic websites like the PeMS dataset.
  - Documentation can be found here: https://playwright.dev/python/docs/library
- I've succesfully automated log-in to the PeMS website and plan on fully automating the workflow from ID collection to data storage.  

**5/27/25**  
- I generalized the process of viewing all the station IDs, by concatenating a special **string** at the end of the URL.
- For extracting the station IDs, I had some help from ChatGPT to find all the clickable station links and scrape for the IDs to be stored in an **array**.
- With this array of IDs, I've decided to track whether a station has truck flow or not by storing binary values in a **hashmap** with station IDs as keys and paired binary values, all stored inside an outer **list**.
  
**6/4/25**
- After checking for truck flow, I now automated the process for viewing the data in table form, then saving the HTML code in an interpretable Excel file.
- The task is complete for now and I will revisit it in the future to scale for passenger and truck flow in the SCAQMD jurisdiction.
