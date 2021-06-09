first_name = 'Stephan'
last_name = 'Salvatore'
print(first_name + last_name)

print(first_name * 4)
print(len(first_name))
print('St' in first_name)
print('St' in last_name)

print(ord('a'))     # Prints ASCII value
print(chr(97))      # Reverse of ord()- Returns character of ASCII code
test_num = 3987
print(str(test_num))

# String Indexing
print(last_name[0])
print(last_name[-1])

# String slicing
print(last_name[2:5])
print(last_name[:7])
print(last_name[3:])
print(last_name[::2])   # Stride in the string

# String does not support assignment operator
# last_name[2] = 'z' -> This is not allowed
# We can use .replace method to do so
print(last_name)
temp_text = last_name.replace('S', 'z')
print(temp_text)

# Some built-in methods
print(temp_text.capitalize())   # Capitalize first character
print(last_name.lower())    # Lowers the string chars
print(last_name.upper())
print(last_name.swapcase())     # swaps chars
print('This is london'.title())

movie_name = 'The Perks of Being a Wallflower'
# Count of a string
print(movie_name.count('e'))
print(movie_name.count('e', 0, 15))

# Find the position of a string
print(movie_name.find('Perks'))
print(movie_name.find('Wolf'))      # Return -1 if string not found
temp = 'foo bar foo baz foo qux'
print(temp.rfind('foo', 0, 14))
print(temp.rfind('Perks', 0, 10))

# Starts with and ends with
print(movie_name.startswith('The'))
print(movie_name.startswith('Hello'))
print(movie_name.endswith('Wallflower'))

# Character classification
print('abc123'.isalnum())   # Checks whether all chars are alphanumeric
print('abcd12@#3'.isalnum())
print('acddd'.isalpha())
print('abcde123'.isalpha())
print('123'.isdigit())
print('abcde123'.isdigit())
