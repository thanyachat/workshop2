# EX 1
thislist = {"apple", "banana", "cherry"}
thislist.remove("banana")
print(thislist)  # Output: {'apple', 'cherry'}

# EX 2
thislist = {"apple", "banana", "cherry"}
thislist.discard("banana")
print(thislist)  # Output: {'cherry', 'apple'}

# EX 3
thislist = {"apple", "banana", "cherry"}
x = thislist.pop()
print(thislist)  # Output: {'cherry','banana'}

# EX 4
thislist = {"apple", "banana", "cherry"}
thislist.clear()
print(thislist)  # Output: set()
