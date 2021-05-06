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
dtypes: float64(2), int64(1), object(2)
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
          
          

          
                    
           
           
            
