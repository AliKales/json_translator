import json

orj_json_dir = input("Full path to json file---> ")

# Read the JSON file
with open(orj_json_dir, 'r') as json_file:
    data = json.load(json_file)

# Extract keys
keys = data.keys()

# Generate Dart code
dart_code = ""
for key in keys:
    dart_code += f"static const {key} = '{key}';\n"

# Write Dart code to a new file
with open('output.dart', 'w') as dart_file:
    dart_file.write(dart_code)