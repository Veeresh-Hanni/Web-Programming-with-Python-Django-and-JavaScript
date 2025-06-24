from functions import squares,square, cube


def loop():
    for i in range(1, 11):
        yield i


sq_list = [squares(i) for i in loop()]
print()
print("Looping through numbers 1 to 10:\n")
print(f"Squares: {[f'Square of {i}: {sq_list[i]}' for i in range(len(sq_list))]}\n")
print(f"Cubes: {[f'Cube of {i}: {cube(i)}' for i in loop()]}\n")

for num,sq,cub in zip(loop(),[square(i) for i in loop()],[cube(i) for i in loop()]):
    print(f"Number: {num}, Square: {sq}, Cube: {cub}")