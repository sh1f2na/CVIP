import random
import string


def generate_password(length, upper_case, lower_case, digits, special_chars):
    chars = ""
    if upper_case:
        chars += string.ascii_uppercase
    if lower_case:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        return "No character set selected. Please choose at least one."

    password = "".join(random.choice(chars) for _ in range(length))
    return password


def main():
    print("Random Password Generator")
    print("-------------------------")

    length = int(input("Enter the password length: "))
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
    use_digits = input("Include digits? (yes/no): ").lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"

    password = generate_password(
        length, use_uppercase, use_lowercase, use_digits, use_special_chars
    )

    print("Your generated password is:", password)


if __name__ == "__main__":
    main()
