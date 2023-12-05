import json


def get_events_data():
    try:
        with open('events.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('events.json', 'w') as f:
            json.dump([], f)
            return []


class Event:
    def __init__(self, name, date, location, resources, category):
        data = get_events_data()
        self.id = data[-1]['id'] + 1 if data else 1
        self.name = name
        self.date = date
        self.category = category
        self.location = location
        self.resources = resources

    def add_event(self, user_id):
        new_event = {
            'id': self.id,
            'name': self.name,
            'date': self.date,
            'category': self.category,
            'location': self.location,
            'participant': [user_id],
            'resources': self.resources
        }
        data = get_events_data()
        data.append(new_event)
        with open('events.json', 'w') as f:
            json.dump(data, f, indent=4)
        return self.id
