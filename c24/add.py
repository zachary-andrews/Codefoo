def number_add(number,counter):
    if len(str(sum_digits(number))) == 1:
        return counter
    return number_add(sum_digits(number),counter+1)
    
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

if __name__ == "__main__":
    number = 199
    print number_add(number,1)