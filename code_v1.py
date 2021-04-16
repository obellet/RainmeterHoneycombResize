import os
import configparser
from configparser import ConfigParser

def set_value_in_property_file(file_path, section, key, value):
    config = configparser.RawConfigParser()
    config.read(file_path)
    config.set(section,key,value)                         
    cfgfile = open(file_path,'w')
    config.write(cfgfile, space_around_delimiters=False)  # use flag in case case you need to avoid white space.
    cfgfile.close()

directory = r"C:\Users\Octave\Documents\Rainmeter\Skins\Honeycomb" # use your directory containing the honeycomb .ini files

for subdir, dirs, files in os.walk(directory):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".ini"):
            config = ConfigParser()
            config.read(filepath)
            section_list = list(config.sections())
            set_value_in_property_file(filepath, section_list[0], 'H', '110') # change the value 110 to adjust the size of the icons
        else:
            continue
