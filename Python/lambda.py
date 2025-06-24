people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
]

# def f(person):
#     return person["name"]


# people.sort(key=f)
# Alternatively, you can use a lambda function directly in the sort method
# syntax = lambda arguments: expression
people.sort(key=lambda person: person["name"])
print(people)