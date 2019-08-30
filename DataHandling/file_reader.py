#Data reader from a JSON file

import json

def read_file(data_path):

    with open(data_path,'r') as in_file:
        data = json.load(in_file)
        in_file.close()
    return data
