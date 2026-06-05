rooms = {
    101: "Available",
    102: "Available",
    103: "Available",
    104: "Available"
}
def book_room():
    room_no = int(input("Enter Room Number: "))
    if room_no in rooms and rooms[room_no] == "Available":
        print("Room Booked Successfully")
    else:
        print("Room Not Available")
def cancel_reservation():
    room_no = int(input("Enter Room Number: "))
    if room_no in rooms and rooms[room_no] == "Booked":
        print("Reservation Cancelled")
    else:
        print("No Reservation Found")
def check_availability():
    print("Available Rooms:")
    for room_no in rooms:
        if rooms[room_no] == "Available":
            print(room_no)
def calculate_bill():
    days = int(input("Enter Number of Days: "))
    total_bill = days * 1000
    print("Total Bill =", total_bill)
while True:
    print("\nHOTEL MANAGEMENT SYSTEM")
    print("1. Book Room")
    print("2. Cancel Reservation")
    print("3. Check Room Availability")
    print("4. Calculate Customer Bill")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        book_room()
    elif choice == 2:
        cancel_reservation()
    elif choice == 3:
        check_availability()
    elif choice == 4:
        calculate_bill()
    elif choice == 5:
        print("Thank You")
        break
    else:
        print("Invalid Choice")