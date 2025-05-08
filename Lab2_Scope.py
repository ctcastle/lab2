# ENSF 692 Spring 2025
# May 8 Lab 2
# Exercise 2
# Conner Castle

# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

# POINT 1
point_no = 1
print(f'Print statements from Point {point_no}: ')
print(f'Point {point_no}: foo = {foo}')
print(f'Point {point_no}: foo type = {type(foo)}')
print(f'Point {point_no}: bar = {bar}')
print(f'Point {point_no}: bar type = {type(bar)}')
print('--------------------------------------------')
# What is the value of foo at this point? - foo = 100 
# What is the type of foo at this point? - foo is an int 
# What is the value of bar at this point? - bar = 100 
# What is the type of bar at this point? - bar is an int 

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
point_no = 2
print(f'Print statements from Point {point_no}: ')
print(f'Point {point_no}: foo = {foo}')
print(f'Point {point_no}: bar = {bar}')
print(f'Point {point_no}: spam = {spam}')
print(f'Point {point_no}: eggs = {eggs}')
print(f'Point {point_no}: ham = {ham}')
print(f'Point {point_no}: baz = {baz}')
print('--------------------------------------------')
# What is the value of foo at this point? - foo = 150 
# What is the value of bar at this point? - bar = 100 
# What is the value of spam at this point? - spam = 200 
# What is the value of eggs at this point? - eggs = 250 
# What is the value of ham at this point? - ham = [1,2,3,100]
# What is the value of baz at this point? - baz = [1,2,3,100]

eggs = "Python is very flexible!"
spam = ham
ham = bar
bar += bar
foo = eggs
eggs = bar + ham
baz.append(bar)

# POINT 3
point_no = 3 
print(f'Print statements from Point {point_no}: ')
print(f'Point {point_no}: foo = {foo}')
print(f'Point {point_no}: bar = {bar}')
print(f'Point {point_no}: spam = {spam}')
print(f'Point {point_no}: eggs = {eggs}')
print(f'Point {point_no}: ham = {ham}')
print(f'Point {point_no}: baz = {baz}')
print('--------------------------------------------')
# What is the value of foo at this point? - foo = "Python is very flexible"
# What is the value of bar at this point? - bar = 200 
# What is the value of spam at this point? - spam = [1,2,3,100,200] -> because this points to the same address as baz it gets updated again on line 53 
# What is the value of eggs at this point? - eggs = 300 -> because bar is 200 and ham is 100 
# What is the value of ham at this point? - ham = 100 
# What is the value of baz at this point? - baz = [1,2,3,100,200]

# Print out the types and final values of each variable.
point_no = 'FINAL' 
print(f'Print statements from Point {point_no}: ')
print(f'Point {point_no}: foo_type: {type(foo)}   foo = {foo}')
print(f'Point {point_no}: bar_type: {type(bar)}   bar = {bar}')
print(f'Point {point_no}: spam_type: {type(spam)} spam = {spam}')
print(f'Point {point_no}: eggs_type: {type(eggs)}  eggs = {eggs}')
print(f'Point {point_no}: ham_type: {type(ham)}   ham = {ham}')
print(f'Point {point_no}: baz_type: {type(baz)}  baz = {baz}')
print('--------------------------------------------')
