import json

from event import Event, get_events_data
from user import User, get_users_data
from hashlib import blake2b


def signup():
    name = input('name: ')
    surname = input('surname: ')
    username = input('username: ')
    password = input('password: ')
    new = User(name, surname, username, password)
    register = new.add_new_user()
    if register == -1:
        print('username already exists')
    return register


def login():
    username = input('username: ')
    password = blake2b(input('password: ').encode('utf-8')).hexdigest()
    data = get_users_data()
    for user in data:
        if user['username'] == username and user['password'] == password:
            print('succeed')
            return user['id']
    print('incorrect username or password')
    return -1


def add_event(user_id):
    name = input('name: ')
    date = input('date(yyyy-mm-dd): ')
    location = input('location: ')
    category = input('category: ')
    resources = input('resources: ')
    new = Event(name=name, date=date, location=location, category=category, resources=resources)
    event_id = new.add_event(user_id)
    user_data = get_users_data()
    for user in user_data:
        if user['id'] == user_id:
            user['my_events'].append(event_id)
            user['registered_events'].append(event_id)
    with open('users.json', 'w') as f:
        json.dump(user_data, f, indent=4)


def register_event(user_id, event_id):
    user_data = get_users_data()
    event_data = get_events_data()
    is_creator = False
    for user in user_data:
        if user['id'] == user_id:
            if event_id not in user['registered_events']:
                user['registered_events'].append(event_id)
                print("registered")
            elif event_id not in user['my_events']:
                user['registered_events'].remove(event_id)
                print("unregistered")
            else:
                is_creator = True
                print("you can not unregister event, you are creator, you can delete event in delete section")
    for event in event_data:
        if event['id'] == event_id:
            if user_id not in event['participant']:
                event['participant'].append(user_id)
            elif not is_creator:
                event['participant'].remove(user_id)
    with open('users.json', 'w') as f:
        json.dump(user_data, f, indent=4)
    with open('events.json', 'w') as f:
        json.dump(event_data, f, indent=4)


def delete_event(user_id, event_id):
    try:
        user_data = get_users_data()
        event_data = get_events_data()
        for user in user_data:
            if user['id'] == user_id:
                user['my_events'].remove(user_id)
            if event_id in user['registered_events']:
                user['registered_events'].remove(event_id)
        for event in event_data:
            if event['id'] == event_id:
                event_data.remove(event)
        with open('users.json', 'w') as f:
            json.dump(user_data, f, indent=4)
        with open('events.json', 'w') as f:
            json.dump(event_data, f, indent=4)
        print("removed")
    except ():
        print("incorrect id")


def edit_event(user_id, event_id):
    user_data = get_users_data()
    event_data = get_events_data()
    user_found = False
    event_found = False

    for user in user_data:
        if user['id'] == user_id and event_id in user['my_events']:
            user_found = True
            for event in event_data:
                if event['id'] == event_id:
                    event_found = True
                    name = input('change name (to skip press enter): ')
                    date = input('change date (yyyy-mm-dd) (to skip press enter): ')
                    location = input('change location (to skip press enter): ')
                    category = input('change category (to skip press enter): ')
                    resources = input('change resources (to skip press enter): ')

                    event['name'] = name if len(name) != 0 else event['name']
                    event['date'] = date if len(date) != 0 else event['date']
                    event['location'] = location if len(location) != 0 else event['location']
                    event['category'] = category if len(category) != 0 else event['category']
                    event['resources'] = resources if len(resources) != 0 else event['resources']

                    print("Event updated successfully.")
                    break

    if not user_found:
        print("User not found.")
    elif not event_found:
        print("Event not found for the given user.")

    with open('events.json', 'w') as f:
        json.dump(event_data, f, indent=4)

    with open('users.json', 'w') as f:
        json.dump(user_data, f, indent=4)


def all_events():
    data = get_events_data()
    for event in data:
        print("===========================================================")
        print(f"Id: {event['id']}")
        print(f"Name: {event['name']}")
        print(f"Date: {event['date']}")
        print(f"Category: {event['category']}")
        print(f"Location: {event['location']}")
        print(f"Resources: {event['resources']}")
        print(f"Participants: {len(event['participant'])} people")
        print("===========================================================")

    if not data:
        print("no events found")


def search_by_name(name):
    data = get_events_data()
    count = 0
    for event in data:
        if name in event['name'].lower():
            print("===========================================================")
            print(f"Id: {event['id']}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Category: {event['category']}")
            print(f"Location: {event['location']}")
            print(f"Resources: {event['resources']}")
            print(f"Participants: {len(event['participant'])} people")
            print("===========================================================")
            count += 1
    if count == 0:
        print("no events found")


def search_by_date(date):
    data = get_events_data()
    count = 0
    for event in data:
        if date in event['date'].lower():
            print("===========================================================")
            print(f"Id: {event['id']}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Category: {event['category']}")
            print(f"Location: {event['location']}")
            print(f"Resources: {event['resources']}")
            print(f"Participants: {len(event['participant'])} people")
            print("===========================================================")
            count += 1

    if count == 0:
        print("no events found")


def search_by_category(category):
    data = get_events_data()
    count = 0
    for event in data:
        if category in event['category'].lower():
            print("===========================================================")
            print(f"Id: {event['id']}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Category: {event['category']}")
            print(f"Location: {event['location']}")
            print(f"Resources: {event['resources']}")
            print(f"Participants: {len(event['participant'])} people")
            print("===========================================================")
            count += 1

    if count == 0:
        print("no events found")


def own_events(current_user):
    user_data = get_users_data()
    event_data = get_events_data()
    own_event = []
    for user in user_data:
        if user['id'] == current_user:
            own_event = user['my_events']
            break

    for event in event_data:
        if event['id'] in own_event:
            print("===========================================================")
            print(f"Id: {event['id']}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Category: {event['category']}")
            print(f"Location: {event['location']}")
            print(f"Resources: {event['resources']}")
            print(f"Participants: {len(event['participant'])} people")
            print("===========================================================")

    if not own_event:
        print("no events found")

    return len(own_event) != 0


def registered_events(user_id):
    users_data = get_users_data()
    events_data = get_events_data()
    registered = []
    for user in users_data:
        if user['id'] == user_id:
            registered = user['registered_events']
            break
    for event in events_data:
        if event['id'] in registered:
            print("===========================================================")
            print(f"Id: {event['id']}")
            print(f"Name: {event['name']}")
            print(f"Date: {event['date']}")
            print(f"Category: {event['category']}")
            print(f"Location: {event['location']}")
            print(f"Resources: {event['resources']}")
            print(f"Participants: {len(event['participant'])} people")
            print("===========================================================")

