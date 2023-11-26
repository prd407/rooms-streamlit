from segmind import DvArch

def get_matching_attributes(room_descriptions, attribute_dict):
    matching_attributes = {key: [] for key in attribute_dict}

    description_words = set()
    for desc in room_descriptions:
        description_words.update(desc.lower().split())

    for attribute_type, attribute_values in attribute_dict.items():
        for value in attribute_values:
            if value.lower() in description_words:
                matching_attributes[attribute_type].append(value.lower())

    for key, value in matching_attributes.items():
        matching_attributes[key] = list(set(value))
    
    return matching_attributes

def get_image_from_segmind(room_description):
    model = DvArch(api_key="SG_027d719da5993c2f") #quick test kept raw key in code 
    img = model.generate(prompt=room_description)
    # img.show()
    return img