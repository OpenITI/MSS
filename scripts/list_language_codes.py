import re
from openiti.helper.funcs import get_all_text_files_in_folder

d = dict()
combo_d = dict()
example_d = dict() # store one path
csv_str = "code,count"
for fp in get_all_text_files_in_folder("../data"):
    language_codes = re.findall(r"-([a-z\d]+)", fp)[0]
    combo_d[language_codes] = combo_d.get(language_codes, 0) + 1
    while language_codes:
        code = language_codes[:3]
        d[code] = d.get(code, 0) + 1
        example_d[code] = fp
        language_codes = language_codes[4:]

print("LANGUAGE CODES:")
for code, count in d.items():
    row = f"\n{code},{count}"
    print(code, count)
    csv_str += row

print()
print("COMBOS:")
for combo, count in combo_d.items():
    print(combo, count)


with open("../language_IDs.csv", mode="w", encoding="utf-8") as file:
    file.write(csv_str)
    
