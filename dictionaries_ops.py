thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Get values in the dict
print(len(thisdict))
print(thisdict.get('model'))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# Insert item in the dict
thisdict["colour"] = 'Red'
print(thisdict)

# Update an item
thisdict["colour"] = 'Blue with White strips'
thisdict.update({'year': 1967})
print(thisdict)


if "model" in thisdict:
    print('Key is present')

# Pop an item
thisdict.pop('year')
print(thisdict)
# thisdict.popitem()      # Removes last item from the dict

# thisdict.clear()    # Clears the dictionary
# del thisdict    # Deletes an entire dictionary
# print(thisdict)

# Loop to a dictionary
for i, j in thisdict.items():
    print(i, j)
# Similarly we can print thisdict.keys() and thisdict.values()

# Copy the dictionary
test_dict = thisdict.copy()
print(test_dict)

# Nested dictionaries
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

parents = {"child1": child1, "child2": child2, "child3": child3}
print(len(parents))
