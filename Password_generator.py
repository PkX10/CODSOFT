import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
    