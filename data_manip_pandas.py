#INTRODUCING NOTES

# FIRST CHAPTER - 1.1 Transforming Data 

# What's the point of pandas? 
# --> Data manipulation 
# --> Data visualization

# pandas is built of two essential Python Packages  -> Numpy and Matplotlib.

# EXPLORING A DATAFRAME : .head() (method)

x.head() # which returns the first few rows of the DataFrame, this becomes very useful if you have many rows

# info() (method)
x.info() # displays the name of columns, the data types they contain, and wether they have any missing values. 

# shape() (method)
x.shape # dataframe's shape attribute contains a tuple that holds the number of rows followed by numbers  of columns -> (r,c)

# .describe() (method) 
x.describe() # the describe method compute some summary statistics for numerical columns , like means, median and etc. 

# Components in a DataFrame - values, columns, index

# .values (attribute)
x.values # contains the data values in a 2-dimensional NumPy array

# .columns (attribute)
x.columns # the columns attribute contains columns names, and the index attribute contains row numbers or row names

# index
x.index # rows -> lembrar que começa a numeração do index 0 


# EXAMPLES

# Print the head of the homelessness data
print(homelessness.head())

# output 
              region       state  individuals  family_members  state_pop
0  East South Central     Alabama       2570.0           864.0    4887681
1             Pacific      Alaska       1434.0           582.0     735139
2            Mountain     Arizona       7259.0          2606.0    7158024
3  West South Central    Arkansas       2280.0           432.0    3009733
4             Pacific  California     109008.0         20964.0   39461588

print(homelessness.info())

#output
<class 'pandas.core.frame.DataFrame'>
Int64Index: 51 entries, 0 to 50
Data columns (total 5 columns):
region            51 non-null object
state             51 non-null object
individuals       51 non-null float64
family_members    51 non-null float64
state_pop         51 non-null int64

types: float64(2), int64(1), object(2)
memory usage: 2.4+ KB
None

print(homelessness.shape) #.shape it's a attribute not a function

#output
(51, 5)

print(homelessness.values) 

#output
[['East South Central' 'Alabama' 2570.0 864.0 4887681]
 ['Pacific' 'Alaska' 1434.0 582.0 735139]
 ['Mountain' 'Arizona' 7259.0 2606.0 7158024]
 ['West South Central' 'Arkansas' 2280.0 432.0 3009733]
 ['Pacific' 'California' 109008.0 20964.0 39461588]
 ['Mountain' 'Colorado' 7607.0 3250.0 5691287]
 ['New England' 'Connecticut' 2280.0 1696.0 3571520]
 ['South Atlantic' 'Delaware' 708.0 374.0 965479]
 ['South Atlantic' 'District of Columbia' 3770.0 3134.0 701547]
 ['South Atlantic' 'Florida' 21443.0 9587.0 21244317]
 ['South Atlantic' 'Georgia' 6943.0 2556.0 10511131]
 ['Pacific' 'Hawaii' 4131.0 2399.0 1420593]
 ['Mountain' 'Idaho' 1297.0 715.0 1750536]
 ['East North Central' 'Illinois' 6752.0 3891.0 12723071]
 ['East North Central' 'Indiana' 3776.0 1482.0 6695497]
 ['West North Central' 'Iowa' 1711.0 1038.0 3148618]
 ['West North Central' 'Kansas' 1443.0 773.0 2911359]
 .
 .
 .
 # vai ainda mais 
 
 print(homelessness.describe())
 # em cout -> quer dizer que tem 51 conteudos 
 #output
 count       51.000          51.000  5.100e+01
mean      7225.784        3504.882  6.406e+06
std      15991.025        7805.412  7.327e+06
min        434.000          75.000  5.776e+05
25%       1446.500         592.000  1.777e+06
50%       3082.000        1482.000  4.461e+06
75%       6781.500        3196.000  7.341e+06
max     109008.000       52070.000  3.946e+07
 
 
# FIRST CHAPTER - 1.1 Sorting and Subsetting
 #abordaremos os dois mais simples e possivelmente maneiras mais importantes de encontrar partes interessantes do seu DataFrame 
 # Primeira coisa que você pode fazer é alterar a ordem das linhas (rows) classificando-as (sorting theme) de forma que os dados mais interessantes fiquem no topo do DataFrame
 
 # You can sort rows (classificar as linhas) using the sort_values method, passing in column name that you want to sort by. 
 # examples -> 
 dogs.sort_values('weight_kg') # when we apply sort_values on the weight_kg column of the dogs DataFrame, we get the lightest (mais leve) at the top, and the heaviest dog at the bottom
 
 # with we setting the ascending argument to False will sort the data the other way around, from heaviest dog to lightest dog 
 dog.sort_values('weight_kg', ascending = False)
 
 #Sorting by multiples variables
 dogs.sort_values(['weight_kg', 'height_cm']) 
 
 # to change the direction values are sorted in, pass a list ascending argument to specify wich direction sorting should be done for each variable
 dogs.sort_values(['weight_kg', 'height_cm'], ascending = [ True, False]) # example 
 
 # subsetting columns (just zoom in on just one column)
 dogs['name'] 
 
 # subsetting multiple columns -> to select it, you need two pairs of square brackets
 dogs[['breed', 'height_cm']]
 
 # PS. lembrando que tem 2 brackets, pq o de fora corresponde ao subsetting do DataFrame, mas o de brackets de dentro é que criam a lista de nomes de colunas que iremos subsetar. 
 
 # Subsetting rows -> the most common way to subset it, is by creating a logical condition to filter against.
 #- for exemple -> let's find all the dogs whose height is greater than centimeters. 
 dogs['height_cm'] > 50  
 
 # output -> será um dataframe de boolens verificando quem é true e quem não é (True or False)
 

 # We can use the the logical condition inside of square brackets to subset the rows we're interested in to get all of the dogs taller than 50 cm. 
 # dará um dataframe topado com tudo que tem direito dos cachorros 
 dogs[dogs['height_cm'] > 50]
 
 # Subsetting rows based on text data 
 dogs[dogs['breed'] == 'Labrador'] # to filter the dogs that are Labradors
 

# subsetting rows based on dates
dogs[dogs['date_of_bith'] > '2015-01-01'] # só os animais que nasceram depois dessa data
# Subsetting rows based on multiple conditions
is_lab = [dogs['breed'] == 'Labrador'
is_brown = dogs['color'] == 'Brown'
dogs[is_lab & is_brown] # compilou os 2 e dará o cachorro que é labrador e marrom e toda as informações dele

           
# Subsetting using .isin() 
is_black_or_brown = dogs['color'].isin(['Black' , 'Brown'])
dogs[is_black_or_brown] # ai dará apenas cachorros com cor preta e marrom

 # exemples
Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
Print the head of the sorted DataFrame.

#sort homelessness by individual (vai pegar os lugares com os menores individuos
homelessness_ind = homelessness.sort_values('individuals') 
#print the top few rows
print(homelessness_ind.head())

          #output
                 region         state  individuals  family_members  state_pop
50            Mountain       Wyoming        434.0           205.0     577601
34  West North Central  North Dakota        467.0            75.0     758080
7       South Atlantic      Delaware        708.0           374.0     965479
39         New England  Rhode Island        747.0           354.0    1058287
45         New England       Vermont        780.0           511.0     624358
 
# exemple 02
#intructions 

Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam.
Print the head of the sorted DataFrame.
 
# sort homelessness bi descending family members 
 homelessness_fam = homelessness.sort_values('family_members', ascending = False)
print(homelessness_fam.head()) 

#exemple 03
Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.
Print the head of the sorted DataFrame

#sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region', 'family members'], ascending = [True, False])
print(homelessness_reg_fam.head()) 
 
#exemples

Create a DataFrame called individuals that contains only the individuals column of homelessness.
Print the head of the result.

#select the individuals column
individuals = homelessness['individuals']
print(individuals.head())
          #output
  0      2570.0
1      1434.0
2      7259.0
3      2280.0
4    109008.0

#exemples 

Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
Print the head of the result.
#select the state and famuly_members columns       
state_fam = homelessness[['state', 'family_members']]           
#print the head of the result             
print(state_fam.head())
          #output
                   state  family_members
    0     Alabama           864.0
    1      Alaska           582.0
    2     Arizona          2606.0
    3    Arkansas           432.0
    4  California         20964.0

          
          
# Subsetting rows  
#example 5 
  Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
#filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals'] > 10000]
print(ind_gt_10k) 
                 region       state  individuals  family_members  state_pop
    4              Pacific  California     109008.0         20964.0   39461588
    9       South Atlantic     Florida      21443.0          9587.0   21244317
    32        Mid-Atlantic    New York      39827.0         52070.0   19530351
    37             Pacific      Oregon      11139.0          3337.0    4181886
    43  West South Central       Texas      19199.0          6111.0   28628666
    47             Pacific  Washington      16424.0          5880.0    7523869
# exemple 06
          Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
#filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'] == 'Mountain']
print(mountain_reg)

          
#example 07
  # Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific")]

# See the result
print(fam_lt_1k_pac)

          #output
   region   state  individuals  family_members  state_pop
1  Pacific  Alaska       1434.0           582.0     735139
          
          
          
          
#example 08 
# subsetting rows by categorical variables 
Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result. 

# subsetet the rows in south atlantic or mid-atlantic regions
south_mid_atlantic = homelessness[homelessness['region'].isin[('South Atlantic', 'Mid-Atlantic'])]
 print(south_mid_atlantic)
             region                 state  individuals  family_members  state_pop
7   South Atlantic              Delaware        708.0           374.0     965479
8   South Atlantic  District of Columbia       3770.0          3134.0     701547
9   South Atlantic               Florida      21443.0          9587.0   21244317
10  South Atlantic               Georgia       6943.0          2556.0   10511131
20  South Atlantic              Maryland       4914.0          2230.0    6035802
30    Mid-Atlantic            New Jersey       6048.0          3350.0    8886025
32    Mid-Atlantic              New York      39827.0         52070.0   19530351
33  South Atlantic        North Carolina       6451.0          2817.0   10381615
38    Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922
40  South Atlantic        South Carolina       3082.0           851.0    5084156                                
          
 # example 09         
Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].isin(canu)]

