import utils
import file_edit
import translator

json_file = {}

locale_keys = []

project_dir = input("Full file path to folder with----> ")

orj_lang_code = input(
    "What language are all texts in? (only language code)---> ").lower()

translation_langs = input(
    "What languages you want translations in? (language codes separated with comma)---> ").split(",")

is_delete_used = False

if input("Do you want to delete unused translations? (y/n)---> ") == "y":
    is_delete_used = True


all_file_paths = utils.get_files_in_directory(project_dir + "\\lib",".dart")


def handle_files(path: str):
    text = file_edit.read_file(path)

    l_k = utils.get_locale_keys(text)

    for value in l_k:
        locale_keys.append(value)

    all_matches = utils.get_all_matches(text)

    for match in all_matches:
        values = utils.get_dic_data(match)

        orj_val = values[0]
        key = values[1]
        value = values[2]

        json_file[key] = value

        new_value = f'LocaleKeys.{key}.tr()'

        text = text.replace(orj_val, new_value)

    file_edit.write_new_text(path, text)


for path in all_file_paths:
    handle_files(path)

dir_to_orj_json = project_dir + "\\assets\\translations\\"+orj_lang_code+".json"

if  is_delete_used and utils.check_if_file_exists(dir_to_orj_json):
    keys_from_json = file_edit.get_json_keys(dir_to_orj_json)

    unique_keys = utils.get_unique_values(keys_from_json, locale_keys)

    current_translation_files = utils.get_files_in_directory(
        project_dir + "\\assets\\translations",".json")
    
    for f in current_translation_files:
        file_edit.delete_values_from_json(f, unique_keys)

file_edit.write_dict_to_json(json_file, dir_to_orj_json)

for lang_code in translation_langs:
    print(f"Translating from {orj_lang_code} to {lang_code}")

    translator.translate_and_create_json(
        language=lang_code, orj_json_dir=dir_to_orj_json)
