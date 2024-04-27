import json
import file_edit
from googletrans import Translator

import utils

def translate_json(json_file, target_language):
    # Load the JSON file
    with open(json_file, 'r',encoding='utf-8') as f:
        data = json.load(f)
    
    # Initialize the translator
    translator = Translator()
    
    # Translate each value in the JSON
    for key, value in data.items():
        if isinstance(value, dict):
            for k, v in value.items():
                translated_text = translator.translate(v, dest=target_language).text
                data[key][k] = translated_text
        else:
            translated_text = translator.translate(value, dest=target_language).text
            data[key] = translated_text
    
    # Write translated data to a new JSON file
    with open('jsons/'+target_language+".json", 'w',encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def translate_and_create_json(language: str, orj_json_dir: str):
    print(f"Translating to {language}")
    # Load the JSON file
    with open(orj_json_dir, encoding='utf-8') as f:
        data = json.load(f)

    # Initialize the translator
    translator = Translator()

    # Define the language to translate to
    # Replace with your desired language code (e.g. 'es' for Spanish, 'fr' for French, etc.)
    newFile = language+'.json'

    dir = utils.get_directory(orj_json_dir)

    newFile = dir+"/"+newFile

    unique_json = {}

    

    if utils.check_if_file_exists(newFile):
        new_fileJson = file_edit.get_json(newFile)
        unique_json = unique_json | utils.get_unique_json(data, new_fileJson)
    else:
        unique_json=data

    # Loop through each key-value pair in the JSON file and translate the value
    for key in unique_json.keys():
        value = unique_json[key]
        if '\n' in value:
            value = value.replace('\n', '')
        translation = ""
        try:
            translation = translator.translate(value, dest=language).text
        except Exception as e:
            translation = value
        unique_json[key] = translation

    if utils.check_if_file_exists(newFile):
        dataFromFile = file_edit.get_json(newFile)

        mergedData = dataFromFile | unique_json

        with open(newFile, "w", encoding='utf-8') as f:
            json.dump(mergedData, f,ensure_ascii=False)

    else:
        with open(newFile, 'w', encoding='utf-8') as f:
            json.dump(unique_json, f,ensure_ascii=False)
