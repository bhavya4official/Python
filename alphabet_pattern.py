pattern = [5, 2, 5, 2, 2]  # F
for item in pattern:
    print('X' * item)

print('\n');

pattern = [5, 2, 2, 2, 5]  # C
for item in pattern:
    output = ''
    for count in range(item):
        output += 'X'
    print(output)
