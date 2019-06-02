clients = 'pablo, ricardo,'

def create_client(client_name):
    global clients #permite ocupar la var global dentro del scope de la funcion
    clients += client_name
    _add_comma()


def list_clients():
    global clients
    print(clients)    


def _add_comma():
    global clients
    clients += ', '


def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()

    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('Invalid command')