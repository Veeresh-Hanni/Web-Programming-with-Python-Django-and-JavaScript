for i in range(1, 11, 2):
    print(i)


# Using a while loop
i = 1
while i < 11:
    print(i)
    i += 2


# Using a for loop with a list
numbers = [1, 3, 5, 7, 9]
for i in numbers:
    print(i)    

# Using a for loop with a string
for char in "Hello":
    print(char)

# Using a for loop with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")    

# Using a for loop with a set
my_set = {1, 2, 3, 4, 5,2}
for item in my_set:
    print(item)


# Using a for loop with enumerate
my_list = ["apple", "banana", "cherry"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

