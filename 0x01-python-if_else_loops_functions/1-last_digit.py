import random
number = random.randint(-10000, 10000)
number=abs(number)
last_digit=abs(number%10)
if last_digit == 0:
    print(f"{last_digit} is zero")
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0 ")