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

# import the "csv" library, which will give us lots of handy code recipes
# for dealing with our data file
import csv

# open is a built-in function that takes a file name and
# a "mode" as parameters. In this example, the file
# `202009CitibikeTripdataExample.csv` should be in the same folder
# as our Python script or notebook. Values for the mode can be
# "r" for "read" or "w" for "write"
source_file = open("./data/202009-citibike-tripdata.csv","r")

# pass our source_file as an ingredient to the the `csv` library's
# DictReader "recipe".
# Store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)

# the DictReader function has added some useful information to our data,
# like a label that shows us all the values in the first or "header" row
print(citibike_reader.fieldnames)

# from the output of the `print()` statement, we can see that
# the exact label for the "User Type" column is `usertype`
