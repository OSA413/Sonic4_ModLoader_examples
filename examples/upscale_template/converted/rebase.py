import os
import glob

os.chdir(os.path.dirname(__file__))

the_files = glob.glob("./**/*.dds", recursive = True)

for file in the_files:
    for end in ["de", "us", "es", "fr", "it", "ja", "sp", "en", "jp", "ge"]:
        if "_"+end.upper()+"_1.AMB" not in file:
            continue
        if end == "ge": end = "de"
        if end == "ja": end = "jp"
        if end == "en": end = "us"
        other_place = file.replace("_base", "_"+end)
        if not os.path.exists(os.path.dirname(other_place)):
            os.makedirs(os.path.dirname(other_place))
        os.rename(file, other_place)
