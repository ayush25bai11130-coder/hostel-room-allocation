# Hostel Room Allocation System

hostel_rooms = {101: None, 102: None, 103: None, 104: None, 105: None}
students = {}

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    if roll in students:
        print("Student already exists!")
        return

    students[roll] = {"name": name, "room": None}
    print("Student added successfully!")


def allocate_room():
    roll = input("Enter student roll number: ")

    if roll not in students:
        print("Student not found!")
        return

    print("\nAvailable Rooms:")
    for room, occupant in hostel_rooms.items():
        if occupant is None:
            print(room)

    room_no = int(input("\nEnter room number to allocate: "))

    if room_no not in hostel_rooms:
        print("Invalid room number!")
        return

    if hostel_rooms[room_no] is not None:
        print("Room already taken!")
        return

    hostel_rooms[room_no] = roll
    students[roll]["room"] = room_no

    print(f"Room {room_no} allocated to {students[roll]['name']}.")


def view_allocations():
    print("\n--- Room Allocations ---")
    for room, roll in hostel_rooms.items():
        if roll:
            print(f"Room {room}: {students[roll]['name']} (Roll: {roll})")
        else:
            print(f"Room {room}: Empty")


def remove_student():
    roll = input("Enter roll number to remove: ")

    if roll not in students:
        print("Student not found!")
        return

    room_no = students[roll]["room"]
    if room_no:
        hostel_rooms[room_no] = None

    del students[roll]
    print("Student removed successfully!")


def available_rooms():
    print("\nAvailable Rooms:")
    for room, roll in hostel_rooms.items():
        if roll is None:
            print(room)


def menu():
    while True:
        print("\n--- Hostel Room Allocation System ---")
        print("1. Add Student")
        print("2. Allocate Room")
        print("3. View Room Allocations")
        print("4. Remove Student")
        print("5. Show Available Rooms")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            allocate_room()
        elif choice == '3':
            view_allocations()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            available_rooms()
        elif choice == '6':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


menu()
