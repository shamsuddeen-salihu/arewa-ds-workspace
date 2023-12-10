import sys
print("Python version:",sys.version)

#operations
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

#strings
print('Shamsuddeen')
print('Salihu')
print('Nigeria')
print('I am enjoying 30 days of python')

#check types
type(10)
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Shamsuddeen'))
print(type('Salihu'))
print(type('Migeria'))

#data types example
integer_num = 5
float_num = 3.14
complex_num = 2 + 3j
string_var = "Hello, world!"
bool_var = True
list_var = [1, 2, 3, 4, 5]
tuple_var = (10, 20, 30)
set_var = {1, 2, 3, 4, 5}
dict_var = {'name': 'Shamsuddeen', 'age': 25, 'city': 'Kano'}

#euclidean distance
import math
point1 = (2, 3)
point2 = (10, 8)

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print("Euclidean distance:",distance)