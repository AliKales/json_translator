import json
import file_edit
from googletrans import Translator

# /Users/kales/Documents/code/flutter/projects/hablo/assets/translations/

translator = Translator()

translation_langs = input(
    "What languages you want translations in? (language codes separated with comma)---> ").split(",")

orj_json_dir = input("Full path to json file---> ")
data = json.load(open(orj_json_dir+"new.json", 'r',encoding='utf-8'))

for lang in translation_langs:
    enData = json.load(open(orj_json_dir+lang+".json", 'r',encoding='utf-8'))
    keys = data.keys()

    for key in keys:
        for key2 in data[key].keys():
            val = data[key][key2]
            if key not in enData:
                enData[key] = {}

            if lang == "en":
                enData[key][key2] = val
            else:                
                transLang = lang
                if transLang == "zh":
                    transLang = "zh-CN"
                enData[key][key2] = translator.translate(val,dest=transLang).text

    with open(orj_json_dir+lang+".json", 'w',encoding='utf-8') as f:
        json.dump(enData, f, indent=4, ensure_ascii=False)
