# Why select a column?

# We can use for calculation
credit_records.price.sum()

# plot
plt.plot(ransom['letter'], ransom['frequency'])

# select with brackets and string
suspect = credit_records['suspects'] # we use quotation mark
print(suspect) # we can see all values for this particular column

# select with dot
price = credit_records.price
print(price) # we can see all values for the price column

#IMPORTANT -> With the column has space eg. 'Golden Retriever', we must use brackets and quotation marks to select the column
#eg.01

# Select the column item from credit_records
# Use brackets and string notation
items = credit_records['item']

# Display the results
print(items)

# OR

# Select the column item from credit_records
# Use dot notation
items = credit_records.item

# Display the results
print(items)

# INSPECT A FILE
# Use info() to inspect mpr
print(mpr.info())
       
