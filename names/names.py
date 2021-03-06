import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

#sorting a list into a binary tree and traverse it with th e second
binarysearch = BinarySearchTree('duplicate_names')

# Replace the nested for loops below with your improvements
#here we are adding the names from name_1 to the tree
for name in names_1:
    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)
    binarysearch.insert(name)

#then we're checking the names in names_2 and see if it's already there, if it finds it, it's added to the duplicates array
for name in names_2:
    if binarysearch.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