# See the result
print(mojave_homelessness) 
         region       state  individuals  family_members  state_pop
    2   Mountain     Arizona       7259.0          2606.0    7158024
    4    Pacific  California     109008.0         20964.0   39461588
    28  Mountain      Nevada       7058.0           486.0    3027341
    44  Mountain        Utah       1904.0           972.0    3153550    
                                  
\
                               
                                  
                                  
 # FIRST CHAPTER 1.3 ADDING A NEW COLUMN     
dogs['height_m'] = dogs['heigh_cm']/100 # nesse caso aumentei uma coluna no dataframe dogs, a coluna de height_m
dog['bmi'] = dogs['weight_kg']/dogs['height_m']**2
                                  
print(dogs.head())
                                  
  #multiples manipulations
# exercicio de figure out the names of skinny, tall dogs 
#First we subset the dogs who have a BMI of under 100
                                  bmi_lt_100 = dogs[dogs['bmi'] < 100]
# next we sort the result in descending order of height to get the talles skinny dogs at the top 
                                  bmi_lt_100_height = dogs.sort_values('height_cm', ascending = False)
# finally we keep only the columns we're interested in 
                                  print(bmi_lt_100_height[['name', 'height_cm', 'bmi']] # vai dar de output apenas essas 3 colunas que representamos acima
  
                                        
#EXAMPLES
    Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
    Add another column to homelessness, named p_individuals, containing the proportion of homeless people in each state who are individuals.
                                       
 # ADD total col as sum of individuals and family_members
                                        homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

                                        
 # add p_individuals col as proportion of individuals 
                                        homelessness['p_individuals'] = homelessness['individuals']/homelessness['total']
                                        print(homelessness)
                                        
                                        
                                #output
                   region                 state  individuals  family_members  state_pop     total  p_individuals
0   East South Central               Alabama       2570.0           864.0    4887681    3434.0          0.748
1              Pacific                Alaska       1434.0           582.0     735139    2016.0          0.711
2             Mountain               Arizona       7259.0          2606.0    7158024    9865.0          0.736
3   West South Central              Arkansas       2280.0           432.0    3009733    2712.0          0.841
4              Pacific            California     109008.0         20964.0   39461588  129972.0          0.839
5             Mountain              Colorado       7607.0          3250.0    5691287   10857.0          0.701
6          New England           Connecticut       2280.0          1696.0    3571520    3976.0          0.573
7       South Atlantic              Delaware        708.0           374.0     965479    1082.0          0.654
8       South Atlantic  District of Columbia       3770.0          3134.0     701547    6904.0          0.546
9       South Atlantic               Florida      21443.0          9587.0   21244317   31030.0          0.691
10      South Atlantic               Georgia       6943.0          2556.0   10511131    9499.0          0.731
11             Pacific                Hawaii       4131.0          2399.0    1420593    6530.0          0.633
12            Mountain                 Idaho       1297.0           715.0    1750536    2012.0          0.645
13  East North Central              Illinois       6752.0          3891.0   12723071   10643.0          0.634
14  East North Central               Indiana       3776.0          1482.0    6695497    5258.0          0.718
15  West North Central                  Iowa       1711.0          1038.0    3148618    2749.0          0.622
16  West North Central                Kansas       1443.0           773.0    2911359    2216.0          0.651
17  East South Central              Kentucky       2735.0           953.0    4461153    3688.0          0.742
18  West South Central             Louisiana       2540.0           519.0    4659690    3059.0          0.830
19         New England                 Maine       1450.0          1066.0    1339057    2516.0          0.576
20      South Atlantic              Maryland       4914.0          2230.0    6035802    7144.0          0.688
21         New England         Massachusetts       6811.0         13257.0    6882635   20068.0          0.339
22  East North Central              Michigan       5209.0          3142.0    9984072    8351.0          0.624
23  West North Central             Minnesota       3993.0          3250.0    5606249    7243.0          0.551
24  East South Central           Mississippi       1024.0           328.0    2981020    1352.0          0.757
25  West North Central              Missouri       3776.0          2107.0    6121623    5883.0          0.642
26            Mountain               Montana        983.0           422.0    1060665    1405.0          0.700
27  West North Central              Nebraska       1745.0           676.0    1925614    2421.0          0.721
28            Mountain                Nevada       7058.0           486.0    3027341    7544.0          0.936
29         New England         New Hampshire        835.0           615.0    1353465    1450.0          0.576
30        Mid-Atlantic            New Jersey       6048.0          3350.0    8886025    9398.0          0.644
31            Mountain            New Mexico       1949.0           602.0    2092741    2551.0          0.764
32        Mid-Atlantic              New York      39827.0         52070.0   19530351   91897.0          0.433
33      South Atlantic        North Carolina       6451.0          2817.0   10381615    9268.0          0.696
34  West North Central          North Dakota        467.0            75.0     758080     542.0          0.862
35  East North Central                  Ohio       6929.0          3320.0   11676341   10249.0          0.676
36  West South Central              Oklahoma       2823.0          1048.0    3940235    3871.0          0.729
37             Pacific                Oregon      11139.0          3337.0    4181886   14476.0          0.769
38        Mid-Atlantic          Pennsylvania       8163.0          5349.0   12800922   13512.0          0.604
39         New England          Rhode Island        747.0           354.0    1058287    1101.0          0.678
40      South Atlantic        South Carolina       3082.0           851.0    5084156    3933.0          0.784
41  West North Central          South Dakota        836.0           323.0     878698    1159.0          0.721
42  East South Central             Tennessee       6139.0          1744.0    6771631    7883.0          0.779
43  West South Central                 Texas      19199.0          6111.0   28628666   25310.0          0.759
44            Mountain                  Utah       1904.0           972.0    3153550    2876.0          0.662
45         New England               Vermont        780.0           511.0     624358    1291.0          0.604
46      South Atlantic              Virginia       3928.0          2047.0    8501286    5975.0          0.657
47             Pacific            Washington      16424.0          5880.0    7523869   22304.0          0.736
48      South Atlantic         West Virginia       1021.0           222.0    1804291    1243.0          0.821
49  East North Central             Wisconsin       2740.0          2167.0    5807406    4907.0          0.558
50            Mountain               Wyoming        434.0           205.0     577601     639.0          0.679                                     
                                                
 #example combo-attack (tudo junto agora)
                                        
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state', 'indiv_per_10k']]

# See the result
print(result)   
 # WASHINGTON D.C. HAS THE HIGHEST NUMBER OF HOMELESS INDIVIDUALS                                       
                   state  indiv_per_10k
8   District of Columbia         53.738
11                Hawaii         29.079
4             California         27.624
37                Oregon         26.636
28                Nevada         23.314
47            Washington         21.829
32              New York         20.392

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                       
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
                                        
                                        #CHAPTER 02 - 2.0 SUMMARY STATISTICS 
 # Summarizing numerical data 
                                        dogs['heigh_cm'].mean() # tem outros como mean(), .median(), .min(), .max(), .mode(), var() (variance), std() (standard deviation), .sum(), .quantile() (calculate quantiles)
                                        
  # summarizing dates 
                                        #oldest dog:
                                        dogs['date_of_birth'].min() 
                                        #youngest dog:
                                        dogs['date_of_birth'].max()
                                        
# The agreggate or .agg() method 
                                        # allows you tu compute custom summary statistics 
                                        #example:
                                        # we create a function pct30 that computes the thirtieth percentile of a DataFrame column
                                        def pct30(column):
                                            return column.quantile(0.3)
                                        #now we can subset the weight column and call .agg passing the name of our function, pct30
                                        dogs['weight_kg'].agg(pct30)
                                        #output
                                        22.599999999999 #it gives us the thirtieth percentile of the dog's weight
                                        
# Summaries on multiple columns 
                                        dogs[['weight_kg', 'height_cm']].agg(pct30)
                                       #OUTPUT
                                        weight_ kg       22.6
                                        height_cm        45.4
                                        dtype: float64

                                        
#Multiple summaries
                                        def pct40(column): # computes the fortieth percentile called pct40
                                            return column.quantile(0.4) 
                                        
                                        def pct30(column): # computes the thirtieth percentile called pct30
                                            return column.quantile(0.3)
                                        dogs['weight_kg'].agg([pct30, pct40])
                                        #OUTPUT
                                        pct30         22.6
                                        pct40         24.0
                                        Name: weight_kg type: float64
                                        
                                        
# Cumulative sum
                                        dogs['weight_kg']                            
                                        0  24
                                        1  24
                                        2  24
                                        3  17
                                        4  29
                                        5  2
                                        6  74
                                        dogs['weight_kg'].cumsum() #soma acumulativa
                                        0  24
                                        1  48
                                        2  72
                                        3  89
                                        4  118
                                        5  120
                                        6  194
 # tem outros tbm como: cummax(), .cummin(), .cumprod()
                                        
                                        
                                                                               
 # mean() and median() -> The mean weekly sales amount is almost double the median weekly sales amount! This can tell you that there are a few very high sales weeks that are making the mean so much higher than the median.
 
 # Super summarizing! Taking the minimum and maximum of a column of dates is handy for figuring out what time period your data covers. In this case, there are data from February of 2010 to October of 2012.
 
                                        #example
                          # In the custom function for this exercise, "IQR" is short for inter-quartile range, which is the 75th percentile minus the 25th percentile. 
                          #  It's an alternative to standard deviation that is helpful if your data contains outliers. sales is available and pandas is loaded as pd. 
                                        # A custom IQR function
                                        def iqr(column):
                                            return column.quantile(0.75) - column.quantile(0.25)
                                        # print IQR of the temperature_c column
                                        print(sales['temperature_c'].agg(igr)
                                        #output
                                        16.583333333333336
                                        
                                              
                                        #exemple 2
                                       # A custom IQR function
                                       def iqr(column):
                                            return column.quantile(0.75) - column.quantile(0.25)

                                       # Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
                                       print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))
                                        
                                              #OUTPUT 
                                              temperature_c           16.583
                                              fuel_price_usd_per_l     0.073
                                              unemployment             0.565
                                              dtype: float64
                                    # example
                                              
                                    Update the aggregation functions called by .agg(): include iqr and np.median in that order.
                                    # Import NumPy and create custom IQR function
                                              import numpy as np
                                              def iqr(column):
                                                  return column.quantile(0.75) - column.quantile(0.25)
                                    # update to print IQR and median of temperature_c, fuel_price_usd_l, unemployment
                                              print(sales[['temperature_c', 'fuel_price_usd_l', "unemployment"]].agg([iqr, np.median]))
                                              
                                              #outupu
                                                      temperature_c  fuel_price_usd_per_l  unemployment
                                          iqr            16.583                 0.073         0.565
                                          median         16.967                 0.743         8.099
                                        
                                    # example 
                                    # Cumulative Statistics 
                                              Cumulative statistics can also be helpful in tracking summary statistics over time. In this exercise, you'll calculate the cumulative sum and cumulative max of a department's weekly sales, which will allow you to identify what the total sales were so far as well as what the highest weekly sales were so far. 
                                              # Sort sales_1_1 by date
                                              sales_1_1 = sales_1_1.sort_values('date')

                                              # Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
                                              sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()

                                              # Get the cumulative max of weekly_sales, add as cum_max_sales col
                                              sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()

                                              # See the columns you calculated
                                              print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])
                                              
                                                       date  weekly_sales  cum_weekly_sales  cum_max_sales
                                              0  2010-02-05      24924.50          24924.50       24924.50
                                              1  2010-03-05      21827.90          46752.40       24924.50
                                              2  2010-04-02      57258.43         104010.83       57258.43
                                              3  2010-05-07      17413.94         121424.77       57258.43
                                              4  2010-06-04      17558.09         138982.86       57258.43
                                              5  2010-07-02      16333.14         155316.00       57258.43
                                              6  2010-08-06      17508.41         172824.41       57258.43
                                              7  2010-09-03      16241.78         189066.19       57258.43
                                              8  2010-10-01      20094.19         209160.38       57258.43

                                             
                                              
                                              # CHAPTER 02 - 2.1 COUNTING
                                              
