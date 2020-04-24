#python program that will collect 6 numbers from the User, display on the screen, will draw 6 numbers on it's own and display it and finally will inform how many numbers would match.
import random

#function that will collect number from the User:
def choice():
    while True:
        try:
            result = int(input("Please pick your number:"))
            break
        except ValueError:
            print("This is not a number")

    return result

#function that will collect 6 different numbers from users:
def user_numbers():
    result = set()
    while len(result) < 6:
        number = choice()
        if 0 < number <= 49:
            result.add(number)

    return result

#function that will display choosen numbers in sorted order:
def print_numbers(numbers):
    print(", ".join(str(number) for number in sorted(numbers)))

#funtion that will draw six numbers from range between 1 and 49:
def drawing_numbers():
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]

#function comparing users numbers to drawn numbers
def lotto():
    user_numbers = choice()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

#part of function matching numbers
    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!"

#tego nie rozumiem - pojawia się błąd którego nie ograniam - do popytania M/W
if __name__ == '__main__'
    lotto()