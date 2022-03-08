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

# now we'll create our three variables to hold the count of each type of Citi Bike
# user, beginning the count for each at zero
subscriber_count = 0
customer_count = 0
other_user_count = 0

# we want to make sure our for loop is working with the data that's already
# been transformed by our DictReader recipe
# so for Step 3, we'll write a `for...in` loop
# using our `citibike_reader` variable
for a_row in citibike_reader:

    # in order for my `if` statements to be "inside" my loop,
    # they have to be indented one more `tab` to the right

    # Step 3a: if the value in the `usertype` column of
    # the current row is "Subscriber"
    if a_row["usertype"] == "Subscriber":

        # indenting one more time so that this next line only happens if
        # `usertype` actually _is_ "Subscriber"
        subscriber_count = subscriber_count +1

    # Step 3b:because we need to use `else` here, but also need
    # another "if" statement, we're using the keyword `elif`,
    # which is short for "else if"
    elif a_row["usertype"] == "Customer":

        # indenting again so that this next line only happens if
        # `usertype` actually _is_ "Customer"
        customer_count = customer_count + 1

    #Step 3c: in this case, we're not checking for anything,
    # we just know that the `usertype` value is neither
    # "Subscriber" nor "Customer", so we'll add one to our catch-all
    # "other" category
    else:
        other_user_count = other_user_count + 1

print("Number of subscribers:")
print(subscriber_count)
print("Number of customers:")
print(customer_count)
print("Number of 'other' users:")
print(other_user_count)