# Dropping Duplicate Names                                              
                                              vet_visits.drop_duplicates(subset = 'names') # tirará linhas do dataframe os nomes(que está na coluna do dataframe) duplicados 
                                              
                                              # mas pode ser que existe nomes iguais de dogs, então precisamos considerar mais itens, ai tem que pegar a raça (breed)
# Dropping Duplicate Pairs
                                              unique_dogs = vet_visits.drop_duplicates(subset = ['names', 'breed'])
                                              print(unique_dogs)
                                              
# To count the dogs of each breed, we'll subset the breed column and use the value_counts method | mostrará quantos de cada raça tem no dataframe
                                              unique_dogs['breed'].value_counts() 
                                              
 # We can also use the sort argument to get the breeds with the biggest counts on top
                                              unique_dogs['breed'].value_counts(sort = True)
                                              
 # normalize argument can be used to turn the counts into proportion of the total
                                              unique_dogs['breed'].valu_counts(normalize = True)
                                              
                                              #EXAMPLE COUNTING CATEGORICAL VARIABLES
                                              # Count the number of stores of each type
                                              Count the number of stores of each store type in store_types.
                                              Count the proportion of stores of each store type in store_types.
                                              Count the number of different departments in store_depts, sorting the counts in descending order.
                                              Count the proportion of different departments in store_depts, sorting the proportions in descending order.
                                              # ANSWER 
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize = True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort = True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort = True, normalize = True)
print(dept_props_sorted)
                                              
                                              #OUTPUT
