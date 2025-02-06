PASSWORD_LENGTH = 10


def main():
    """get and print password using function"""
    user_password = get_password()
    print_asterisks(user_password)


def print_asterisks(user_password):
    """print asterisks as the length of characters in user's password"""
    print(user_password * "*")


def get_password():
    """get user's password meeting the required characters"""
    user_password = len(input("Enter your password: "))
    while user_password <= PASSWORD_LENGTH:
        print("Invalid Password")
        user_password = input("Enter your password: ")
    return user_password


main()
