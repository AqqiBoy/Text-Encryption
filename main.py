# Creating Base64 Ascii Table
b64_ascii_table = []
for i in range(65, 91):
    b64_ascii_table.append(chr(i))
for i in range(97, 123):
    b64_ascii_table.append(chr(i))
for i in range(48, 58):
    b64_ascii_table.append(chr(i))
b64_ascii_table.append(chr(43))
b64_ascii_table.append(chr(47))

# Starting Decoding

# Saving String Characters In Array
string = 'aGk='
string_arr = []
for i in string:
    string_arr.append(i)

# Counting '='
equal_count = 0
while string_arr[-1] == '=':
    string_arr.pop()
    equal_count += 1

# Finding Indexes Of String Characters
char_indexes = []
for i in range(len(string_arr)):
    for j in range(len(b64_ascii_table)):
        if string_arr[i] == b64_ascii_table[j]:
            char_indexes.append(b64_ascii_table.index(b64_ascii_table[j]))

# Binary Conversion Of Indexes
all_numbers_binary_array = []
message = ''
for i in char_indexes:
    binary_counter = 0
    int_num = int(i)
    array_binary_pattern = list()
    while int_num != 0:
        remainder = int_num % 2
        array_binary_pattern.append(remainder)
        int_num = int_num // 2
    array_binary_pattern.reverse()
    for j in range(len(array_binary_pattern)):
        binary_counter += 1
    binary_counter = 6 - binary_counter
    for k in range(binary_counter):
        all_numbers_binary_array.append(0)
    for l in array_binary_pattern:
        all_numbers_binary_array.append(l)
for i in range(equal_count * 2):
    all_numbers_binary_array.pop()
counter = int(len(all_numbers_binary_array) / 8)
for i in range(counter):
    char_array = []
    for j in range(8):
        char_array.append(all_numbers_binary_array[0])
        all_numbers_binary_array.pop(0)
    char_array.reverse()
    sum = 0
    for k in range(len(char_array)):
        sum = sum + int(char_array[k]) * 2 ** k
    message += chr(sum)

print(message)