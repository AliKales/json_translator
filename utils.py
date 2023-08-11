import os
import re


def check_if_file_exists(filename):
    return os.path.exists(filename)


def get_files_in_directory(directory,file_extension):
    abs_directory = os.path.abspath(directory)
    files = []
    for root, directories, filenames in os.walk(abs_directory):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if file_path.endswith(file_extension):
                files.append(file_path)
    return files


def list_remove_starts_with(string_list, starts_with):
    return [string for string in string_list if not string.startswith(starts_with)]


# it will return a list
# 0= orj string
# 1= key
# 2= text
def get_dic_data(string: str):
    string_list = string.split("__")

    return [string, string_list[0][1:], string_list[1]]


pattern = r'''(['"])(.*?)__([^_]+)__\1'''  # Matching pattern: Quoted strings with double underscores


def get_all_matches(text: str):
    matches = re.findall(pattern, text)
    result = [match[0] + match[1] + '__' + match[2] + '__' + match[0]
              for match in matches]

    return result


def get_directory(filepath):
    directory = os.path.dirname(filepath)
    return directory

def get_locale_keys(text:str):
    pattern_locale_keys = r'LocaleKeys\.(\w+)\.tr\(\)'  # Matching pattern: LocaleKeys.randomText.tr()

    matches = re.findall(pattern_locale_keys, text)

    return matches

def get_unique_values(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    unique_values = list(set1.symmetric_difference(set2))
    return unique_values

def get_unique_json(dict1,dict2):
    unique_dict = {}

    for key, value in dict1.items():
        if key not in dict2:
            unique_dict[key] = value
    return unique_dict