**5/26/25**  
- After visiting the PeMS website, I've decided to choose the Playwright library for my task of webscraping thanks to it's accessibility and ease of use for dynamic websites like the PeMS dataset.
  - Documentation can be found here: https://playwright.dev/python/docs/library
- I've succesfully automated log-in to the PeMS website and plan on fully automating the workflow from ID collection to data storage.  
**5/27/25**  
- I generalized the process of viewing all the station ids, by concatenating a special **string** at the end of the URL.
- For extracting the station IDs, I had some help from ChatGPT to find all the clickable station links and scrape for the IDs to be stored in an **array**.
- I've decided to track whether a station has truck flow or not by storing binary values in a **hashmap** with the station id as key and the binary value as the paired value.