A    11
B     1
Name: type, dtype: int64
A    0.917
B    0.083
Name: type, dtype: float64
41    12
30    12
23    12
24    12
25    12
      ..
37    10
48     8
50     6
39     4
43     2
Name: department, Length: 80, dtype: int64
41    0.013
30    0.013
23    0.013
24    0.013
25    0.013
      ...  
37    0.011
48    0.009
50    0.006
39    0.004
43    0.002
Name: department, Length: 80, dtype: float64
                                              
                                              # CHAPTER 02 - 2.2 GROUPED SUMMARY STATISTICS
# Summaries by group (mais dificil e pouco usado)
                                              dogs[dogs['color'] == 'Black']['weight_kg'].mean()
                                              dogs[dogs['color'] == 'Brown']['weight_kg'].mean()
                                              dogs[dogs['color'] == 'white']['weight_kg'].mean()
                                              dogs[dogs['color'] == 'Black']['weight_kg'].mean()
                                                
                                              
# Grouped summasumries 
                                              dogs.groupby('color')['weight_kg'].mean()
                                              #this will give us the mean weight for each dog color
# Multiple grouped summaries
                                              dogs.groupby('color')['weight_kg'].agg([min, max, sum])

                                              # we can use the agg method to get multiple statistics. This gives us the min, max and sum of different colored dogs weights
 #Grouping by multiple variables
                                              dogs.groupby(['color', 'breed'])['weight_kg'].mean()
                                              # we group by color and breed, select the weight and take the mean 
 # Many Groups, many summaries
                                              dogs.groupby(['color', 'breed'])[['weight_kg', 'height_cm']].mean()
                                              # group by multiple columns and aggregate bu multiple columns
                                              
                                              # EXAMPLE
# MODO MAIS DIFICIL E POUCO USADO
# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
                                              
                                              
                                              #EXAMPLE
                                              
# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)
                                     
                                              # EXAMPLE MULTIPLE GROUP SUMMARIES
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([min, max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg([min, max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)                                           

#OUTPUT
     unemployment                      fuel_price_usd_per_l                     
              min    max   mean median                  min    max   mean median
type                                                                            
A           3.879  8.992  7.973  8.067                0.664  1.107  0.745  0.735
B           7.170  9.765  9.279  9.199                0.760  1.108  0.806  0.803
                                              
                                              
                                              # CHAPTER 02 - 2.4 PIVOTING TABLES
                                              # they're another way of calculating grouped summary statistics 
 # Group by pivot table 
                                              dogs.groupby('color')['weight_kg'].mean() (isso foi visto já)
                                              # agora vem o pivot table 
                                              dogs.pivot_table(values = 'weight_kg', index = 'color')
                                              # os dois de cima terão o mesmo output , pq pivot_table já dar por defaut a mean statistic 
# Different Statistics 
                                              import numpy as np
                                              dogs.pivot_table(values = 'weight_kg', index = 'color', aggfunc = np.median) (exemplo agora foi np.median)
 # Multiple statistics
                                              dogs.pivot_table(values = 'weight_kg', index = 'color', aggfunc = [np.mean, np.median])
                                              
# Pivot on two variables 
                                              dogs.groupby(['color', 'breed'])['weight_kg'].mean()  (isso foi visto já)
                                              # agora vem o pivot table
                                              dogs.pivot_table(values = 'weight_kg', index = 'color', columns = 'breed')
                                              
# Filling missing values in pivot tables (pq eles colocam 'nan' quando n tem valor, ai é melhor colocar o argument fill_value = a alguma coisa, por exemplo = 0)
                                              dogs.pivot_table(values = 'weight_kg', index = 'color', columns = 'breed', fill_value = 0)
                                              # agora ao invez de ter nan terá 0 
                                              
# Summing with pivot tables
                                              dogs.pivot_table(values = 'weight_kg', index = 'color', coluns = 'breed', fill_value = 0, margins = True)
                                              # se eu colocar True, the last row and last column of the pivot table contain the mean of all the values in the column or row, not including the missing values that were filled in whit 0's
                                              # vai ter a média lá da linha color e média das colunas breed ( ou seja, de cada raça)
                                              

                                              # examples
                                              Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values ='weekly_sales', index = 'type')

# Print mean_sales_by_type
print(mean_sales_by_type)

                                              # output
         weekly_sales
type              
A        23674.667
B        25696.678
                                              # example
                                              Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.
# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values = 'weekly_sales', index = 'type', aggfunc = [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)
                                              # output
             mean       median
     weekly_sales weekly_sales
type                          
A       23674.667     11943.92
B       25696.678     13336.08

                                              # example
                                              Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values = 'weekly_sales', index = 'type', columns = 'is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
                                              #output
 is_holiday      False    True 
type                          
A           23768.584  590.045
B           25751.981  810.705
 
                                              #example
                                              Print the mean weekly_sales by department and type, filling in any missing values with 0.
                                              
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values = 'weekly_sales', index = 'department', columns = 'type', fill_value = 0))
                                              #output
type                 A           B
department                        
1            30961.725   44050.627
2            67600.159  112958.527
3            17160.003   30580.655
4            44285.399   51219.654
5            34821.011   63236.875
...                ...         ...
95          123933.787   77082.103
96           21367.043    9528.538
97           28471.267    5828.873
98           12875.423     217.428
99             379.124       0.000 (esse 0, era um nan que tinha antes)

[80 rows x 2 columns]
                                              
                                              # Example the margins = True
# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value = 0, margins = True))
 type                A           B        All
    department                                  
    1           30961.725   44050.627  32052.467
    2           67600.159  112958.527  71380.023
    3           17160.003   30580.655  18278.391
    4           44285.399   51219.654  44863.254
    5           34821.011   63236.875  37189.000
    ...               ...         ...        ...
    96          21367.043    9528.538  20337.608
    97          28471.267    5828.873  26584.401
    98          12875.423     217.428  11820.590
    99            379.124       0.000    379.124
    All         23674.667   25696.678  23843.950
    
    [81 rows x 3 columns]
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                     
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                        
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                       
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                         
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                          
--
                                              #CHAPTER 03 - SLICING AND INDEXING

dogs.columns -> dará o output de nome das colunas 
dogs.index -> dará output com que index começa start = 0, stop = 7, step = 1 ... por exemplo seria assim como  mostrei 

                                              # setting a columns as the index 
# you can move a column from the body of the DataFrame to the index -> então será no lugar da coluna que fica de 0 à 7, irá entrar outra coisa, por exemplo:
                                              dogs_ind = dogs.set_index('name')
                                              print(dogs_ind)
                                              
                                              # Dropping an index 
                                              dogs_ind.reset_index(drop = True)
                                              # isso quer dizer que tirarei a coluna name que foi colocada no lugar dos index logo acima, mas nÃo irá aparecer mais essa coluna name no dataframe
                                              
                                              # Indexes make subsetting simpler (aparecerá apenas o dataframe de bella e stella)
                                              dogs[dogs['name'].isin(['Bella', 'Stella'])]
                                             o equivalente com o de cima
                                             dogs_ind.loc[['Bella', 'Stella']] -> o .loc filter the index values, então vai tirar a coluna de index e colocar 
                                              
                                             # um pouco mais do .loc
                                              dogs_ind2 = dogs.set_index('breed')
                                              isso ai vai mostrar a coluna de index apenas com raças 
                                              para encontrar apenas uma raça e ver o dataframe dele, só usar o que tá embaixo:
                                              dogs_ind2.loc['Labrador']
                                              
                                              # Multi-level indexes hierarchical indexes
                                              técnicamente é escolher a ordem de cada coluna, e tirar tbm a coluna do index 
                                              dogs_ind3 = dogs.set_index(['breed', 'color'])
                                              
                                              #Subset the outer level with a list -> é meio que se tiver um desses que você escolher, eles vao ficar "colados", ver um exemplo depois bicho, que tu vai entender
                                              dogs_ind3_.loc[['labrador', 'Chiahuahua']] -> como labrador terá 2 cachorros, ai terá um subconjunto com os 2 nomes e 2 cores de cada um 
                                              
                                              # subset inner level  with a list of tuples , meio que especificar mesmo qual será dos cachorros
                                              dos_ind3.loc[[('labrador', 'brown'), ('chihuahua', 'tan')]]
                                              
                                              # Sorting by index values 
                                              dogs_ind3.sort_values()
                                              # by default, it sorts all index levels from outer to inner, in ascending order
                                              
                                              # Controlling sort_index
                                              dogs_ind3.sort_index(level = ['color', 'breed'], ascending = [True, False])
                                              
                                              # NOW YOU HAVE TWO PROBLEMS 
                                              -> Index values are just data (storing data in multiple forms makes it harder to think about)
                                              -> Indexes violate 'tidy data' principles (tidy data - where is stored in tabular form like a dataframe
                                              #in pandas the syntax for working with indexes is different from the syntax for working with columns
                                              -> you need to learn two syntaxes (by using two syntaxes, your code is more complicated, which can result in more bugs) 
                                                                                         
                                              # SETTINGS AND REMOVING INDEXES EXAMPLE
                                                                                         
# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index(drop = False))

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop = True))
                                             #OUTPUT
                                                                                         
            date     city        country  avg_temp_c
