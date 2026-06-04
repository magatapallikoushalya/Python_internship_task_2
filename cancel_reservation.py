rooms = {101: "Booked",102: "Available",103: "Booked"}
def cancel_reservation():
    room_no = int(input("Enter Room Number: "))
    if room_no in rooms and rooms[room_no] == "Booked":       
        print("Reservation Cancelled")
    else:
        print("No Reservation Found")
cancel_reservation()
