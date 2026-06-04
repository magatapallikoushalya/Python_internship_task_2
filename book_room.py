rooms = {101: "Available",102: "Available",103: "Available"}
def book_room():
    room_no = int(input("Enter Room Number: "))
    if room_no in rooms and rooms[room_no] == "Available":
        rooms[room_no] = "Booked"
        print("Room Booked Successfully")
    else:
        print("Room Not Available")
book_room()
