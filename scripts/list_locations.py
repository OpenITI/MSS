import os
from openiti.helper import yml
from openiti.helper.templates import location_yml_template

default_vals = yml.ymlToDic(location_yml_template)

tsv_str = "ID\tcity\tinstitution"
for fn in os.listdir("../data"):
    yml_fp = os.path.join("../data", fn, fn+".yml")
    yml_d = yml.readYML(yml_fp)
    row = "\n" + fn            
    for k in ["CITY", "INST"]:
        val = ""
        for lang in ["EN", "AR"]:
            key = f"10#LOC#{k}#{lang}###:"
            val = yml_d[key]
            if val == default_vals[key]:
                key = ""
            if val:
                break
        row += "\t" + val
    print(row)
    tsv_str += row


with open("../location_IDs.tsv", mode="w", encoding="utf-8") as file:
    file.write(tsv_str)
    