0     2000-01-01  Abidjan  Côte D'Ivoire      27.293
1     2000-02-01  Abidjan  Côte D'Ivoire      27.685
2     2000-03-01  Abidjan  Côte D'Ivoire      29.061
3     2000-04-01  Abidjan  Côte D'Ivoire      28.162
4     2000-05-01  Abidjan  Côte D'Ivoire      27.547
...          ...      ...            ...         ...
16495 2013-05-01     Xian          China      18.979
16496 2013-06-01     Xian          China      23.522
16497 2013-07-01     Xian          China      25.251
16498 2013-08-01     Xian          China      24.528
16499 2013-09-01     Xian          China         NaN

[16500 rows x 4 columns]
              date        country  avg_temp_c
city                                         
Abidjan 2000-01-01  Côte D'Ivoire      27.293
Abidjan 2000-02-01  Côte D'Ivoire      27.685
Abidjan 2000-03-01  Côte D'Ivoire      29.061
Abidjan 2000-04-01  Côte D'Ivoire      28.162
Abidjan 2000-05-01  Côte D'Ivoire      27.547
...            ...            ...         ...
Xian    2013-05-01          China      18.979
Xian    2013-06-01          China      23.522
Xian    2013-07-01          China      25.251
Xian    2013-08-01          China      24.528
Xian    2013-09-01          China         NaN

[16500 rows x 3 columns]
          city       date        country  avg_temp_c
0      Abidjan 2000-01-01  Côte D'Ivoire      27.293
1      Abidjan 2000-02-01  Côte D'Ivoire      27.685
2      Abidjan 2000-03-01  Côte D'Ivoire      29.061
3      Abidjan 2000-04-01  Côte D'Ivoire      28.162
4      Abidjan 2000-05-01  Côte D'Ivoire      27.547
...        ...        ...            ...         ...
16495     Xian 2013-05-01          China      18.979
16496     Xian 2013-06-01          China      23.522
16497     Xian 2013-07-01          China      25.251
16498     Xian 2013-08-01          China      24.528
16499     Xian 2013-09-01          China         NaN

[16500 rows x 4 columns]
            date        country  avg_temp_c
0     2000-01-01  Côte D'Ivoire      27.293
1     2000-02-01  Côte D'Ivoire      27.685
2     2000-03-01  Côte D'Ivoire      29.061
3     2000-04-01  Côte D'Ivoire      28.162
4     2000-05-01  Côte D'Ivoire      27.547
...          ...            ...         ...
16495 2013-05-01          China      18.979
16496 2013-06-01          China      23.522
16497 2013-07-01          China      25.251
16498 2013-08-01          China      24.528
16499 2013-09-01          China         NaN

[16500 rows x 3 columns]

                                                                                         
                                                               # SUBSETTING WITH .LOC[]
# Make a list of cities to subset on
cities = ["Moscow", "Saint Petersburg"]

# Subset temperatures using square brackets
print(temperatures[temperatures['city'].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities]) -> MESMA COISA DA DE CIMA, MAS MAIS 'SIMPLES'
                                                                #OUTPUT

<script.py> output:
                date    city country  avg_temp_c
    10725 2000-01-01  Moscow  Russia      -7.313
    10726 2000-02-01  Moscow  Russia      -3.551
    10727 2000-03-01  Moscow  Russia      -1.661
    10728 2000-04-01  Moscow  Russia      10.096
    10729 2000-05-01  Moscow  Russia      10.357
    ...          ...     ...     ...         ...
    10885 2013-05-01  Moscow  Russia      16.152
    10886 2013-06-01  Moscow  Russia      18.718
    10887 2013-07-01  Moscow  Russia      18.136
    10888 2013-08-01  Moscow  Russia      17.485
    10889 2013-09-01  Moscow  Russia         NaN
    
    [165 rows x 4 columns]
                          date country  avg_temp_c
    city                                          
    Moscow          2000-01-01  Russia      -7.313
    Moscow          2000-02-01  Russia      -3.551
    Moscow          2000-03-01  Russia      -1.661
    Moscow          2000-04-01  Russia      10.096
    Moscow          2000-05-01  Russia      10.357
    ...                    ...     ...         ...
    Moscow          2013-06-01  Russia      18.718
    Moscow          2013-07-01  Russia      18.136
    Moscow          2013-08-01  Russia      17.485
    Moscow          2013-09-01  Russia         NaN
    Saint Petesburg        NaT     NaN         NaN
    
    [166 rows x 3 columns]
                                                        # SETTING MULTI-LEVEL INDEXES 
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil','Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])
                                                                                         
                                                                                         
                                                      # SORTING BY INDEX VALUES
# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level = ['city']))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level = ['country', 'city'], ascending = [True, False]))                                                                                       
                                              
                                                    # OUTPUT
