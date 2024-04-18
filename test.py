def available_rooms(floor):
    prevroom = 0
    rooms = []
    available = []
    for room in floor:
        if prevroom == 0:
            prevroom = room
            rooms.append(room)
        else:
            if room == prevroom + 1:
                rooms.append(room)
                prevroom = room
            else:
                available.append(rooms)
                rooms = [room]
                prevroom = room
    available.append(rooms)
    return available

floor1 = [1,2,3,5,6,7,11,13]

print(available_rooms(floor1))
