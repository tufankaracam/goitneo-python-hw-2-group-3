from collections import UserDict

class PhoneFormat(Exception):
    def __init__(self):
        super().__init__('Phone number must have 10 numbers and must contain just numbers!')

class Field:
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return self.value

class Name(Field):
    pass

class Phone(Field):
    def __init__(self,value):
        if not self.validate_phone(value):
            raise PhoneFormat()
        super().__init__(value)

    def validate_phone(self, value):
        return value.isdigit() and len(value) == 10
        
        
class Record:
    def __init__(self,name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return 'You already have this phone number.'
        self.phones.append(phone)
        return 'Phone number added.'

    def remove_phone(self,phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(phone)
                return 'Phone number removed.'
        return 'Phone number not found.'

    def edit_phone(self,phone1,phone2):
        for p in self.phones:
            if p.value == phone1:
                p.value = phone2
                return 'Phone number added.'
        return 'Phone number not found.'

    def find_phone(self,phone):
        phone = Phone(phone)
        for p in self.phones:
            if p.value == phone.value:
                return p.value 
        return 'Phone number not found.'

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join([p.value for p in self.phones])}"
    
class AddressBook(UserDict):
    def add_record(self,record:Record):
        self.data[record.name.value] = record

    def find(self,name:Name):
        return self.data[name]

    def delete(self,name:Name):
        del self.data[name]
