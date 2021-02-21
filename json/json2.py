import json

# a Pytgon object (dict):
python_dict = {
    "name": "jim & Por",
     "age":26,
      "city": "Bnagkok"
}

# convert into JSON:
json_string = json.dumps(python_dict)

# the result is a JSON string:
print(json_string)