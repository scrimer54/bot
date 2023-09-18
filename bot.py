import functools

contacts = {}


def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Error: Invalid input. Try again."

    return wrapper


def hello():
    return "How can I help you?"


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"The contact {name} with the number {phone} has been added."


@input_error
def change_contact(name, new_phone):
    contacts[name] = new_phone
    return f"The phone number for {name} has been changed to{new_phone}."


@input_error
def phone_contact(name):
    return f"Phone number for {name}: {contacts[name]}"


def show_all_contacts():
    if not contacts:
        return "You have no contacts saved."
    
    result = "List of contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    
    return result.strip()


def main():
    print("Welcome to the helper bot!")
    
    while True:
        user_input = input("Enter the command (or 'exit' to finish): ").lower()
        
        if user_input == "exit" or user_input == "good bye" or user_input == "close":
            print("Good bye!")
            break
        elif user_input == "hello":
            print(hello())
        elif user_input.startswith("add"):
            _, name, phone = user_input.split(maxsplit=2)
            print(add_contact(name, phone))
        elif user_input.startswith("change"):
            _, name, new_phone = user_input.split(maxsplit=2)
            print(change_contact(name, new_phone))
        elif user_input.startswith("phone"):
            _, name = user_input.split(maxsplit=1)
            print(phone_contact(name))
        elif user_input == "show all":
            print(show_all_contacts())
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()
