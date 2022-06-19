# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked) # from file deshaun, take the column day_of_week 

# Display Deshaun's plot
plt.show()

# SHOW LEGENDS

# Officer Deshaun
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')

# Add a label to Aditya's plot
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')

# Add a label to Mengfei's plot
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a command to make the legend display
plt.legend()

# Display plot
plt.show()


# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title('Officers')

# Add y-axis label
plt.ylabel('Cases Solved')

# Legend
plt.legend()
# Display plot
plt.show()


# Officer Deshaun is examining the number of hours that he worked over the past six months. 
# The number for June is low because he only had data for the first week. Help Deshaun add an annotation to the graph to explain this.

# Arbitrary text
plt.plot(six_months.month, six_months.hours_worked)
plt.text(2.5, 80, 'Missing June Data') # plt.text(xcoord, ycoord, 'Text message') # na coordenada x = 2.5 e y = 80 vai ter uma mensagem dizendo 'Missing June data'
# Display graph
plt.show()

# change font size
plt.title('Plot title', fontsize = 20)
# Change  font color 
plt.legend(color = 'green')

# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color = 'DarkCyan')

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle = ':')

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker = 's')

# Add a legend
plt.legend()

# Display the plot
plt.show()


# Changing line color
plt.plot(x, y, color = 'tomato')
# Changing line width
plt.plot(x, y, linewidth = 1) # vai até 7

# changing line style -> You can change linestyle to dotted (':'), dashed('--'), or no line ('').
plt.plot(x, y, linestyle = ':') # pode ser tbm '-', '--', '-.' ou ':' 

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.plot(suspect2.letter, suspect2.frequency, label='Gertrude Cox')

# Add x- and y-labels
plt.xlabel("Letter")
plt.ylabel("Frequency")

# Add a legend
plt.legend()

# Display plot
plt.show()
# adding markers -> You can change the marker to circle ('o'), diamond('d'), or square ('s').
plt.plot(x, y, marker = 'x') # pode ser, x, s, d, *, o, h)

# changing the graphe style
plt.style.use('fivethirtyeight') # you can use also 'seaborn', 'ggplot', 'default'

# Change the style to fivethirtyeight
plt.style.use('fivethirtyeight')

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

# View all styles by typing print(plt.style.available) in the console.
print(plt.style.available)

# PLOT SCATTER - ALPHA IS THE TRANSPARENCY
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha = 0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

