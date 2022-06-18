# Logical statements
question = 12*8
solution == 96

question == solution
#Output
True #boolean

price = 2.25
price > 5
#output
False

name = 'bayes'
name != 'Bayes' # it's not equal 

# Using logical in Dataframes
credit_records[credit_records.price > 20] # will select all the rows in credit_recods that the price (column) is > than 20

credit_records[credit_recods.suspects == 'Ronald Aylmer  Fisher']

# Is plate1 equal to "FRQ123"?
print(plate1 == "FRQ123")

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)
  
  
