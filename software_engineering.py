#Joseph Tebou
def encoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) + 3) % 10)
        result += new_digit
    return result


def decoder(message):
    result = ''
    for digit in message:
        new_digit = str((int(digit) - 3) % 10)
        result += new_digit
    return result


def main():
    while True:
        print("1. To encode")
        print("2. To decode")
        print("3. To exit")
        choice = input("Enter your choice (1 or 2 or 3): ")
        if choice == "1":
            value = input("Enter an 8-digit password: ")
            print("Encoded password is", encoder(value))
        elif choice == "2":
            value = input("Enter an already encoded 8-digit password: ")
            print("Decoded password is", decoder(value))
        elif choice == "3":
            break
        else:
            print("Invalid choice")
        print()


main()

