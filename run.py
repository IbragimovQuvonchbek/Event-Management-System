from functions import signup, login, add_event, all_events, register_event, search_by_name, search_by_date, \
    search_by_category, own_events, edit_event, delete_event, registered_events

while True:
    print("exit | sign up | log in (0|1|2): ")
    option = int(input('option: '))
    current_user_id = -1
    if option == 0:
        break
    elif option == 1:
        print("Sign up")
        current_user_id = signup()
    if option == 1 or option == 2:
        print("Log in")
        current_user_id = login()

    while current_user_id != -1:
        print("back | view events | create event | registered event | own events(0|1|2|3|4): ")
        option = int(input('option: '))
        if option == 0:
            break
        elif option == 1:
            print("======================View Events Section=================================")
            while True:
                print("back | search by name | search by date | search by category | all events(0|1|2|3|4): ")
                option = int(input('option: '))
                if option == 0:
                    break
                elif option == 1:
                    name = input("event name: ")
                    search_by_name(name)
                    while True:
                        print("back | register for event(0|1): ")
                        option = int(input('option: '))
                        if option == 0:
                            break
                        elif option == 1:
                            event_id = int(input('event id: '))
                            register_event(user_id=current_user_id, event_id=event_id)
                elif option == 2:
                    date = input("event date(yyyy-mm-dd): ")
                    search_by_date(date)
                    while True:
                        print("back | register for event(0|1): ")
                        option = int(input('option: '))
                        if option == 0:
                            break
                        elif option == 1:
                            event_id = int(input('event id: '))
                            register_event(user_id=current_user_id, event_id=event_id)
                elif option == 3:
                    category = input("event name: ")
                    search_by_name(category)
                    search_by_category(category)
                    while True:
                        print("back | register for event(0|1): ")
                        option = int(input('option: '))
                        if option == 0:
                            break
                        elif option == 1:
                            event_id = int(input('event id: '))
                            register_event(user_id=current_user_id, event_id=event_id)
                elif option == 4:
                    all_events()
                    while True:
                        print("back | register for event(0|1): ")
                        option = int(input('option: '))
                        if option == 0:
                            break
                        elif option == 1:
                            event_id = int(input('event id: '))
                            register_event(user_id=current_user_id, event_id=event_id)
        elif option == 2:
            print("======================Create Event Section=================================")
            add_event(current_user_id)
        elif option == 3:
            print("======================Registered Events Section=================================")
            registered_events(current_user_id)
            print("unregister or register")
            event_id = int(input('event id: '))
            register_event(user_id=current_user_id, event_id=event_id)
        elif option == 4:
            print("======================Own Events Section=================================")
            while True:
                own = own_events(current_user_id)
                if own:
                    print("back | edit | delete(0|1|2): ")
                    option = int(input('option: '))
                    if option == 0:
                        break
                    elif option == 1:
                        event_id = int(input("event id: "))
                        edit_event(current_user_id, event_id)
                    elif option == 2:
                        event_id = int(input("event id: "))
                        delete_event(current_user_id, event_id)
                        print("===========================================")
                else:
                    break
