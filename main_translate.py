import translator
import utils

translation_langs = input(
    "What languages you want translations in? (language codes separated with comma)---> ").split(",")

orj_json_dir = input("Full path to json file---> ")

if utils.check_if_file_exists(orj_json_dir):
    for lang in translation_langs:
        translator.translate_json(orj_json_dir,lang)
        # translator.translate_and_create_json(lang,orj_json_dir)