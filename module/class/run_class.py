# module/class/run_class.py

import classPerson

name = "thanyachat permpool"
age = 20
address = "Thailand"

person = classPerson.Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info())