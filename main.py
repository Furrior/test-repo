import random

def generate_random_number():
    """Generate a random number between 1 and 100"""
    return random.randint(1, 100)

def main():
    random_number = generate_random_number()
    print(f"Random number: {random_number}")
    if random_number > 50:
        print("The number is greater than 50!")
    else:
        print("The number is less than or equal to 50!")

if __name__ == "__main__":
    main()