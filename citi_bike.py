# Question: How many Citi Bike rides each day are taken by subscribers versus "customers"?

# Answer: Choose a single day of rides to examine. The data set located here: XXXXX was generated from the original system data found here: https://s3.amazonaws.com/tripdata/index.html -> 202009-citibike-tripdata.csv.zip

# Program Outline:
# 1. Read in the data file: 202009CtibikeTripdataExample.csv
# 2. Create variables to count: subscribers, customers and other
# 3. For each row in the file:
#       a. If the "User Type" is "Subscriber" add 1 to "subscriber_count" variable
#       b. If the "User Type" is "Customer" add 1 to "customer_count" variable
#       c. Otherwise, add 1 to the "other" variable
# 4. Print out my results
