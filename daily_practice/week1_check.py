import json

def data_dict_counter(file_path):
    type_counter = {}
    with open(file_path, "r") as f:
        data = json.load(f)
    for d in data:
        event_name = d["type"]["name"]
        if event_name in type_counter:
            type_counter[event_name] +=1
        else:
            type_counter[event_name] =1
    return type_counter

if __name__ == "__main__":
    file_path = "/Users/muaazshanji/projects/statsbomb-data/data/events/15946.json"
    print(data_dict_counter(file_path))


