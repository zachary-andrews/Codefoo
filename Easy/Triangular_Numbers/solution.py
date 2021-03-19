import math

def get_divisors(number):
    divisors = [1]
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            divisors.extend([i,number/i])
            divisors.extend([number])
    return list(set(divisors))

def get_triangles(number):
    triangle = 0
    for i in range(number+1):
        triangle += i 
    return triangle

if __name__ == "__main__":
    count = 0 
    while len(get_divisors(get_triangles(count))) <= 500:
        count += 1
    print(get_triangles(count))