<script.py> output:
                             date  avg_temp_c
    country     city                         
    Afghanistan Kabul  2000-01-01       3.326
                Kabul  2000-02-01       3.454
                Kabul  2000-03-01       9.612
                Kabul  2000-04-01      17.925
                Kabul  2000-05-01      24.658
    ...                       ...         ...
    Zimbabwe    Harare 2013-05-01      18.298
                Harare 2013-06-01      17.020
                Harare 2013-07-01      16.299
                Harare 2013-08-01      19.232
                Harare 2013-09-01         NaN
    
    [16500 rows x 2 columns]
                                date  avg_temp_c
    country       city                          
    Côte D'Ivoire Abidjan 2000-01-01      27.293
                  Abidjan 2000-02-01      27.685
                  Abidjan 2000-03-01      29.061
                  Abidjan 2000-04-01      28.162
                  Abidjan 2000-05-01      27.547
    ...                          ...         ...
    China         Xian    2013-05-01      18.979
                  Xian    2013-06-01      23.522
                  Xian    2013-07-01      25.251
                  Xian    2013-08-01      24.528
                  Xian    2013-09-01         NaN
    
    [16500 rows x 2 columns]
                             date  avg_temp_c
    country     city                         
    Afghanistan Kabul  2000-01-01       3.326
                Kabul  2000-02-01       3.454
                Kabul  2000-03-01       9.612
                Kabul  2000-04-01      17.925
                Kabul  2000-05-01      24.658
    ...                       ...         ...
    Zimbabwe    Harare 2013-05-01      18.298
                Harare 2013-06-01      17.020
                Harare 2013-07-01      16.299
                Harare 2013-08-01      19.232
                Harare 2013-09-01         NaN
    
    [16500 rows x 2 columns]
                                                                                         
                                                                 # CHAPTER 3 - 3.2 SLICING AND SUBSETTING WITH .LOC AND .ILOC 
  # slicing is a technique for selecting consecutive elements from objects 
                                                                 
                                                                                         
                                                                 # Slicing lists
   breeds = ["Labrador", "Poodle", "Chow Chow", "Schnauzer", "Labrador", "Chihuahua", ...]] 
   breeds[2:5] -> isso é o slice
   #output -> ["Chow Chow", "Schnauzer", "Labrador"] 
   breeds[:3] -> pegará do inicio da lista até index 2 chow chow, pq não inclui o 3
   breeds[:] -> pegará toda a lista                                                                                      

                                                                # Sort the index before you slice
  you can slice DataFrames, but first, you need to sort the index. 
  here, the dogs dataset has been given a multi-level index of breed and color; then, the index is sorted with sort_index
   -> dogs_srt = dogs.set_index(["breed", "color"]).sort_index()
                                                               
                                                               # Slicing the outer index level -> ou seja, aquele que substituiu os números
   To slice rows at the outer level of an index, you call loc, passing the first and last values separated by a colon 
   dogs_srt.loc["Chow Chow" : "Poodle"] the final value "Poodle" is included (ou seja o valor final é incluido) 
                                                                                         
   the same technique does not work on inner index levels. 
                                                               # Slicing the inner index levels badly -> ou seja, os demais values
   nesse caso é diferente que o slicing the outer index 
   se eu quiser fazer -> dogs_srt.loc["Tan" : "Grey"] -> dará erro, pq em dataframe não funciona o slicing por dentro, apenas o outer index
   então:
  the correct approach to slicing index levels is to pass the first and last positions as tuples
  ->->-> o certo -> dogs_srt.loc[("Labrador", "Brown"]:("Schnauzer", "Grey")] -> first element here is a tuple of Labrador and brown, lembrar que o schnauzer está incluso
                                  
                                  
                                                                 # Slicing Columns
The simplest case involves subsetting columns but keeping all rows. 
dogs_srt.loc[:,"name":"height_cm"]     -> mantem toda a linha usando :, e seleciona as colunas que quer ver
                                  
                                                                # Slice Twice -> you can slice on rows and columns at the same time: simply pass the appropriate slice to each argument
dogs_srt.loc[("Labrador", "Brown"]:("Schnauzer", "Grey"), "name":"height_cm"]
              
                                  #An important use case of slicing is to subset DataFrames by range of dates
              dogs = dogs.set_index("date_of_birth").sort_index() -> nesse caso vai ficar as datas no lugar da coluna dos index numeros
                                  
                                  # Slicing by dates -> depois de subset dates in index 
              # get dogs with date_of_birth between 2014-08-25 and 2016-09-16
              dogs.loc["2014-08-25" : "2016-09-16"]
              
                                  # Slicing by partial dates
              # get dogs date_of_birth between 2014-01-01 and 2016-12-31 -> ou seja de 2014 até 2016
              dogs.loc["2014":"2016"]
              
                                  # Subsetting by row/columnn number
              print(dogs.iloc[2:5, 1:4] -> this uses a similar syntax to slicing lists, except that there are two arguments: one for rows and one for columns
                    lemnrar que o ultimo depois do : não conta 
                    
                    
                    
                    
                    
                                  # EXAMPLES - SLICING INDEX VALUES
                    
#Instructions -> You can only slice an index if the index is sorted (using .sort_index()).
# pandas is loaded as pd. temperatures_ind has country and city in the index, and is available.
    Sort the index of temperatures_ind.
    Use slicing with .loc[] to get these subsets:
    from Pakistan to Russia.
    from Lahore to Moscow. (This will return nonsense.)
    from Pakistan, Lahore to Russia, Moscow.
    
# Resoluçao                    
# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc["Pakistan" : "Russia"])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc["Lahore":"Moscow"])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[("Pakistan, Lahore") : ("Russia", "Moscow")])  
                     
                                      # EXAMPLES - Slicing in both directions
                    
# Instructions -
# pandas is loaded as pd. temperatures_srt is indexed by country and city, has a sorted index, and is available.
 
    Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
    Use .loc[] slicing to subset columns from date to avg_temp_c.
    Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.
                    
# Resolução
                    
# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[("India", "Hyderabad") : ("Iraq", "Baghdad")])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:, "date" : "avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[("India", "Hyderabad") : ("Iraq", "Baghdad"), "date" : "avg_temp_c"])
                    
                    
                                    # EXAMPLE - SLICING TIME SERIES
Slicing is particularly useful for time series since it's a common thing to want to filter for data within a date range. Add the date column to the index, then use .loc[] to perform the subsetting. The important thing to remember is to keep your dates in ISO 8601 format, that is, yyyy-mm-dd.

Recall from Chapter 1 that you can combine multiple Boolean conditions using logical operators (such as &). To do so in one line of code, you'll need to add parentheses () around each condition.
#pandas is loaded as pd and temperatures, with no index, is available.

# Instructions -

    Use Boolean conditions (not .isin() or .loc[]) to subset for rows in 2010 and 2011, and print the results.
    Note that because the date isn't set as an index, a condition that contains only a year, such as df["date"] == "2009", will check if the date is equal to the first day of the first month of the year (e.g. 2009-01-01), rather than checking whether the date occurs within the given year. We recommend writing out the full date when using Boolean conditions (e.g., 2009-12-31).
    Set the index to the date column.
    Use .loc[] to subset for rows in 2010 and 2011.
    Use .loc[] to subset for rows from Aug 2010 to Feb 2011.
                    
# Resolução
                    
# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
temperatures_bool = temperatures[(temperatures["date"] >= "2010-01-01") & (temperatures["date"] <= "2011-12-31")]

print(temperatures_bool)

# Set date as an index and sort the index
temperatures_ind = temperatures.set_index("date").sort_index()

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc["2010":"2011"])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc["2010-08-01":"2011-02-01"])    
                    
                                                    # CHAPTER 03 - 2.3 WORKING WITH PIVOT TABLE
  # pIVOTING THE DOG PACK
                    dogs_height_by_breed_vs_color = dog_pack_pivot_table("height_cm", index = "breed", columns = "color")
                    print(dogs_height_by_breed_vs_color)
  # the first argument is the column name containing values to aggregate
  # the index argument lists the columns to group by and display in rows
  # and the columns argument list the columns to group by and display in columns
                    #default function it's mean
 -> dará um dataframe que as linhas são as raças  e as colunas são as cores, e os valores dessas colunas terá as alturas
                    tipo:
                    color       black         brown       gray        tan          white
                    breed       
                    beagle      34.500        36.500      36.311      35.700        38.891
                    boxer       57.345        63.500      58.900      62.3200       56.400
                    st. bernard  ....          .....         ...     ....          .....           
                    chihuahua     ....          .....         ...    ....          .....         
                    chow chow     ....          .....         ...
                    labrador      ....          .....         ...     ....          .....         
                    .
                    .
                    .
                    
                    
