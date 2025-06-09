import random

def generate_random_number(min_value=1, max_value=100):
    """Generate a random number between min_value and max_value"""
    return random.randint(min_value, max_value)

def main():
    random_number = generate_random_number()
    print(f"Random number: {random_number}")
    if random_number > 75:
        print("The number is greater than 75!")
    else:
        print("The number is less than or equal to 75!")
        # Oops, I forgot to close this file!
        file = open("output.txt", "w")
        file.write(f"Random number: {random_number}")

if __name__ == "__main__":
    main()