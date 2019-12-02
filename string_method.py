# Count the length of string for validation
course = 'Python course'
print(len(course))  # len is general purpose function (not restricted to string only)
print(course.upper())  # upper method is a (function specific to string )
print(course.lower())
print(course.title())  # First letter of each word become capital
print(course.find('P'))  # Case sensitive method to find first occurance of a char/string
print(course.find('course'))  # if not present it returns -1
print(course.replace('P', 'H'))
print(course.replace('course', 'language'))
print('Print' in course)  # in operator return boolean value (True/False) for existence of a char/string

# print is a general purpose function (it does not belong to specific object)
# In OOPs, function that belong/specific to some kind of object = metho
