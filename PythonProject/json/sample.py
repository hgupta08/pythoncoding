import json
food_ratings = {"organic dog food": 2, "human food": 10}

with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    json.dump(food_ratings, write_file)

# After importing the json module, you can use .dumps() to convert a
# Python dictionary to a JSON-formatted string, which represents a JSON object.

#writing to file using json dump(file,target) as the argument
print(json.dumps(food_ratings,sort_keys=True))

# By using json.loads(), you can convert JSON data back into Python objects.

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
}
dog_data_json = json.dumps(dog_data)

print(type(dog_data_json["address"]["home"]))

dog_data_json = json.loads(dog_data_json)

print(type(dog_data_json["address"]["home"]))

#
# type(new_dog_data["address"]["home"])
#
#
# new_dog_data = json.loads(dog_data_json)
# new_dog_data