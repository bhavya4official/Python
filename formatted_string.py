# formatted string
first = 'Bhavya'
last = 'Singh'

# string concatenation is complex
message = first + ' [' + last + '] is a coder.'
print(message)

msg = f"{first} [{last}] is a coder."
""" Prefix sting with f and use {place holders} to dynamically insert value into string
 formatted string is simple to read"""
print(msg)
