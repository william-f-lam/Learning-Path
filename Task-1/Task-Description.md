High Level Description:  
  
1. Develop a Python script to automatically collect publically available data from the California Performance Measurement (PeMS) Data Source, specifically truck flow along I5-N, District 7 Stations.

Low Level Description:  

1. Open the pems.dot.ca.gov website.
2. Log into the website.
3. Enter the report finder for I-5N, District 7, Stations dataset.
4. View and store all IDs
5. For each ID, visit the time series performance aggreate.
6. While visiting time series data, note if truck flow is available.
7. If truck flow is available, view the table of data and save it to a data frame.
8. Save the data frame to an .xlsx file.
