from shared.utils import parse_input
from wrappers import phone_handler, edit_handler
from storage import contacts

leave_commands = ['close', 'exit', 'vihod']


def exit():
    print("Good bye!")

def hello():
    print('How can I help you?')

def all():
    if not len(contacts.keys()):
        print('No Names, no numbers')
    else:
        for name in contacts.keys():
            print(name + ':' + contacts[name])

@phone_handler
def phone(args):
    print(contacts[args[0]])

@edit_handler
def edit(args):
    print(f"Contact {args[0]} updated with number {args[1]}")


config = {
    'hello': lambda args: hello(),
    'all': lambda args: all(),
    'phone': lambda args: phone(args),
    'add': lambda args: edit(args),
    'change': lambda args: edit(args),
}


def main():
    data = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *input_parametres = parse_input(user_input)

            for parameter in input_parametres:
                parameter = parameter.lower()

            if command in leave_commands:
                exit()
                break

            if command in config.keys():
                config[command](input_parametres)
            else:
                print("Invalid command.")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()