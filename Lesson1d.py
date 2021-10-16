
# Lists , tuples , dictionaries
# they are more similar to arrays
# We use arrays when we habev many values to be stored in one varaible

# a tuple
fruits = ('Apple','Mango','Passion','Melons')
marks = (90,45,45,77,66,55,77,88,77,66,77,33,22.6)
print(fruits)
print(marks)
print(fruits[2])
print('The child got ', marks[2], 'Was awarded an ',fruits[0])

# a tuple is immutrable/ can't be updated
# fruits.append('Orange')  # pushes the end
#fruits.insert(0, 'Blackberries')
#fruits.remove('Mango')
#print(fruits)
# A list flexible and uses the square []
import  statistics
print('Mean ', statistics.mean(marks))
print('Median', statistics.median(marks))
print('SDEv', statistics.stdev(marks))









