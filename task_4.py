def input_error(func):
    """
    A decorator to handle input errors.
    Handles ValueError, KeyError, and IndexError exceptions.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Error: contact not found."
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    """
    Parses user input into a command and arguments.
    """
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


@input_error
def add_contact(args, contacts):
    """
    Adds a new contact to the dictionary.
    """
    if len(args) < 2:
        raise ValueError  # Raises ValueError if the input is incomplete
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


@input_error
def change_contact(args, contacts):
    """
    Updates the phone number for an existing contact.
    """
    if len(args) < 2:
        raise ValueError  # Raises ValueError if the input is incomplete
    name, phone = args
    if name not in contacts:
        raise KeyError  # Raises KeyError if the contact does not exist
    contacts[name] = phone
    return f"Contact {name} updated."


@input_error
def show_phone(args, contacts):
    """
    Returns the phone number for the contact.
    """
    if not args:
        raise IndexError  # Raises IndexError if no argument is passed
    name = args[0]
    return contacts.get(name, f"Error: contact {name} not found.")


@input_error
def show_all(contacts):
    """
    Outputs all saved contacts.
    """
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    """
    Main function that handles user interaction in an infinite loop.
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


# Usage:
if __name__ == "__main__":
    main()