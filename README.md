# Woolf University. Python Programing Course. Homework – Basics of Working with Classes

## Overview

Design an address book management system using Python classes. You will implement entities for fields and contacts, as well as an `AddressBook` to manage them.

---

## Entities and Classes

1. **Field** (base class)

   * Common functionality for all record fields.

2. **Name**

   * Inherits from `Field`.
   * Stores the contact’s name.
   * **Required** field.

3. **Phone**

   * Inherits from `Field`.
   * Stores a phone number.
   * Validates format: must be exactly 10 digits.

4. **Record**

   * Stores a `Name` object and a list of `Phone` objects.
   * Methods:

     * `add_phone(phone: Phone) -> None`
     * `remove_phone(phone: str) -> bool`
     * `edit_phone(old: str, new: str) -> bool`
     * `find_phone(number: str) -> bool`

5. **AddressBook**

   * Inherits from `dict` or uses an internal `dict` to map names to `Record` objects.
   * Methods:

     * `add_record(record: Record) -> None`
     * `find(name: str) -> Record | None`
     * `delete(name: str) -> bool`

---

## Functionality Requirements

1. **AddressBook**

   * Add new records.
   * Search for records by name.
   * Delete records by name.

2. **Record**

   * Add a phone number.
   * Remove a phone number.
   * Edit an existing phone number.
   * Search for a phone number in the record.

3. **Phone**

   * Validate input: ensure the phone number string consists of exactly 10 digits (no letters or symbols).

---

## Evaluation Criteria

### `AddressBook`

* Implements `add_record(record: Record)` to add to `self.data` or internal mapping.
* Implements `find(name: str) -> Record | None` to retrieve a record.
* Implements `delete(name: str) -> bool` to remove a record and return success.

### `Record`

* Stores a `Name` object in an attribute (e.g., `self.name`).
* Stores a list of `Phone` objects (e.g., `self.phones`).
* Implements `add_phone`, `remove_phone`, `edit_phone`, and `find_phone` methods with correct behavior.

### `Phone`

* Validates format on instantiation or via a setter:

  * Accepts only digit strings of length 10.
  * Raises `ValueError` on invalid format.

---
