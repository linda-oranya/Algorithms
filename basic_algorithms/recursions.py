def factorial(number):
    if number < 0:
        return 0
    elif number == 0 or number == 1:
        return 1
    else:
        val = 1
        while number > 1:  # 1
            val *= number  # val = 5*1 = 5*4*3*2
            number -= 1  # number = 5-1 = 4-1-1-1
        return val  # 120


def recursive_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * recursive_factorial(number - 1)


# print('1st', factorial(6))
# print('2nd', recursive_factorial(6))


# optimized factorial
def optimized_factorial(number, memory={0: 1, 1: 1}):
    if number in memory:
        return memory[number]
    else:
        memory[number] = number * optimized_factorial(number - 1)
        return memory[number]


# print(optimized_factorial(7))


# fibonnacci recursive
def recursive_fibonnacci(n):  # 10
    if n <= 1:
        return n
    else:
        return recursive_fibonnacci(n - 1) + recursive_fibonnacci(n - 2)


terms = 10
if terms <= 0:
    print('value less than 0')
else:
    print('series')
for i in range(terms):
    print(recursive_fibonnacci(i))
