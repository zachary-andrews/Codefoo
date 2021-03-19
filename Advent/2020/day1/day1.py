def partone() -> int:
    with open("numbies.txt", "r") as f:
        data = f.read()

    numbers = [int(i) for i in data.split()]

    for number in numbers:
        compliment = 2020-number
        if compliment in numbers:
            return(compliment * number)

def parttwo():
    with open("numbies.txt", "r") as f:
        data = f.read()

    numbers = [int(i) for i in data.split()]

    for i in range( 0, len(numbers)-2):

        for j in range(i + 1, len(numbers)-1):

            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return (numbers[i]*numbers[j]*numbers[k])



if __name__ == "__main__":
    partone()
    print(parttwo())
