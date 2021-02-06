thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX 1
for key in thisdict:
    print(key)

# Output:
# brand
# model
# year

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX 2
for key in thisdict:
    print(thisdict[key])

# Output:
# Ford
# Mustang
# 1964

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX 3
for key in thisdict.keys():
    print(key)

# Output:
# brand
# model
# year

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX 4
for value in thisdict.values():
    print(value)

# Output:
# Ford
# Mustang
# 1964

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

# EX 5
for key, value in thisdict.items():
    print(key, value)

# Output:
# brand Ford
# model Mustang
# yaar 1964