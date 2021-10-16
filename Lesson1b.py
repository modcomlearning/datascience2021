# Given PRT/100 find simple interest
p = 50000
r = 14.5
t = 3
employee_name = "Joseph Johnson"
initials = 'Mr'
mesaage =  '''Multiline message goes here  '''

print("Your principle amount was ", p, 'KES')
print('Your rate was at', r, "%")
print('Time was', t, 'Months')
print('Your name is ', initials,  employee_name)

# do some maths
interest  = (p * r* t)/100
print('Your simple interest is ', interest, 'KES')
print(mesaage[0:10])
words = mesaage.split()
print(words)

