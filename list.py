# here we will learn about the list 
courses=['History','Math','Science','Social Studies']
print(courses)

# to use slicing
print(courses[0:2])
print(courses[3:])
print(courses[2]) # for single access of the file.
print(courses[2:4])
print(courses[-2:])

# to append something on the the list of courses
courses.append('Art')
print(courses)
# to insert these two Opt Math to the first index then 
courses.insert(0, 'Opt Math')
print(courses)

courses_2=['Nepali','Vocation Studies']
print(courses_2[0])
print(courses_2)
# now we are going directly insert this courses_2 list on the list of courses 
 
# will directly insert all the values to the courses list. like this ['Opt Math', 'History', ['Nepali', 
# 'Vocation Studies'], 'Math', 'Science', 'Social Studies', 'Art']
courses.insert(2, courses_2)
print(courses) 

# so to get rid of this ['Opt Math', 'History', ['Nepali', 'Vocation Studies'], 'Math', 'Science', 'Social Studies', 'Art'] output then we have to use extend method 
courses_3=['Chinese','Japanese']
courses.extend(courses_3) # takes only one arguement
print(courses)

# to remove the value from a list called Nepali subject. 
courses_2.remove('Nepali')
print(courses)

# will remove the very last value of the list courses. This is useful for making our list like a stack or queue
courses.pop()
print(courses)

# to get a return value about which got popped or removed out of the list of courses
popped=courses.pop() 
print('This the chinese one will get popped out of the list:- ' + popped)
print(courses)

# sorting the list in the couple of ways we can expect
courses.reverse() # reverse order sorting
print(courses)

# sorting in alphabetical order of the languages
courses_4=['Chinese','Nepali','English','Japanese','korean','Indian']
print(courses_4)
courses_4.sort()
print(courses_4)

# sorting the list of numbers acending order 
nums=[1,158,19,0,454,56,9,41,15,3,4,98,24,6,7,8,2,11,66,44,9,97]
nums.sort()
print(nums)

# sorting of list of numbers in decending order and more easier method
nums.sort(reverse=True)
print(nums)

# sorting of the list without altering the original list using diff methods using sorted function
# we need make a new variable and set it to return the value of the sorted function
# sorted() -----> this function doesn't do vedvaav with int and strings.
sorted_nums=sorted(nums)
print(sorted_nums)

# for string one
sorted_courses_4=sorted(courses_4)
print(sorted_courses_4)

# for printing the max amd min value of the given list 
print(min(nums))
print(max(nums))
