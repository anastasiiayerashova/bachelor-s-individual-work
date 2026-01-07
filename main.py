from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):

        if not name or not name.strip():
            raise ValueError('Name cannot be empty')
        
        super().__init__(name.strip())


class Phone(Field):
    def __init__(self, phone: str):
        phone = phone.strip()

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError('Phone number must be exactly 10 digits and contain only numbers')

        super().__init__(phone)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone (self, phone: str):
        new_phone = Phone(phone)

        if new_phone.value not in [p.value for p in self.phones]:
            self.phones.append(new_phone)
            return f'Phone number {new_phone.value} added to contact'
        else:
            return 'Phone number already exists in contact'

    def remove_phone (self, phone: str):
        phone_to_remove = phone.strip()

        for p in self.phones:

            if p.value == phone_to_remove:
                self.phones.remove(p)
                return f'Phone number {phone_to_remove} removed from contact'
            
        raise ValueError('Phone number not found in contact')

    def edit_phone (self, old_phone: str, new_phone: str):
        old_phone = old_phone.strip()
        new_phone = new_phone.strip()

        for i, p in enumerate(self.phones):
            
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return f'Phone number {old_phone} changed to {new_phone}'
            
        raise ValueError('Old phone number not found in contact')
    
    def find_phone (self, phone: str):
        phone_to_find = phone.strip()

        for p in self.phones:

            if p.value == phone_to_find:
                return f'Phone number {phone_to_find} found in contact'
            
        return f'Phone number {phone_to_find} not found in contact'

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record (self, record: Record):
        self.data[record.name.value] = record

        return f'Record for {record.name.value} added to address book'
    
    def delete (self, name: str):
        name_to_delete = name.strip()

        if name_to_delete in self.data:
            del self.data[name_to_delete]

        return f'Record for {name_to_delete} deleted from address book'
        
    def find (self, name: str):
        name_to_find = name.strip()

        return self.data.get(name_to_find, None)


if __name__ == "__main__":
        
    book = AddressBook()

   
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

   
    book.add_record(john_record)

   
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    
    for name, record in book.data.items():
        print(record)

   
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  

   
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  

    
    book.delete("Jane")



    