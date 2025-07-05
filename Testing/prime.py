import math

def is_prime(n:int) -> bool:
    if n < 2:
        return False
    
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

# assert is_prime(4) == True
# print(is_prime(9))