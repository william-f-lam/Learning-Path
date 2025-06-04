High Level Description:  
  
1. Develop a statistical or machine learning (ML) model that, given an OD (origin-destination) pair as input, predicts a probability distribution over the top five most likely next destinations after arriving at the input destination.

Low Level Description:  

1. Iterate over the trip and stop activitiy of UCR AI-Energy Nexus Laboratory dataset and store origin, destination, and next destination for each stop in each CSV.
2. Store results in JavaScript Object Notation (JSON), counting the number of times an origin GEOID visits a given destination GEOID.
3. Given an input OD pair, provide the five most likely desintations based on JSON results.
