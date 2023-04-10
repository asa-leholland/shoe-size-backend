import json

def convert_size(data_path, gender=None, size=None, location=None, converted_location=None):
    with open(data_path) as f:
        data = json.load(f)

    if not any([gender,size,location,converted_location]):
        return data

    if not any([location,converted_location,size]):
        # filter the result so it is only matching the gender
        gender_filtered = []
        for entry in data:
            if entry["Unit"] == gender:
                gender_filtered.append(entry)
        return gender_filtered

    for item in data:
        if item["Unit"] == gender:
            if not any([size]):
                return item
            index = item[location].index(size)
            return item[converted_location][index]