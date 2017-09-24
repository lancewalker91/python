#database.py
import sys,shelve
def store_person(db):
    pid = input('Enter a unique number:')
    person = {}
    person['name'] = input('Enter name:')
    person['age'] = input('Enter age:')
    person['phone'] = input('Enter phone number:')
    db[pid] = person
def lookup_person(db):
    pid = input('Enter ID number:')
    filed = input('what would like to know?(name,age,phone)')
    filed = filed.strip().lower()
    print(filed.capitalize() + ':',db[pid][filed])

def print_hlep():
    print('The available commands are:')
    print('store:Stores information about a person')
    print('lookup:Looks up a person from ID number')
    print('quit:Save changes')
    print('?:Print this message')

def enter_command():
    cmd = input('Enter command (? for help):')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('C:\\database.dat')
    try:
        cmd = enter_command()
        if cmd == 'store':
            store_person(database)
        elif cmd == 'lookup':
            lookup_person(database)
        elif cmd == '?':
            print_hlep()
        elif cmd =='quit':
            return
    finally:
        database.close()

if __name__ == '__main__':
    main()