import json

def read_room_descriptions(room_file):
    if room_file is not None:
        try:
            room_descriptions = room_file.read().decode('utf-8').splitlines()
            return room_descriptions
        except Exception as e:
            print(f"Error reading Text data: {e}")
            return []
    else:
        return []

def read_attribute_dictionary(attributes_file):
    if attributes_file is not None:
        try:
            attributes_data = attributes_file.read().decode('utf-8') 
            attributes = json.loads(attributes_data) 
            return attributes
        except Exception as e:
            print(f"Error reading JSON data: {e}")
            return {}
    else:
        return {}
