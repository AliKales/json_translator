import utils
import file_edit

dir_to_orj_json = input("Path to json file---> ")

if  utils.check_if_file_exists(dir_to_orj_json):
    keys_from_json = file_edit.get_json_keys(dir_to_orj_json)

    unique_keys = utils.get_unique_values(keys_from_json, locale_keys)

    current_translation_files = utils.get_files_in_directory(
        project_dir + "\\assets\\translations",".json")
    
    for f in current_translation_files:
        file_edit.delete_values_from_json(f, unique_keys)