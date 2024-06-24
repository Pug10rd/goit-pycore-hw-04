def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Please type name and number"


def change_contact(args, contacts):
    try: 
        name, phone = args
    except ValueError:
        return "Please type name and a new number"
    try:
        if contacts[name]:
            contacts[name] = phone
            return "Contact changed"
    except KeyError:
        return "Name does not exist"

def show_phone(args, contacts: dict):
    try:
        return f'{contacts[args[0]]}'
    except KeyError:
        return "Name does not exist"

def show_all(contacts):
    return f"{contacts}"

# def delete_contact(args, contacts: dict):
#     contacts.pop(*args)
#     return "Contact deleted"