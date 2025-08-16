def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
    return True


solution =is_prime(int(input("enter the number\n")))
print(solution)