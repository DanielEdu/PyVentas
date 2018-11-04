#funciones help(nombre_function)
#dir(obj)
clients = 'Daniel,Pablo,Juan'

def welcome():
    print('''
 __      _____ _    ___ ___  __  __ ___ _   
 \ \    / / __| |  / __/ _ \|  \/  | __| |
  \ \/\/ /| _|| |_| (_| (_) | |\/| | _||_|
   \_/\_/ |___|____\___\___/|_|  |_|___(_)
     
   ''') 
    print('*'*50)
    print('What would you like to day?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[L]ist   clients')


def create_client(client):
    global clients
    
    if client not in clients:
        _add_coma()
        clients += client
    else:
        print('Client alreay exists')


def delete_client(client):
    global clients
    if client in clients:
        clients = clients.replace(','+client,'')
    else:
        print('Client does not exists')


def update_client(old_client,new_client):
    global clients
    if old_client in clients:
        clients = clients.replace(old_client,new_client)
    else:
        print('Client does not exists')

def _add_coma():
    global clients
    clients += ','

def _get_client():
    client = input('What is the client name? ')
    return client

def list_clients():
    global clients
    print (clients)


if __name__=='__main__':
    welcome()
    command =input()
    command = command.upper()
    
    if command == 'C':
        create_client(_get_client())

    elif command == 'D':
        delete_client(_get_client())

    elif command == 'U':
        old_client = _get_client()
        new_client = input('What is the new client?')
        update_client(old_client,new_client)

    elif command == 'L':
        list_clients()

    else:
        print('Invalid commad')

    list_clients()




 #####   
