High Level Description:  
  
1. Develop a statistical or machine learning (ML) model that, given an OD (origin-destination) pair as input, predicts a probability distribution over the top five most likely next destinations after arriving at the input destination.

Low Level Description:  

1. Read the file for California Census Tracts and convert to the WGS84 coordinate system.
  - https://catalog.data.gov/dataset/tiger-line-shapefile-2021-state-california-census-tracts 
2. Read the file for UCR UCR AI-Energy Nexus Laboratory dataset for trip and stop activities.
3. Iterate over CSV files from UCR dataset.
4. For each CSV file, create spatial points from the given latitude longitude pair.
5. Spatial join to see if the points are within California's shapefile, and map to appropriate GEOIDs, otherwise discard for Nevada points.
6. For each origin GEOID and its destination GEOID, track its next destinations and increment a counter to that second destination GEOID.
7. Store results in JavaScript Object Notation (JSON), counting the number of times an OD pair GEOID visits a given destination GEOID.
8. Given an input OD pair, provide the five most likely destinations based on JSON results.
