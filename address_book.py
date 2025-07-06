from collections import UserDict
from typing import List, Optional

class Field:
    """Base class for record fields."""
    
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

class Name(Field):
    """Class for storing contact name. Required field."""
    pass

class Phone(Field):
    """Class for storing phone number. Must contain exactly 10 digits."""
    
    def __init__(self, value: str) -> None:
        if not self.validate_phone(value):
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)
    
    def validate_phone(self, phone: str) -> bool:
        """Validate that phone number contains exactly 10 digits."""
        return phone.isdigit() and len(phone) == 10

class Record:
    """Class for storing contact information including name and phone numbers."""
    
    def __init__(self, name: str) -> None:
        self.name: Name = Name(name)
        self.phones: List[Phone] = []

    def add_phone(self, phone: str) -> None:
        """Add a phone number to the record."""
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
    
    def remove_phone(self, phone: str) -> None:
        """Remove a phone number from the record."""
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone {phone} not found in record")
    
    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit an existing phone number."""
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            # Validate new phone number by creating temporary Phone object
            temp_phone = Phone(new_phone)
            phone_to_edit.value = new_phone
        else:
            raise ValueError(f"Phone {old_phone} not found in record")
    
    def find_phone(self, phone: str) -> Optional[Phone]:
        """Find a phone number in the record."""
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """Class for storing and managing contact records."""
    
    def add_record(self, record: Record) -> None:
        """Add a record to the address book."""
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Optional[Record]:
        """Find a record by name."""
        return self.data.get(name)
    
    def delete(self, name: str) -> None:
        """Delete a record by name."""
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name '{name}' not found")

# Example usage and testing
if __name__ == "__main__":
    # Create new address book
    book = AddressBook()

    # Create record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John's record to address book
    book.add_record(john_record)

    # Create and add new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print all records in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit phone for John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)

    # Search for specific phone in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    # Delete Jane's record
    book.delete("Jane")
    
    # Verify Jane is deleted
    print("\nAfter deleting Jane:")
    for name, record in book.data.items():
        print(record)
