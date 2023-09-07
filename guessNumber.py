import random

def guess_number():
    n = int(input("Enter the minimum value: "))
    m = int(input("Enter the maximum value: "))
    if n > m:
        print("The minumum value must be less than the maximum value.")
        return
    target_number = random.randint(n, m)
    max_attempts = 5
    for attempt in range(max_attempts):
        guess = int(input(f"Expected value. (must be in the range of {n} to {m}): "))
        if guess == target_number:
            print(f"Correct answer!")
            return
        elif guess > target_number:
            print("Large number.")
        else:
            print("Smaller number.")
    print(f"Too bad! The correct answer is {target_number}.")
guess_number()
