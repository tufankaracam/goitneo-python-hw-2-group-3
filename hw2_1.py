
def input_error(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found!"
        except IndexError:
            return "Give me name please."
    return inner

@input_error
def add_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
  
@input_error
def change_contact(args,contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    else:
        contacts[name] = phone
        return 'Contact updated.'

@input_error         
def show_phone(args,contacts):
    return contacts[args[0]]
        

def show_all(contacts):
    return '\n'.join([f'{k:<10}: {v:>10}' for k,v in contacts.items()])

def parseCommands(input):
    if input=='':
        return '',[]
    
    cmd,*args = input.strip().lower().split()
    return cmd,args

def main():
    print('Welcome to the Contact Assistant!')
    contacts = {}
    while(True):
        cmd,args = parseCommands(input('>'))
        #print(f'cmd : {cmd} | commands : {args}')
        if cmd == 'hello':
            print('How can I help you?')
        elif (cmd =='close' or cmd =='exit'):
            print('Good bye!')
            break
        elif cmd =='phone':
            print(show_phone(args,contacts))
        elif cmd =='add':
            print(add_contact(args,contacts))
        elif cmd =='change':
            print(change_contact(args,contacts))
        elif cmd =='all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()