# pivot tables are just DataFrame with sorted indexes -> that means that all the fun stuff you've learned so far this chapter can be used on them.            
                                                # .loc[] + slicing is a power combo
                    
                    
                    # in particular, the loc[] and slicing combination is ideal for subseting pivot tables, like so.
                    dogs_heigh_by_breed_vs_color_.loc["chow chow" : "poodle"] -> slicing the dataframe acima que usamos o pivot table
                    
                                                # the axis argument
                    dogs_heigh_by_breed_vs_color_.mean(axis = "index")
                    # the methods for calculating summary statistics on a dataframe, such as mean, have an axis argument
                    # the default valus is "index" which means "calculate the statistic across rows" -> then here, the mean is calculate for each color, that is across the breeds
                    
                    #to calculate the summary statistic for each row, that is, "across the columns", you set the axis to columns
                      dogs_heigh_by_breed_vs_color_.mean(axis = "columns") -> here the mean heigh calculated for each breed, that means across the colors
                    
                                                                        
                    
                                                                # EXAMPLE - PIVOTING TEMPERATURE  BY CITY  AND YEAR
    

It's interesting to see how temperatures for each city change over time—looking at every month results in a big table, which can be tricky to reason about. Instead, let's look at how temperatures change by year.

You can access the components of a date (year, month and day) using code of the form dataframe["column"].dt.component. For example, the month component is dataframe["column"].dt.month, and the year component is dataframe["column"].dt.year.

Once you have the year column, you can create a pivot table with the data aggregated by city and year, which you'll explore in the coming exercises.

pandas is loaded as pd. temperatures is available.
                    
                    
# INSTRUCTIONS
                    
    Add a year column to temperatures, from the year component of the date column.
    Make a pivot table of the avg_temp_c column, with country and city as rows, and year as columns. Assign to temp_by_country_city_vs_year, and look at the result.
                    
                    
# RESOLUÇÃO
# Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)
                    
                    #OUTPUT
                    # Add a year column to temperatures
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)
                    
#OUTPUT
year                              2000    2001    2002    2003    2004  ...    2009    2010    2011    2012    2013
country       city                                                      ...                                        
Afghanistan   Kabul             15.823  15.848  15.715  15.133  16.128  ...  15.093  15.676  15.812  14.510  16.206
Angola        Luanda            24.410  24.427  24.791  24.867  24.216  ...  24.325  24.440  24.151  24.240  24.554
Australia     Melbourne         14.320  14.180  14.076  13.986  13.742  ...  14.647  14.232  14.191  14.269  14.742
              Sydney            17.567  17.855  17.734  17.592  17.870  ...  18.176  17.999  17.713  17.474  18.090
Bangladesh    Dhaka             25.905  25.931  26.095  25.927  26.136  ...  26.536  26.648  25.803  26.284  26.587
...                                ...     ...     ...     ...     ...  ...     ...     ...     ...     ...     ...
United States Chicago           11.090  11.703  11.532  10.482  10.943  ...  10.298  11.816  11.214  12.821  11.587
              Los Angeles       16.643  16.466  16.430  16.945  16.553  ...  16.677  15.887  15.875  17.090  18.121
              New York           9.969  10.931  11.252   9.836  10.389  ...  10.142  11.358  11.272  11.972  12.164
Vietnam       Ho Chi Minh City  27.589  27.832  28.065  27.828  27.687  ...  27.853  28.282  27.675  28.249  28.455
Zimbabwe      Harare            20.284  20.861  21.079  20.889  20.308  ...  20.524  21.166  20.782  20.523  19.756    
                    
                    
                    
                    
                                                                # EXAMPLE - SUBSETTING PIVOT TABLES
# INSTRUCTIONS
Use .loc[] on temp_by_country_city_vs_year to take subsets.

    From Egypt to India.
    From Egypt, Cairo to India, Delhi.
    From Egypt, Cairo to India, Delhi, and 2005 to 2010.
                    
                    
# RESOLUÇÃO
# Subset for Egypt to India
temp_by_country_city_vs_year.loc["Egypt" : "India"]

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[("Egypt", "Cairo") : ("India", "Delhi")]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[("Egypt", "Cairo") : ("India", "Delhi"), "2005":"2010"]
                    
                    
 # OUTPUT
 year                    2005    2006    2007    2008    2009    2010
country  city                                                       
Egypt    Cairo        22.006  22.050  22.361  22.644  22.625  23.718
         Gizeh        22.006  22.050  22.361  22.644  22.625  23.718
Ethiopia Addis Abeba  18.313  18.427  18.143  18.165  18.765  18.298
France   Paris        11.553  11.788  11.751  11.278  11.464  10.410
Germany  Berlin        9.919  10.545  10.883  10.658  10.062   8.607
India    Ahmadabad    26.828  27.283  27.511  27.049  28.096  28.018
         Bangalore    25.476  25.418  25.464  25.353  25.726  25.705
         Bombay       27.036  27.381  27.635  27.178  27.845  27.765
         Calcutta     26.729  26.986  26.585  26.522  27.153  27.289
         Delhi        25.716  26.366  26.146  25.675  26.554  26.520                   
                                                                                # EXAMPLE - CALCULATING ON A PIVOT TABLE
Pivot tables are filled with summary statistics, but they are only a first step to finding something insightful. Often you'll need to perform further calculations on them. A common thing to do is to find the rows or columns where the highest or lowest value occurs.

Recall from Chapter 1 that you can easily subset a Series or DataFrame to find rows of interest using a logical condition inside of square brackets. For example: series[series > value].

pandas is loaded as pd and the DataFrame temp_by_country_city_vs_year is available
                    
 # INSTRUCTION
                    
    Calculate the mean temperature for each year, assigning to mean_temp_by_year.
    Filter mean_temp_by_year for the year that had the highest mean temperature.
    Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
    Filter mean_temp_by_city for the city that had the lowest mean temperature.
# RESOLUÇÃO
# Get the worldwide mean temp by year
mean_temp_by_year = temp_by_country_city_vs_year.mean()

# Filter for the year that had the highest mean temp
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])

# Get the mean temp by city
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis = "columns")

# Filter for the city that had the lowest mean temp
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])
                    
                    # OUTPUT
    <script.py> output:
    year
    2013    20.312
    dtype: float64
    country  city  
    China    Harbin    4.877
    dtype: float64
                    
