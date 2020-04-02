# 1. write a divide_by function that divides 50 by number passed to iter
# 2. add try and except statement
# 3. add another example where user can potentially enter invalid entry
# 4. now wrap this new code in try-except

def divide_by(number):
  try:
    return 50/number
  except ZeroDivisionError:
    print ('Error: you can\'t divide by zero')

print(divide_by(2))
print(divide_by(10))
print(divide_by(5.5))

print(divide_by(0))
print(divide_by(20))
print('=========********=========')

#===============================
# 3. add another example where user can potentially enter invalid entry
dogs_num = input('How many dogs you have?') 
try:
  if int(dogs_num) >= 5:
    print('That\'s lot of dogs!')
  else:
    print('That\'s not that many dogs!')

except ValueError:
  print("You didn't enter a number!")
