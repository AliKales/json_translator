import utils
import file_edit
import translator

json_file = {}

project_dir = input("Full file path to folder of project----> ")

orj_lang_code = input(
    "What language are all texts in? (only language code)---> ").lower()

all_file_paths = utils.get_files_in_directory(project_dir + "\\lib", ".dart")


def handle_files(path: str):
    text = file_edit.read_file(path)

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


file_edit.write_dict_to_json(json_file, dir_to_orj_json)
