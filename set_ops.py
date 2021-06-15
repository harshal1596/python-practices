test_set = {'Python', 'Java', 'PHP'}
print(len(test_set))

for i in test_set:
    print(i)
test_set.add('Ruby')

# Add sets
# Remove an item
test_set.remove("PHP")
test_set.discard("C")
# test_set.clear()    # Clears a set
print(test_set)

# Join sets
second_set = {'Python', 'CPP'}
test_set.update(second_set)
third_set = {'MySQL', 'MongoDB', 'Python'}
# test_set.union(third_set)   # union() and update() are same

abc = third_set.intersection(test_set)     # This stores only common element to the set
print(abc)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# Keep all but not the duplicates
# x.symmetric_difference_update(y)
# print(x)

z = x.symmetric_difference(y)
print(z)

