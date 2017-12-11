from die import Die
import pygal

# Create a D6
die = Die()

# Make some rolls and store in list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# analyze resu;ts
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one d6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die.visual.svg')

