import requests

X_AUTH_TOKEN = '9e1ef4144dee79b0bd985e4480bee1ae'
BASE_URL = 'https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api/'

def start_simulation(problem_number): #authkey,problem,day
    response = requests.post(
        f"{BASE_URL}/start",
        headers={"X-Auth-Token": X_AUTH_TOKEN, "Content-Type": "application/json"},
        json={"problem": problem_number}
    )
    return response.json()

def fetch_new_requests(auth_key): #reservations_info:[id,amount,checkin,checkout]
    response = requests.get(
        f"{BASE_URL}/new_requests",
        headers={"Authorization": auth_key, "Content-Type": "application/json"}
    )
    return response.json()

def send_replies(auth_key, replies):
    response = requests.put(
        f"{BASE_URL}/reply",
        headers={"Authorization": auth_key, "Content-Type": "application/json"},
        json={"replies": replies}
    )
    return response.json()

def simulate_day(auth_key, room_assignments):
    response = requests.put(
        f"{BASE_URL}/simulate",
        headers={"Authorization": auth_key, "Content-Type": "application/json"},
        json={"room_assign": room_assignments}
    )
    return response.json()

def fetch_score(auth_key):
    response = requests.get(
        f"{BASE_URL}/score",
        headers={"Authorization": auth_key, "Content-Type": "application/json"}
    )
    return response.json()

def fetch_available_rooms(floor):
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



auth_response = start_simulation(1)
auth_key = auth_response['auth_key']
day = auth_response['day']
hotel = {}
for floor in range(1,4):
    floor_rooms = []
    for room in range(1,21):
        floor_rooms.append(int(str(floor) + str("%03d" % room)))
    hotel[floor] = floor_rooms

pending_requests = []
reservation_deadline = {}
while day <= 200:
    should_accept = {}
    replies = []
    room_assignments = []

    new_requests = fetch_new_requests(auth_key)
    for request in new_requests['reservations_info']:
        reservation_deadline[request['id']] = min(request['check_in_date'],day+14)

    pending_requests+=new_requests['reservations_info']

    for request in pending_requests:
        if reservation_deadline[request['id']]-day == 1:
            del reservation_deadline[request['id']]
            should_accept[request['id']] = request['amount']
            pending_requests.remove(request)

    should_accept_srt = sorted(should_accept.items(), key=lambda x:x[1], reverse=True)
    print(should_accept_srt)
    best_option = (20,[])
    for accept in should_accept_srt:
        for floor in hotel:
            available_rooms = fetch_available_rooms(hotel[floor])
            print(available_rooms)
            for rooms in available_rooms:
                if len(rooms) > accept[1] and len(rooms) < best_option[0]:
                    best_option = (len(rooms),rooms)
        if best_option[1] == []:
            replies.append({"id": accept[0], "reply": "refused"})
        else:
            replies.append({"id": accept[0], "reply": "accepted"})
            for room_number in range(accept[1]):
                room_assignments.append({"id": accept[0], "room_number":best_option[1][room_number]})

            reply_response = send_replies(auth_key, replies)


    simulate_response = simulate_day(auth_key, room_assignments)
    day = simulate_response['day']


# score = fetch_score(auth_key)
# print(score)