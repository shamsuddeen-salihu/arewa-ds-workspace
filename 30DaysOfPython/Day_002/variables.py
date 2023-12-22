# Exercises: Level 1
# Day 2: 30 Days of python programming
first_name="Shamsuddeen"
last_name="Salihu"
full_name="Shamsuddeen Salihu"
country="Nigeria"
age=25
year=1998
is_married=True
is_true= True
is_light_on=False
first_name, last_name, country, age, is_married = 'Shamsuddeen', 'Salihu', 'Nigeria', 25, True

# Exercises: Level 2
# checking the data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#finding the length of first name
print(len(first_name))
#comparing the length of firsname and lastname
print(len(first_name)==len(last_name))

#arithmetic
num_one, num_two= 5, 4
total= num_one + num_two,
diff=num_one - num_two,
product= num_one * num_two,
division= num_one/num_two,
remainder = num_two%num_one,
exp =num_one**num_two,
floor_division= num_one//num_two

# area of a circle
radius=30
pi=3.142
area_of_circle=pi*radius**2
circum_of_circle=2*pi*radius
print(area_of_circle)
print(circum_of_circle)

#input from user
user_radius=float(input("Enter radius:")) 
area_of_circle2=pi*user_radius**2
print(area_of_circle2)
