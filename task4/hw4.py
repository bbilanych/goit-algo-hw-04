def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    name, = args
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Invalid command.")
            continue

        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print("Invalid command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Invalid command.")
            else:
                print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Invalid command.")
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
