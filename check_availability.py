rooms = {101: "Available",102: "Booked",103: "Available"}
def check_availability():
    room_no = int(input("Enter Room Number: "))
    if room_no in rooms:
        print("Room Status:", rooms[room_no])
    else:
        print("Room Not Found")
check_availability()
