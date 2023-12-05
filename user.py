import json
from hashlib import blake2b

def get_users_data():
    try:
        with open('users.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('users.json', 'w') as f:
            json.dump([], f)
            return []


class User:
    id = -1

    def __init__(self, name, surname, username, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.__password = password

    def add_new_user(self):
        if not self._is_exists():
            data = get_users_data()
            self.id = data[-1]['id'] + 1 if data else 1
            new_user = {
                'id': self.id,
                'username': self.username,
                'name': self.name,
                'surname': self.surname,
                'my_events': [],
                'registered_events': [],
                'password': blake2b(self.__password.encode('utf-8')).hexdigest()
            }
            data.append(new_user)
            with open('users.json', 'w') as f:
                json.dump(data, f, indent=4)
        return self.id

    def _is_exists(self):
        data = get_users_data()
        for user in data:
            if user['username'] == self.username:
                return True
        return False
