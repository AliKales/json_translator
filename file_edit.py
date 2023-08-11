import os
import json
import utils
from collections import OrderedDict


def read_file(file_path):
    with open(file_path, 'r') as file:
        txt = file.read()
    file.close()
    return txt


def write_new_text(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
    file.close()


def write_dict_to_json(dictionary, filepath):
    # Create directory if it doesn't exist
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if utils.check_if_file_exists(filepath):
        # Step 1: Read the JSON file
        with open(filepath, 'r') as file:
            data = json.load(file)
        dictionary = {**data, ** dictionary}
        file.close()

    dictionary = OrderedDict(sorted(dictionary.items(), key=lambda t: t[0]))

    # Write dictionary to JSON file
    with open(filepath, 'w') as file:
        json.dump(dictionary, file)
    file.close()


def get_json_keys(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        keys = list(data.keys())
        return keys


def get_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            return data
        except Exception:
            return {}

def delete_values_from_json(file_path, keys):
    with open(file_path, 'r') as file:
        data = json.load(file)
        for key in keys:
            if key in data:
                del data[key]

    with open(file_path, 'w') as file:
        json.dump(data, file)
